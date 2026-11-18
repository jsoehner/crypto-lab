"""GCP Cloud KMS / Cloud HSM: BYOK (Bring Your Own Key) and CMK Envelope Encryption.

Demonstrates mainstream usage of `google-cloud-kms` without an External Key
Management (EKM) platform:
  1. BYOK: Wrap local key material with a GCP Cloud KMS ImportJob public key
     (RSA-OAEP-3072-SHA256 + AES-256-KWP) for HSM-backed import.
  2. CMK Envelope Encryption: Encrypt a local AES-256-GCM Data Encryption Key
     (DEK) using a GCP Cloud HSM `CryptoKey` with Additional Authenticated Data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.keywrap import aes_key_wrap_with_padding, aes_key_unwrap_with_padding

from crypto_support import random_bytes


class GcpKmsClient(Protocol):
    """Subset of google.cloud.kms.KeyManagementServiceClient used for CMK envelope wrapping."""

    def encrypt(self, key_name: str, plaintext: bytes, additional_authenticated_data: bytes) -> bytes: ...
    def decrypt(self, key_name: str, ciphertext: bytes, additional_authenticated_data: bytes) -> bytes: ...


class SimulatedGcpCloudHsm:
    """In-memory simulator of GCP Cloud KMS / Cloud HSM for offline verification.

    In production, replace with:
        from google.cloud import kms
        client = kms.KeyManagementServiceClient()
        key_name = client.crypto_key_path(project, location, key_ring, crypto_key)
        resp = client.encrypt(request={
            "name": key_name,
            "plaintext": dek,
            "additional_authenticated_data": aad,
        })
    """

    def __init__(self) -> None:
        self._import_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)
        self.import_job_public = self._import_private.public_key()
        self._hsm_kek = random_bytes(32)
        self.imported_keys: dict[str, bytes] = {}

    def import_crypto_key_version(self, key_name: str, wrapped_key_blob: bytes) -> str:
        """Simulate GCP Cloud KMS ImportJob unwrapping inside Cloud HSM."""
        ephemeral_aes = self._import_private.decrypt(
            wrapped_key_blob[:384],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        imported_material = aes_key_unwrap_with_padding(ephemeral_aes, wrapped_key_blob[384:])
        self.imported_keys[key_name] = imported_material
        return f"{key_name}/cryptoKeyVersions/1"

    def encrypt(self, key_name: str, plaintext: bytes, additional_authenticated_data: bytes) -> bytes:
        nonce = random_bytes(12)
        ct = AESGCM(self._hsm_kek).encrypt(nonce, plaintext, key_name.encode("utf-8") + additional_authenticated_data)
        return nonce + ct

    def decrypt(self, key_name: str, ciphertext: bytes, additional_authenticated_data: bytes) -> bytes:
        nonce, ct = ciphertext[:12], ciphertext[12:]
        return AESGCM(self._hsm_kek).decrypt(nonce, ct, key_name.encode("utf-8") + additional_authenticated_data)


def prepare_gcp_byok_blob(import_job_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:
    """Wrap key material using GCP's RSA_OAEP_3072_SHA256_AES_256 import method."""
    ephemeral_aes = random_bytes(32)
    wrapped_ephemeral = import_job_public.encrypt(
        ephemeral_aes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    wrapped_target = aes_key_wrap_with_padding(ephemeral_aes, target_key_material)
    return wrapped_ephemeral + wrapped_target


@dataclass(frozen=True)
class GcpCmkEnvelope:
    key_name: str
    wrapped_dek: bytes
    nonce: bytes
    ciphertext: bytes


def encrypt_with_gcp_cmk(
    kms_client: GcpKmsClient,
    key_name: str,
    plaintext: bytes,
    aad: bytes,
) -> GcpCmkEnvelope:
    """Envelope-encrypt data using a local AES-256-GCM DEK wrapped by GCP Cloud HSM."""
    dek = random_bytes(32)
    wrapped_dek = kms_client.encrypt(key_name, dek, aad)
    nonce = random_bytes(12)
    ciphertext = AESGCM(dek).encrypt(nonce, plaintext, aad)
    return GcpCmkEnvelope(key_name=key_name, wrapped_dek=wrapped_dek, nonce=nonce, ciphertext=ciphertext)


def decrypt_with_gcp_cmk(
    kms_client: GcpKmsClient,
    envelope: GcpCmkEnvelope,
    aad: bytes,
) -> bytes:
    """Unwrap the DEK via GCP Cloud KMS and decrypt locally."""
    dek = kms_client.decrypt(envelope.key_name, envelope.wrapped_dek, aad)
    return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    kms = SimulatedGcpCloudHsm()
    key_name = "projects/demo-proj/locations/us-central1/keyRings/app-ring/cryptoKeys/cmk-hsm"

    # 1. BYOK: Wrap on-premises key and import into GCP Cloud HSM
    on_prem_key = random_bytes(32)
    byok_blob = prepare_gcp_byok_blob(kms.import_job_public, on_prem_key)
    version_name = kms.import_crypto_key_version(key_name, byok_blob)

    # 2. CMK Envelope Encryption
    aad = b"service=billing;env=prod"
    envelope = encrypt_with_gcp_cmk(kms, key_name, b"gcp confidential record", aad)
    plaintext = decrypt_with_gcp_cmk(kms, envelope, aad)
    assert plaintext == b"gcp confidential record"
    print(f"GcpKmsByokCmkExample OK version={version_name}")


if __name__ == "__main__":
    main()
