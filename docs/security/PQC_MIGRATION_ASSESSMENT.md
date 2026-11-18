# Post-Quantum Cryptography (PQC) Migration Assessment

**Date:** 2026-11-18 | **Version:** `1.2.0` | **CBOM Scanner:** `scripts/scan_crypto_ast.py` + `scripts/analyze_cbom.py`

## Executive Summary

A full AST and CBOM audit of this repository identified **185 cryptographic call sites** across **10 distinct cryptographic assets** in Python, Java 25, JavaScript (Node.js 22), and PowerShell.

- **Symmetric & Digest Primitives (Grover-Resistant):** `AES-256-GCM`, `SHA-256`, `HMAC-SHA-256`, `HKDF-SHA-256`, and `PBKDF2-HMAC-SHA-256` already provide 128-bit+ post-quantum security when configured with 256-bit keys and 256-bit+ digests.
- **Asymmetric Primitives (Shor-Vulnerable -> PQC Equivalents):** Every classical asymmetric function in this repository (`X25519`, `RSA-OAEP`, `RSA-PSS`, `Ed25519`) now has a side-by-side quantum-resistant equivalent implemented and tested in Java 25 and JavaScript (Node.js 22):
  - **ML-KEM-768** (NIST FIPS 203)
  - **Hybrid X25519 + ML-KEM-768** (transition key establishment)
  - **ML-DSA-65** (NIST FIPS 204)
  - **SLH-DSA-SHA2-128f** (NIST FIPS 205)

## Function-by-Function Migration Matrix

| Classical Function | Classical Reference | Quantum Threat | PQC / Quantum-Resistant Equivalent | PQC Reference Implementation |
|---|---|---|---|---|
| **Key Agreement** (`X25519 + HKDF-SHA-256`) | `X25519HkdfExample.java`, `x25519_hkdf_example.py` | Shor's algorithm (Harvest Now, Decrypt Later) | **Hybrid X25519 + ML-KEM-768 + HKDF-SHA-256** or **ML-KEM-768** | [HybridX25519MlKemExample.java](../../java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java), [hybrid_kem_example.js](../../javascript/src/hybrid_kem_example.js) |
| **Public-Key Encryption** (`RSA-3072 OAEP`) | `RsaOaepPssExample.java`, `rsa_oaep_pss_example.py` | Shor's algorithm | **ML-KEM-768 + HKDF-SHA-256 + AES-256-GCM (KEM-DEM)** | [MlKemExample.java](../../java/src/main/java/org/example/crypto/MlKemExample.java), [ml_kem_example.js](../../javascript/src/ml_kem_example.js) |
| **General Digital Signatures** (`Ed25519`, `RSA-PSS`) | `Ed25519Example.java`, `RsaOaepPssExample.java`, `ed25519_example.py`, `rsa_oaep_pss_example.py` | Shor's algorithm | **ML-DSA-65** (NIST FIPS 204) | [MlDsaExample.java](../../java/src/main/java/org/example/crypto/MlDsaExample.java), [ml_dsa_example.js](../../javascript/src/ml_dsa_example.js) |
| **Root CA / Code Signing** (`RSA-3072`, `Ed25519`) | `Ed25519Example.java`, `RsaOaepPssExample.java` | Shor's algorithm | **SLH-DSA-SHA2-128f** (NIST FIPS 205, stateless hash-based) | [slh_dsa_example.js](../../javascript/src/slh_dsa_example.js) |
| **Authenticated Encryption** (`AES-256-GCM`) | `AesGcmExample.java`, `aes_gcm_example.py`, `aes_gcm_example.js`, `AesGcmExample.ps1` | Grover's algorithm (halves key strength) | **Retain AES-256-GCM** (256-bit key = 128-bit quantum security) | Already quantum-resistant |
| **Hashing & MAC** (`SHA-256`, `HMAC-SHA-256`) | `HashingExample.java`, `HmacExample.java`, `hashing_example.py`, `hmac_example.py`, `hashing.js`, `hmac_example.js` | Grover's algorithm | **Retain SHA-256 / HMAC-SHA-256** (upgrade any AES-128 KEKs to AES-256) | Already quantum-resistant |

## CBOM Scorecard (Post-Addition)

- **First-Party Code Crypto Assets:** 10 (185 AST call sites)
- **Post-Quantum Ready (PQC):** 3 (`ML-KEM-768`, `ML-DSA-65`, `SLH-DSA`) — **42.9%** of tracked asymmetric primitives
- **Classical Symmetric / Digest:** 3 (`AES-256-GCM`, `SHA-256`, `HMAC-SHA-256`)
- **Quantum-Vulnerable (Retained for Side-by-Side Comparison):** 4 (`Ed25519`, `RSA-2048`, `RSA-3072`, `ECDH-X25519`)

## Guidance for Development Teams

1. **Do not wait for a "big-bang" cutover:** Adopt **Hybrid X25519 + ML-KEM-768** first for TLS/API key establishment so classical and post-quantum security both apply.
2. **Replace RSA-OAEP encryption with KEM-DEM:** Use `ML-KEM-768` to encapsulate a shared secret, derive a 256-bit key with `HKDF-SHA-256`, and encrypt payloads with `AES-256-GCM`.
3. **Budget for larger PQC artifacts:** `ML-KEM-768` ciphertexts are `1,088` bytes, `ML-DSA-65` signatures are `3,309` bytes, and `SLH-DSA-SHA2-128f` signatures are `17,088` bytes.
4. **Python Ecosystem Note:** As of `cryptography==50.0.0`, PyCA `cryptography` does not expose `ML-KEM` or `ML-DSA` in `hazmat.primitives.asymmetric`; use Java 25+ or Node.js (`@noble/post-quantum`) for native/pure-JS FIPS 203–205 workloads, or `liboqs-python` where C/OpenSSL bindings are permitted.
