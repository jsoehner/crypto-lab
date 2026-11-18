"""Test suite for all Python cryptography examples with educational threat context."""

import unittest
from cryptography.exceptions import InvalidTag

from aes_gcm_example import encrypt, decrypt, generate_key
from aes_key_wrap_example import wrap, unwrap
from crypto_support import random_bytes, constant_time_equal
from ed25519_example import sign, verify
from edu_output import print_edu_case
from hashing_example import sha256
from hmac_example import compute, verify as hmac_verify
from pbkdf2_example import derive, verify as pbkdf2_verify
from private_key_serialisation_example import serialise_encrypted, load_encrypted
from rsa_oaep_pss_example import (
    encrypt as rsa_encrypt,
    decrypt as rsa_decrypt,
    sign as rsa_sign,
    verify as rsa_verify,
    generate_private_key,
)
from x25519_hkdf_example import derive_key


class TestCryptography(unittest.TestCase):
    def test_hashing(self):
        print_edu_case(
            "SHA-256 Cryptographic Digest",
            "Data could be accidentally corrupted or silently altered in storage or transit.",
            "Hashing b'test data' with SHA-256 (32-byte digest) and verifying a 1-byte change alters the digest.",
            "SHA-256 provides collision resistance and 128-bit Grover quantum resistance; broken MD5/SHA-1 allow forged collisions.",
        )
        data = b"test data"
        digest = sha256(data)
        self.assertEqual(len(digest), 32)
        self.assertNotEqual(digest, sha256(data + b" "))

    def test_hmac(self):
        print_edu_case(
            "HMAC-SHA-256 Message Authentication",
            "An attacker who knows the hash algorithm could replace both a message and its plain SHA-256 hash, or use timing differences to guess a MAC.",
            "Computing a 256-bit keyed HMAC-SHA-256 tag, verifying it in constant time, and rejecting a tampered message.",
            "A secret key prevents unauthorized tag forgery, and hmac.compare_digest prevents timing side-channel leaks.",
        )
        key = random_bytes(32)
        message = b"test message"
        tag = compute(key, message)
        self.assertTrue(hmac_verify(key, message, tag))
        self.assertFalse(hmac_verify(key, message + b"!", tag))

    def test_pbkdf2(self):
        print_edu_case(
            "PBKDF2-HMAC-SHA-256 Password Hashing",
            "Stolen password databases are vulnerable to rainbow tables and fast GPU brute-force attacks.",
            "Deriving a key with a unique 128-bit random salt and 600,000 PBKDF2-HMAC-SHA-256 iterations, then testing valid vs. wrong passwords.",
            "Unique random salts defeat precomputed rainbow tables, and high iteration counts slow offline brute-force guessing.",
        )
        password = b"test password"
        stored = derive(password)
        self.assertTrue(pbkdf2_verify(password, stored))
        self.assertFalse(pbkdf2_verify(b"wrong password", stored))

    def test_aes_gcm(self):
        print_edu_case(
            "AES-256-GCM Authenticated Encryption with AAD",
            "Unauthenticated encryption (like AES-CBC without MAC) lets attackers flip bits in ciphertext or move ciphertext between contexts.",
            "Encrypting with a 256-bit key, fresh 96-bit CSPRNG nonce, and AAD; then verifying wrong AAD raises InvalidTag.",
            "AES-256-GCM provides confidentiality, integrity, and context binding (AAD) in one step, and 256-bit keys resist Grover's algorithm.",
        )
        key = generate_key()
        plaintext = b"secret message"
        aad = b"aad"
        envelope = encrypt(key, plaintext, aad)
        decrypted = decrypt(key, envelope, aad)
        self.assertEqual(plaintext, decrypted)

        with self.assertRaises(InvalidTag):
            decrypt(key, envelope, b"wrong-aad")

    def test_rsa_oaep_pss(self):
        print_edu_case(
            "RSA-3072 OAEP Encryption & PSS Signatures",
            "Legacy PKCS#1 v1.5 RSA padding is vulnerable to Bleichenbacher oracle attacks, and RSA-1024/2048 lacks sufficient classical margin.",
            "Generating an RSA-3072 keypair, encrypting with OAEP-SHA-256, signing with PSS-SHA-256, and rejecting tampered messages.",
            "OAEP and PSS add randomized provably secure padding; note that RSA remains Shor-vulnerable and should migrate to ML-KEM/ML-DSA.",
        )
        private_key = generate_private_key()
        public_key = private_key.public_key()
        message = b"rsa message"
        ciphertext = rsa_encrypt(public_key, message)
        self.assertEqual(message, rsa_decrypt(private_key, ciphertext))
        signature = rsa_sign(private_key, message)
        self.assertTrue(rsa_verify(public_key, message, signature))
        self.assertFalse(rsa_verify(public_key, b"tampered", signature))

    def test_ed25519(self):
        print_edu_case(
            "Ed25519 Digital Signatures",
            "ECDSA with poor random nonces (k-reuse) leaks the private key immediately.",
            "Signing and verifying with Ed25519 and confirming tampered payloads fail verification.",
            "Ed25519 uses deterministic nonces and constant-time curve arithmetic; migrate to ML-DSA-65 (FIPS 204) for quantum resistance.",
        )
        from cryptography.hazmat.primitives.asymmetric import ed25519
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        message = b"ed25519 message"
        signature = sign(private_key, message)
        self.assertTrue(verify(public_key, message, signature))
        self.assertFalse(verify(public_key, b"tampered", signature))

    def test_x25519_hkdf(self):
        print_edu_case(
            "X25519 Key Agreement + HKDF-SHA-256",
            "Two parties need a shared symmetric key over an untrusted network without sending secrets in plaintext.",
            "Performing X25519 Diffie-Hellman between Alice and Bob and stretching the secret through HKDF-SHA-256 with salt and info.",
            "HKDF extracts uniform entropy from the raw ECDH secret and binds session context; migrate to Hybrid X25519+ML-KEM-768 for PQC.",
        )
        from cryptography.hazmat.primitives.asymmetric import x25519
        alice = x25519.X25519PrivateKey.generate()
        bob = x25519.X25519PrivateKey.generate()
        salt = random_bytes(16)
        info = b"info"
        alice_key = derive_key(alice, bob.public_key(), salt, info)
        bob_key = derive_key(bob, alice.public_key(), salt, info)
        self.assertTrue(constant_time_equal(alice_key, bob_key))

    def test_aes_key_wrap(self):
        print_edu_case(
            "AES Key Wrap (RFC 3394)",
            "Storing or transporting raw symmetric keys with ad-hoc XOR or ECB leaks key structure and lacks integrity.",
            "Wrapping and unwrapping a 256-bit content key under a 256-bit Key Encryption Key (KEK) using RFC 3394.",
            "AES-KW provides deterministic, integrity-checked key wrapping standardized for KMS and HSM key transport.",
        )
        kek = random_bytes(32)
        content_key = random_bytes(32)
        wrapped = wrap(kek, content_key)
        recovered = unwrap(kek, wrapped)
        self.assertTrue(constant_time_equal(content_key, recovered))

    def test_private_key_serialisation(self):
        print_edu_case(
            "Encrypted PKCS#8 Private Key Serialization",
            "Saving private keys as unencrypted PEM files exposes identity/signing keys to anyone with disk or backup read access.",
            "Serializing an Ed25519 private key into passphrase-encrypted PKCS#8 PEM, reloading it, and verifying wrong passphrases fail.",
            "PKCS#8 BestAvailableEncryption protects keys at rest with strong KDF + authenticated encryption.",
        )
        from cryptography.hazmat.primitives.asymmetric import ed25519
        key = ed25519.Ed25519PrivateKey.generate()
        password = b"strong-passphrase"
        pem = serialise_encrypted(key, password)
        loaded = load_encrypted(pem, password)
        self.assertEqual(key.public_key().public_bytes_raw(), loaded.public_key().public_bytes_raw())
        with self.assertRaises(ValueError):
            load_encrypted(pem, b"wrong-passphrase")


if __name__ == "__main__":
    unittest.main()
