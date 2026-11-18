"""Unit tests for Azure Key Vault BYOK/CMK, GCP Cloud KMS BYOK/CMK, and External KMS (EKM/HYOK)."""

import unittest
from cryptography.exceptions import InvalidTag

from azure_keyvault_byok_cmk_example import (
    SimulatedAzureManagedHsm,
    decrypt_with_azure_cmk,
    encrypt_with_azure_cmk,
    prepare_azure_byok_blob,
)
from crypto_support import random_bytes
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


class TestCloudKmsPatterns(unittest.TestCase):
    def test_azure_byok_and_cmk_envelope(self):
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
        ekm = ExternalKmsControlPlane()
        caller = "spiffe://cloud/sa/app"
        key_uri = ekm.create_key("root-kek", allowed_callers={caller})
        aad = b"obj=123"

        env = cloud_encrypt_with_ekm(ekm, key_uri, b"ekm payload", aad, caller=caller, justification="WRITE")
        self.assertEqual(
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE"),
            b"ekm payload",
        )

        # Justification mismatch must fail (bound as AAD)
        with self.assertRaises(InvalidTag):
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="DIFFERENT_REASON")

        # Unauthorized caller must be denied and logged
        with self.assertRaises(PermissionError):
            cloud_decrypt_with_ekm(ekm, env, aad, caller="spiffe://cloud/sa/rogue", justification="WRITE")

        # Instant kill-switch blocks decryption immediately
        ekm.disable_key(key_uri, actor="secops", reason="incident")
        with self.assertRaises(PermissionError):
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE")

        # Re-enable restores access; destroy permanently zeroizes
        ekm.enable_key(key_uri, actor="secops", reason="cleared")
        self.assertEqual(
            cloud_decrypt_with_ekm(ekm, env, aad, caller=caller, justification="WRITE"),
            b"ekm payload",
        )
        ekm.destroy_key(key_uri, actor="secops", reason="decommission")
        self.assertEqual(ekm._keys[key_uri].state, KeyState.DESTROYED)
        with self.assertRaises(PermissionError):
            ekm.enable_key(key_uri, actor="secops", reason="attempt-restore")


if __name__ == "__main__":
    unittest.main()
