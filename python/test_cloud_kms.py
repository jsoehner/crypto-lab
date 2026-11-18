"""Unit tests for Azure BYOK/CMK, GCP BYOK/CMK, and External KMS (EKM/HYOK) with educational context."""

import unittest
from cryptography.exceptions import InvalidTag

from azure_keyvault_byok_cmk_example import (
    SimulatedAzureManagedHsm,
    decrypt_with_azure_cmk,
    encrypt_with_azure_cmk,
    prepare_azure_byok_blob,
)
from ciphertrust_ekm_example import (
    CipherTrustClient,
    SimulatedCipherTrustTransport,
    decrypt_with_ciphertrust,
    encrypt_with_ciphertrust,
)
from crypto_support import random_bytes
from edu_output import print_edu_case
from external_kms_ekm_example import (
    ExternalKmsControlPlane,
    KeyState,
    cloud_decrypt_with_ekm,
    cloud_encrypt_with_ekm,
)
from gcp_kms_byok_cmk_example import (
    SimulatedGcpCloudHsm,
    decrypt_with_gcp_cmk,
    encrypt_with_gcp_cmk,
    prepare_gcp_byok_blob,
)
from vault_ekm_proxy_example import (
    SimulatedVaultEkmProxy,
    decrypt_with_ekm_proxy,
    encrypt_with_ekm_proxy,
)
from stage3_multi_cloud_ekm_orchestration import Stage3MultiCloudOrchestrator


class TestCloudKmsPatterns(unittest.TestCase):
    def test_azure_byok_and_cmk_envelope(self):
        print_edu_case(
            "Azure Managed HSM: BYOK + CMK Envelope Encryption (No External EKM)",
            "Organizations want to generate root keys on-premises and import them into Azure HSM without exposing raw key material in transit.",
            "Wrapping an on-prem key with RSA-OAEP-256 + AES-256-KWP for BYOK import, then wrapping a local AES-256-GCM DEK with the Azure CMK.",
            "BYOK keeps key generation sovereign, while envelope encryption keeps bulk data fast and local while protecting the DEK inside Azure HSM.",
        )
        hsm = SimulatedAzureManagedHsm()
        on_prem_key = random_bytes(32)
        blob = prepare_azure_byok_blob(hsm.kek_public, on_prem_key)
        key_id = hsm.import_byok_key("cmk-1", blob)
        self.assertIn("cmk-1", key_id)
        self.assertEqual(hsm.imported_keys["cmk-1"], on_prem_key)

        aad = b"tenant=acme"
        env = encrypt_with_azure_cmk(hsm, b"azure secret", aad)
        self.assertEqual(decrypt_with_azure_cmk(hsm, env, aad), b"azure secret")
        with self.assertRaises(InvalidTag):
            decrypt_with_azure_cmk(hsm, env, b"wrong-aad")

    def test_gcp_byok_and_cmk_envelope(self):
        print_edu_case(
            "GCP Cloud KMS / Cloud HSM: BYOK + CMK Envelope Encryption (No External EKM)",
            "Cloud workloads need customer-managed HSM keys with strict context binding so wrapped DEKs cannot be replayed across services.",
            "Wrapping key material for a GCP ImportJob (RSA-OAEP-3072-SHA256 + AES-256-KWP) and wrapping DEKs with key-name + AAD.",
            "Binding the GCP CryptoKey resource name and service AAD prevents cross-environment ciphertext substitution.",
        )
        kms = SimulatedGcpCloudHsm()
        key_name = "projects/p/locations/us/keyRings/r/cryptoKeys/k"
        on_prem_key = random_bytes(32)
        blob = prepare_gcp_byok_blob(kms.import_job_public, on_prem_key)
        version = kms.import_crypto_key_version(key_name, blob)
        self.assertTrue(version.endswith("/cryptoKeyVersions/1"))
        self.assertEqual(kms.imported_keys[key_name], on_prem_key)

        aad = b"service=ledger"
        env = encrypt_with_gcp_cmk(kms, key_name, b"gcp secret", aad)
        self.assertEqual(decrypt_with_gcp_cmk(kms, env, aad), b"gcp secret")
        with self.assertRaises(InvalidTag):
            decrypt_with_gcp_cmk(kms, env, b"wrong-aad")

    def test_external_kms_ekm_control_and_kill_switch(self):
        print_edu_case(
            "External KMS (EKM / HYOK): Sovereign Control Plane & Kill-Switch",
            "Regulated workloads cannot allow cloud providers to hold root KEKs or decrypt data after an incident or subpoena.",
            "Testing caller allowlists, justification AAD binding, disable_key() kill-switch, enable_key() recovery, and destroy_key() zeroization.",
            "Because the root KEK never leaves your external KMS, disabling it instantly renders all cloud-stored ciphertexts unreadable.",
        )
        ekm = ExternalKmsControlPlane()
        caller = "spiffe://cloud/sa/app"
        key_uri = ekm.create_key("root-kek", allowed_callers={caller})
        aad = b"obj=123"

        env = cloud_encrypt_with_ekm(ekm, key_uri, b"ekm payload", aad, caller=caller, justification="WRITE")
        self.assertEqual(
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE"),
            b"ekm payload",
        )

        with self.assertRaises(InvalidTag):
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="DIFFERENT_REASON")

        with self.assertRaises(PermissionError):
            cloud_decrypt_with_ekm(ekm, env, aad, caller="spiffe://cloud/sa/rogue", justification="WRITE")

        ekm.disable_key(key_uri, actor="secops", reason="incident")
        with self.assertRaises(PermissionError):
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE")

        ekm.enable_key(key_uri, actor="secops", reason="cleared")
        self.assertEqual(
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE"),
            b"ekm payload",
        )
        ekm.destroy_key(key_uri, actor="secops", reason="decommission")
        self.assertEqual(ekm._keys[key_uri].state, KeyState.DESTROYED)
        with self.assertRaises(PermissionError):
            ekm.enable_key(key_uri, actor="secops", reason="attempt-restore")

    def test_ciphertrust_rest_ekm_envelope_and_revocation(self):
        print_edu_case(
            "CipherTrust Manager REST Client (Offline Protocol Simulator)",
            "Teams need to test CipherTrust REST EKM integrations in CI without standing up a full 8 GB appliance.",
            "Running CipherTrustClient against SimulatedCipherTrustTransport for key creation, DEK wrap/unwrap, AAD check, and deactivation.",
            "Using a protocol-compatible transport interface lets the exact same application code run in offline CI and against live CipherTrust.",
        )
        client = CipherTrustClient(SimulatedCipherTrustTransport())
        key_meta = client.create_aes256_key("cm-ce-kek")
        self.assertEqual(key_meta["state"], "Active")

        aad = b"env=lab;app=orders"
        env = encrypt_with_ciphertrust(client, "cm-ce-kek", b"ciphertrust secret", aad)
        self.assertEqual(decrypt_with_ciphertrust(client, env, aad), b"ciphertrust secret")

        with self.assertRaises(InvalidTag):
            decrypt_with_ciphertrust(client, env, b"wrong-aad")

        client.deactivate_key("cm-ce-kek")
        with self.assertRaises(PermissionError):
            decrypt_with_ciphertrust(client, env, aad)

    def test_vault_oidc_ekm_proxy_and_rate_limit(self):
        print_edu_case(
            "OIDC + mTLS EKM Proxy (HashiCorp Vault Transit Pattern)",
            "Applications need Layer-7 OIDC identity validation and rate limiting in front of Layer-4 mTLS Vault Transit KEKs.",
            "Wrapping/unwrapping a DEK via SimulatedVaultEkmProxy with valid JWT, invalid JWT (401), wrong AAD, and rate-limit (429).",
            "Separating OIDC identity enforcement from Vault mTLS prevents unauthenticated callers from reaching the HSM/KMS engine.",
        )
        valid_jwt = "oidc.jwt.alice"
        proxy = SimulatedVaultEkmProxy(valid_tokens={valid_jwt}, max_requests_per_window=4)
        aad = b"realm=ekm-demo"

        env = encrypt_with_ekm_proxy(proxy, valid_jwt, b"vault secret", aad)
        self.assertEqual(decrypt_with_ekm_proxy(proxy, valid_jwt, env, aad), b"vault secret")

        with self.assertRaises(InvalidTag):
            decrypt_with_ekm_proxy(proxy, valid_jwt, env, b"wrong-aad")

        with self.assertRaises(PermissionError):
            decrypt_with_ekm_proxy(proxy, "expired.or.forged.jwt", env, aad)

        # 5th request in window triggers 429 rate limit
        with self.assertRaises(RuntimeError):
            decrypt_with_ekm_proxy(proxy, valid_jwt, env, aad)

    def test_stage3_ekm_vault_cloud_cascade_revocation(self):
        print_edu_case(
            "Stage 3: External KMS + Vault + Cloud/SaaS Multi-Cloud Cascade",
            "Enterprises using Vault, Azure Key Vault, GCP Cloud KMS, and SaaS vaults risk fragmented key revocation during an incident.",
            "Anchoring Vault, Azure, and GCP Service KEKs to a single Sovereign Root KEK, then deactivating the Root KEK.",
            "One kill-switch action in the External KMS cascades across Vault and every Cloud/SaaS vault simultaneously.",
        )
        ctm = CipherTrustClient(SimulatedCipherTrustTransport())
        orch = Stage3MultiCloudOrchestrator(ctm, "stage3-root-kek")
        aad = b"org=global"

        env_vault = orch.encrypt_for_target("vault-transit", b"vault-data", aad)
        env_azure = orch.encrypt_for_target("azure-keyvault", b"azure-data", aad)
        env_gcp = orch.encrypt_for_target("gcp-cloud-kms", b"gcp-data", aad)

        self.assertEqual(orch.decrypt_for_target(env_vault, aad), b"vault-data")
        self.assertEqual(orch.decrypt_for_target(env_azure, aad), b"azure-data")
        self.assertEqual(orch.decrypt_for_target(env_gcp, aad), b"gcp-data")

        # Single Root KEK deactivation cascades across all 3 platforms
        ctm.deactivate_key("stage3-root-kek")
        for env in (env_vault, env_azure, env_gcp):
            with self.assertRaises(PermissionError):
                orch.decrypt_for_target(env, aad)


if __name__ == "__main__":
    unittest.main()
