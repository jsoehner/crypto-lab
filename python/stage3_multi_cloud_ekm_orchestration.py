"""Stage 3: External KMS (Root of Trust) + Vault Transit (App Broker) + Cloud/SaaS Vaults.

Demonstrates the 3-tier sovereign key hierarchy:
  1. Sovereign External KMS (CipherTrust / HYOK): Holds the Root KEK; never exported.
  2. HashiCorp Vault Transit (App Broker): Receives a wrapped Service KEK and enforces
     OIDC JWT + mTLS for fast application-level DEK wrapping.
  3. Cloud / SaaS Vaults (Azure Key Vault, GCP Cloud KMS, SaaS Tenant Vaults): Hold
     cloud-side or BYOK-wrapped tenant keys anchored to the External KMS.

When the Sovereign External KMS disables the Root KEK, downstream Vault and Cloud/SaaS
key unwraps are immediately blocked from a single control plane.
"""

from __future__ import annotations

from dataclasses import dataclass

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from ciphertrust_ekm_example import CipherTrustClient, SimulatedCipherTrustTransport
from crypto_support import random_bytes


@dataclass(frozen=True)
class MultiCloudEnvelope:
    target_cloud: str
    wrapped_service_kek: dict[str, str]
    wrapped_dek: bytes
    nonce: bytes
    ciphertext: bytes


class Stage3MultiCloudOrchestrator:
    """Orchestrates Root KEK (CTM) -> Service KEK (Vault/Cloud Vault) -> App DEK."""

    def __init__(self, ctm_client: CipherTrustClient, root_kek_name: str) -> None:
        self.ctm = ctm_client
        self.root_kek_name = root_kek_name
        self.ctm.create_aes256_key(root_kek_name)

    def encrypt_for_target(
        self,
        target_cloud: str,
        plaintext: bytes,
        aad: bytes,
    ) -> MultiCloudEnvelope:
        # 1. Generate a Service/Cloud KEK (e.g., for Vault Transit or Azure/GCP/SaaS Vault)
        service_kek = random_bytes(32)
        # 2. Wrap the Service KEK under the Sovereign External KMS Root KEK
        wrapped_service_kek = self.ctm.wrap_dek(
            self.root_kek_name,
            service_kek,
            aad=target_cloud.encode("utf-8"),
        )
        # 3. Cloud/Vault broker wraps the local AES-256-GCM DEK using the Service KEK
        dek = random_bytes(32)
        dek_nonce = random_bytes(12)
        wrapped_dek = dek_nonce + AESGCM(service_kek).encrypt(dek_nonce, dek, aad)

        # 4. Application encrypts payload locally with the DEK
        data_nonce = random_bytes(12)
        ciphertext = AESGCM(dek).encrypt(data_nonce, plaintext, aad)
        return MultiCloudEnvelope(
            target_cloud=target_cloud,
            wrapped_service_kek=wrapped_service_kek,
            wrapped_dek=wrapped_dek,
            nonce=data_nonce,
            ciphertext=ciphertext,
        )

    def decrypt_for_target(self, envelope: MultiCloudEnvelope, aad: bytes) -> bytes:
        # Unwrapping the Service KEK requires live authorization from the External KMS
        service_kek = self.ctm.unwrap_dek(
            self.root_kek_name,
            envelope.wrapped_service_kek,
            aad=envelope.target_cloud.encode("utf-8"),
        )
        dek_nonce, dek_ct = envelope.wrapped_dek[:12], envelope.wrapped_dek[12:]
        dek = AESGCM(service_kek).decrypt(dek_nonce, dek_ct, aad)
        return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    ctm = CipherTrustClient(SimulatedCipherTrustTransport())
    orchestrator = Stage3MultiCloudOrchestrator(ctm, "sovereign-root-kek")

    aad = b"tenant=enterprise-1;classification=restricted"
    vault_env = orchestrator.encrypt_for_target("vault-transit", b"app-tier secret", aad)
    azure_env = orchestrator.encrypt_for_target("azure-keyvault", b"azure-saas secret", aad)
    gcp_env = orchestrator.encrypt_for_target("gcp-cloud-kms", b"gcp-analytics secret", aad)

    assert orchestrator.decrypt_for_target(vault_env, aad) == b"app-tier secret"
    assert orchestrator.decrypt_for_target(azure_env, aad) == b"azure-saas secret"
    assert orchestrator.decrypt_for_target(gcp_env, aad) == b"gcp-analytics secret"
    print("Stage3MultiCloudOrchestrator OK targets=[vault-transit, azure-keyvault, gcp-cloud-kms]")


if __name__ == "__main__":
    main()
