"""Cross-project integration tests between `crypto-lab` and a live `ctm-ekm-lab` instance.

Runs automatically whenever `CIPHERTRUST_URL` is set in the environment (for example,
after sourcing `/home/jsoehner/ctm-ekm-lab/.env.ciphertrust`). Skips cleanly in
offline CI where no CipherTrust Manager instance is running.
"""

from __future__ import annotations

import os
import ssl
import unittest
import urllib.error

from cryptography.exceptions import InvalidTag

from ciphertrust_ekm_example import (
    CipherTrustClient,
    LiveCipherTrustTransport,
    decrypt_with_ciphertrust,
    encrypt_with_ciphertrust,
)


_CTM_URL = os.environ.get("CIPHERTRUST_URL", "")
if _CTM_URL:
    _mtls = "mTLS enabled" if os.environ.get("CIPHERTRUST_CLIENT_CERT") else "mTLS disabled"
    print(f"\n[CTM STATUS] AVAILABLE — Running live integration tests against {_CTM_URL} ({_mtls})", flush=True)
else:
    print("\n[CTM STATUS] NOT AVAILABLE — CIPHERTRUST_URL unset; skipping live CTM integration tests", flush=True)


@unittest.skipUnless(_CTM_URL, "CIPHERTRUST_URL not set; CTM unavailable (skipping live integration tests)")
class TestLiveCipherTrustIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = CipherTrustClient.from_env()

    def test_01_key_create_and_metadata_lookup(self):
        meta = self.client.create_aes256_key("ctm-int-primary")
        self.assertEqual(meta["algorithm"], "AES")
        self.assertEqual(meta["size"], 256)
        self.assertEqual(meta["state"], "Active")

        fetched = self.client.get_key_metadata("ctm-int-primary")
        self.assertEqual(fetched["name"], "ctm-int-primary")
        self.assertGreaterEqual(fetched["version"], 1)

    def test_02_live_envelope_roundtrip(self):
        self.client.create_aes256_key("ctm-int-envelope")
        aad = b"tenant=acme;env=live-ctm"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-envelope", b"live ctm payload", aad)
        self.assertEqual(decrypt_with_ciphertrust(self.client, env, aad), b"live ctm payload")

    def test_03_wrong_aad_and_tampered_ciphertext_rejected(self):
        self.client.create_aes256_key("ctm-int-tamper")
        aad = b"tenant=acme;op=write"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-tamper", b"sensitive", aad)

        # Wrong AAD fails at CTM KEK unwrap (HTTP 400)
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env, b"tenant=evil;op=write")
        self.assertEqual(ctx.exception.code, 400)

        # Tampered local ciphertext fails AES-256-GCM tag check
        tampered_ct = bytearray(env.ciphertext)
        tampered_ct[0] ^= 0xFF
        bad_env = type(env)(
            key_name=env.key_name,
            wrapped_dek=env.wrapped_dek,
            nonce=env.nonce,
            ciphertext=bytes(tampered_ct),
        )
        with self.assertRaises(InvalidTag):
            decrypt_with_ciphertrust(self.client, bad_env, aad)

    def test_04_kill_switch_deactivate_and_reactivate(self):
        self.client.create_aes256_key("ctm-int-killswitch")
        aad = b"app=payments"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-killswitch", b"ledger entry", aad)

        # Deactivate -> HTTP 403 immediately blocks decryption
        self.client.deactivate_key("ctm-int-killswitch")
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env, aad)
        self.assertEqual(ctx.exception.code, 403)

        # Reactivate -> decryption succeeds again
        self.client.reactivate_key("ctm-int-killswitch")
        self.assertEqual(decrypt_with_ciphertrust(self.client, env, aad), b"ledger entry")

    def test_05_key_rotation_preserves_old_version_decryption(self):
        self.client.create_aes256_key("ctm-int-rotate")
        aad = b"service=vault"
        env_v1 = encrypt_with_ciphertrust(self.client, "ctm-int-rotate", b"payload-v1", aad)
        self.assertEqual(env_v1.wrapped_dek.get("version"), 1)

        rot = self.client.rotate_key("ctm-int-rotate")
        self.assertEqual(rot["version"], 2)

        env_v2 = encrypt_with_ciphertrust(self.client, "ctm-int-rotate", b"payload-v2", aad)
        self.assertEqual(env_v2.wrapped_dek.get("version"), 2)

        self.assertEqual(decrypt_with_ciphertrust(self.client, env_v1, aad), b"payload-v1")
        self.assertEqual(decrypt_with_ciphertrust(self.client, env_v2, aad), b"payload-v2")

    def test_06_multi_tenant_isolation(self):
        self.client.create_aes256_key("ctm-tenant-a")
        self.client.create_aes256_key("ctm-tenant-b")

        env_a = encrypt_with_ciphertrust(self.client, "ctm-tenant-a", b"tenant-a-data", b"a")
        env_b = encrypt_with_ciphertrust(self.client, "ctm-tenant-b", b"tenant-b-data", b"b")

        # Revoke Tenant A only; Tenant B remains operational
        self.client.deactivate_key("ctm-tenant-a")
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env_a, b"a")
        self.assertEqual(ctx.exception.code, 403)
        self.assertEqual(decrypt_with_ciphertrust(self.client, env_b, b"b"), b"tenant-b-data")

    def test_07_invalid_credentials_and_invalid_jwt_rejected(self):
        url = os.environ["CIPHERTRUST_URL"]
        ca = os.environ.get("CIPHERTRUST_CA_BUNDLE")
        cert = os.environ.get("CIPHERTRUST_CLIENT_CERT")
        key = os.environ.get("CIPHERTRUST_CLIENT_KEY")

        with self.assertRaises(urllib.error.HTTPError) as bad_pw:
            LiveCipherTrustTransport(
                base_url=url,
                username=os.environ.get("CIPHERTRUST_USER", "admin"),
                password="definitely-wrong-password",
                ca_bundle=ca,
                client_cert=cert,
                client_key=key,
            )
        self.assertEqual(bad_pw.exception.code, 401)

        bad_token_client = CipherTrustClient(
            LiveCipherTrustTransport(
                base_url=url,
                token="invalid.jwt.token",
                ca_bundle=ca,
                client_cert=cert,
                client_key=key,
            )
        )
        with self.assertRaises(urllib.error.HTTPError) as bad_jwt:
            bad_token_client.get_key_metadata("ctm-int-primary")
        self.assertEqual(bad_jwt.exception.code, 401)

    def test_08_missing_mtls_client_cert_rejected_when_enforced(self):
        if not os.environ.get("CIPHERTRUST_CLIENT_CERT"):
            self.skipTest("mTLS client cert not configured")
        url = os.environ["CIPHERTRUST_URL"]
        ca = os.environ.get("CIPHERTRUST_CA_BUNDLE")
        with self.assertRaises((ssl.SSLError, urllib.error.URLError)):
            LiveCipherTrustTransport(
                base_url=url,
                username=os.environ.get("CIPHERTRUST_USER", "admin"),
                password=os.environ.get("CIPHERTRUST_PASSWORD", ""),
                ca_bundle=ca,
                client_cert=None,
                client_key=None,
            )


if __name__ == "__main__":
    unittest.main()
