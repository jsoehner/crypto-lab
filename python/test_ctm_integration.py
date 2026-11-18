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
from edu_output import GREEN, RESET, YELLOW, print_edu_case

_CTM_URL = os.environ.get("CIPHERTRUST_URL", "")
if _CTM_URL:
    _mtls = "mTLS enabled" if os.environ.get("CIPHERTRUST_CLIENT_CERT") else "mTLS disabled"
    print(f"\n{GREEN}[CTM STATUS] AVAILABLE{RESET} — Running live integration tests against {_CTM_URL} ({_mtls})", flush=True)
else:
    print(f"\n{YELLOW}[CTM STATUS] NOT AVAILABLE{RESET} — CIPHERTRUST_URL unset; skipping live CTM integration tests", flush=True)


@unittest.skipUnless(_CTM_URL, "CIPHERTRUST_URL not set; CTM unavailable (skipping live integration tests)")
class TestLiveCipherTrustIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = CipherTrustClient.from_env()

    def test_01_key_create_and_metadata_lookup(self):
        print_edu_case(
            "CTM Live Test 01: Key Provisioning & Metadata Inspection",
            "Applications must verify that keys created in an external KMS meet policy (AES-256, Active) before encrypting production data.",
            "Calling POST /api/v1/vault/keys2 and GET /api/v1/vault/keys2/ctm-int-primary over mTLS + JWT.",
            "Centralized key provisioning enforces 256-bit Grover-resistant KEKs and unexportable key policies outside the application.",
        )
        meta = self.client.create_aes256_key("ctm-int-primary")
        self.assertEqual(meta["algorithm"], "AES")
        self.assertEqual(meta["size"], 256)
        self.assertEqual(meta["state"], "Active")

        fetched = self.client.get_key_metadata("ctm-int-primary")
        self.assertEqual(fetched["name"], "ctm-int-primary")
        self.assertGreaterEqual(fetched["version"], 1)

    def test_02_live_envelope_roundtrip(self):
        print_edu_case(
            "CTM Live Test 02: Live Envelope Encryption Round-Trip",
            "Sending large payloads to a remote KMS adds latency and exposes plaintext over the network.",
            "Generating a local 256-bit DEK, wrapping only the 32-byte DEK via CTM, and encrypting the payload locally with AES-256-GCM.",
            "Envelope encryption keeps bulk data fast and local while ensuring the root KEK never leaves the CipherTrust control plane.",
        )
        self.client.create_aes256_key("ctm-int-envelope")
        aad = b"tenant=acme;env=live-ctm"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-envelope", b"live ctm payload", aad)
        self.assertEqual(decrypt_with_ciphertrust(self.client, env, aad), b"live ctm payload")

    def test_03_wrong_aad_and_tampered_ciphertext_rejected(self):
        print_edu_case(
            "CTM Live Test 03: AAD Context Binding & Tamper Rejection",
            "An attacker with storage access might copy an encrypted record into a different tenant's bucket or flip ciphertext bytes.",
            "Attempting unwrap with wrong AAD (expecting HTTP 400 from CTM) and decrypting tampered ciphertext (expecting InvalidTag).",
            "Binding tenant/context AAD at both the KEK unwrap and local DEK layers stops cross-tenant replay and silent tampering.",
        )
        self.client.create_aes256_key("ctm-int-tamper")
        aad = b"tenant=acme;op=write"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-tamper", b"sensitive", aad)

        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env, b"tenant=evil;op=write")
        self.assertEqual(ctx.exception.code, 400)

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
        print_edu_case(
            "CTM Live Test 04: Cryptographic Kill-Switch & Recovery",
            "During a cloud breach or legal hold, security teams must cut off data access immediately without deleting storage.",
            "Deactivating ctm-int-killswitch (verifying HTTP 403 blocks decrypt), then reactivating it to restore access.",
            "Because the external KMS mediates every DEK unwrap, deactivating the KEK acts as an instant global kill-switch.",
        )
        self.client.create_aes256_key("ctm-int-killswitch")
        aad = b"app=payments"
        env = encrypt_with_ciphertrust(self.client, "ctm-int-killswitch", b"ledger entry", aad)

        self.client.deactivate_key("ctm-int-killswitch")
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env, aad)
        self.assertEqual(ctx.exception.code, 403)

        self.client.reactivate_key("ctm-int-killswitch")
        self.assertEqual(decrypt_with_ciphertrust(self.client, env, aad), b"ledger entry")

    def test_05_key_rotation_preserves_old_version_decryption(self):
        print_edu_case(
            "CTM Live Test 05: Versioned Key Rotation (v1 -> v2)",
            "Rotating keys by re-encrypting terabytes of data causes downtime; failing to rotate increases key-wear exposure.",
            "Wrapping payload-v1 under v1, rotating KEK to v2, wrapping payload-v2 under v2, and verifying both decrypt cleanly.",
            "Versioned KEKs let new data use fresh key material immediately while old envelopes remain readable during gradual re-wrap.",
        )
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
        print_edu_case(
            "CTM Live Test 06: Multi-Tenant Blast-Radius Isolation",
            "Sharing a single KEK across all customers means revoking one compromised tenant breaks everyone else.",
            "Provisioning ctm-tenant-a and ctm-tenant-b, deactivating Tenant A, and verifying Tenant B continues operating.",
            "Per-tenant KEKs enable surgical offboarding and incident containment with zero impact on healthy tenants.",
        )
        self.client.create_aes256_key("ctm-tenant-a")
        self.client.create_aes256_key("ctm-tenant-b")

        env_a = encrypt_with_ciphertrust(self.client, "ctm-tenant-a", b"tenant-a-data", b"a")
        env_b = encrypt_with_ciphertrust(self.client, "ctm-tenant-b", b"tenant-b-data", b"b")

        self.client.deactivate_key("ctm-tenant-a")
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            decrypt_with_ciphertrust(self.client, env_a, b"a")
        self.assertEqual(ctx.exception.code, 403)
        self.assertEqual(decrypt_with_ciphertrust(self.client, env_b, b"b"), b"tenant-b-data")

    def test_07_invalid_credentials_and_invalid_jwt_rejected(self):
        print_edu_case(
            "CTM Live Test 07: Authentication & Bearer Token Enforcement",
            "An attacker with network reachability to the KMS API might attempt unauthenticated or forged-token unwrap requests.",
            "Sending wrong password to /api/v1/auth/tokens and a forged JWT to /api/v1/vault/keys2 (expecting HTTP 401).",
            "Strict JWT authentication ensures only verified workloads can request key metadata or DEK unwrapping.",
        )
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
        print_edu_case(
            "CTM Live Test 08: Mutual TLS (X.509 v3) Transport Enforcement",
            "Bearer tokens alone can be replayed if stolen; the KMS must also verify cryptographic machine identity at the TLS layer.",
            "Connecting to the mTLS-enforced CTM endpoint without a client certificate (expecting SSLError).",
            "Mutual TLS blocks unauthorized hosts at the TLS handshake before any HTTP/API parser or token check is reached.",
        )
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
