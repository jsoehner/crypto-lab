"""Azure Key Vault / Managed HSM: BYOK (Bring Your Own Key) and CMK Envelope Encryption.

Demonstrates mainstream usage of `azure-identity` and `azure-keyvault-keys`
without an External Key Management (EKM) platform:
  1. BYOK: Wrap an on-premises key using the Azure Key Vault / Managed HSM
     RSA-OAEP-256 Key Exchange Key (KEK) + AES-256-KWP (RFC 5649) before import.
  2. CMK Envelope Encryption: Generate a local AES-256-GCM Data Encryption Key
     (DEK), wrap it with the cloud HSM-backed KEK via `CryptographyClient`, and
     encrypt application data locally.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.keywrap import aes_key_wrap_with_padding, aes_key_unwrap_with_padding

from crypto_support import random_bytes


class AzureKeyVaultCryptoClient(Protocol):
    """Subset of azure.keyvault.keys.crypto.CryptographyClient used for CMK wrapping."""

    def wrap_key(self, algorithm: str, key: bytes) -> bytes: ...
    def unwrap_key(self, algorithm: str, encrypted_key: bytes) -> bytes: ...


class SimulatedAzureManagedHsm:
    """In-memory simulator of an Azure Managed HSM KEK for offline verification.

    In production, replace with:
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.keys import KeyClient
        from azure.keyvault.keys.crypto import CryptographyClient, KeyWrapAlgorithm

        credential = DefaultAzureCredential()
        key_client = KeyClient(vault_url="https://<vault>.vault.azure.net/", credential=credential)
        kek = key_client.get_key("<kek-name>")
        crypto_client = CryptographyClient(kek, credential=credential)
    """

    def __init__(self) -> None:
        self._kek_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)
        self.kek_public = self._kek_private.public_key()
        self.imported_keys: dict[str, bytes] = {}

    def import_byok_key(self, key_name: str, wrapped_byok_blob: bytes) -> str:
        """Unwrap a BYOK blob (RSA-OAEP-256 wrapped AES-KWP key) inside the HSM boundary."""
        # Format: 384-byte RSA-3072 OAEP-SHA256 wrapped ephemeral KEK || AES-KWP wrapped target key
        ephemeral_kek = self._kek_private.decrypt(
            wrapped_byok_blob[:384],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        target_key = aes_key_unwrap_with_padding(ephemeral_kek, wrapped_byok_blob[384:])
        self.imported_keys[key_name] = target_key
        return f"https://example-hsm.managedhsm.azure.net/keys/{key_name}/v1"

    def wrap_key(self, algorithm: str, key: bytes) -> bytes:
        if algorithm != "RSA-OAEP-256":
            raise ValueError(f"Unsupported key wrap algorithm: {algorithm}")
        return self.kek_public.encrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

    def unwrap_key(self, algorithm: str, encrypted_key: bytes) -> bytes:
        if algorithm != "RSA-OAEP-256":
            raise ValueError(f"Unsupported key wrap algorithm: {algorithm}")
        return self._kek_private.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )


def prepare_azure_byok_blob(hsm_kek_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:
    """Wrap an on-prem key for Azure Managed HSM BYOK import (CKM_RSA_AES_KEY_WRAP pattern)."""
    ephemeral_aes_kek = random_bytes(32)
    wrapped_ephemeral = hsm_kek_public.encrypt(
        ephemeral_aes_kek,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    wrapped_target = aes_key_wrap_with_padding(ephemeral_aes_kek, target_key_material)
    return wrapped_ephemeral + wrapped_target


@dataclass(frozen=True)
class AzureCmkEnvelope:
    wrapped_dek: bytes
    nonce: bytes
    ciphertext: bytes


def encrypt_with_azure_cmk(
    crypto_client: AzureKeyVaultCryptoClient,
    plaintext: bytes,
    aad: bytes,
) -> AzureCmkEnvelope:
    """Envelope-encrypt data using a local AES-256-GCM DEK wrapped by an Azure HSM CMK."""
    dek = random_bytes(32)
    wrapped_dek = crypto_client.wrap_key("RSA-OAEP-256", dek)
    nonce = random_bytes(12)
    ciphertext = AESGCM(dek).encrypt(nonce, plaintext, aad)
    return AzureCmkEnvelope(wrapped_dek=wrapped_dek, nonce=nonce, ciphertext=ciphertext)


def decrypt_with_azure_cmk(
    crypto_client: AzureKeyVaultCryptoClient,
    envelope: AzureCmkEnvelope,
    aad: bytes,
) -> bytes:
    """Unwrap the DEK via Azure Key Vault / Managed HSM and decrypt locally."""
    dek = crypto_client.unwrap_key("RSA-OAEP-256", envelope.wrapped_dek)
    return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    hsm = SimulatedAzureManagedHsm()

    # 1. BYOK: Wrap an on-premises 256-bit key and import into Azure Managed HSM
    on_prem_key = random_bytes(32)
    byok_blob = prepare_azure_byok_blob(hsm.kek_public, on_prem_key)
    key_id = hsm.import_byok_key("customer-master-key", byok_blob)

    # 2. CMK Envelope Encryption
    aad = b"tenant=acme;region=eastus2"
    envelope = encrypt_with_azure_cmk(hsm, b"sensitive customer payload", aad)
    plaintext = decrypt_with_azure_cmk(hsm, envelope, aad)
    assert plaintext == b"sensitive customer payload"
    print(f"AzureKeyVaultByokCmkExample OK keyId={key_id}")


if __name__ == "__main__":
    main()
