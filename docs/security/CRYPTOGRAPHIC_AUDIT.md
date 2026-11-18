## 🛡️ Cryptographic Bill of Materials (CBOM) & PQC Migration Assessment

**Format**: CycloneDX (v1.6) | **First-Party Code Crypto Assets**: 54 | **Total Tracked Crypto Assets**: 56

### 📊 Post-Quantum Migration Scorecard

| Metric | Count | Migration Status |
|---|---|---|
| **Post-Quantum Ready (PQC)** | **0** | 🟢 Quantum-Resistant (NIST FIPS 203/204/205) |
| **Quantum-Vulnerable (Backlog)** | **37** | 🔴 At Risk of 'Harvest Now, Decrypt Later' |
| **Classical Symmetric / Digest** | **19** | 🟡 Classical Security (Requires AES-256 / SHA-256+) |
| **Asymmetric PQC Migration Progress** | **0.0%** | (0 of 37 asymmetric/vulnerable primitives migrated) |

### 🎯 Cryptographic Supply Chain Coverage & Confidence

| Evaluation Layer | Coverage / Status | Audit Confidence Assessment |
|---|---|---|
| **First-Party Code (`src/`, `scripts/`)** | **100% Audited** (54 Crypto Primitive(s) Inventoried across Java (40), PowerShell (5), Python (64)) | 🟢 **HIGH** (Direct AST & SAST verified) |
| **Third-Party Supply Chain** | **100.0%** (11 of 11 dependencies cataloged) | 🟢 HIGH (Known profiles assimilated) |
| **Overall Audit Confidence Score** | **100.0%** | 🟢 HIGH (0 unassimilated supply chain dependencies) |

| **System OS Inventory** | **Pending Update** | 🟡 **Warning** (Local OS crypto components not yet inventoried) |

### ✅ Post-Quantum Ready Assets

> ⚠️ **No Post-Quantum Ready assets detected.** Immediate migration planning recommended for asymmetric key exchanges and digital signatures.

### ⚠️ Quantum-Vulnerable Assets & Remediation Plan

| Component / Algorithm | Type / Primitive | Key Length / Curve | Recommended Target | Provenance / Context |
|---|---|---|---|---|
| **`password@be2c7461-07d0-44dd-961e-4589753184a1`**<br><sub>password@be2c7461-07d0-44dd-961e-4589753184a1</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`RSA-OAEP`**<br><sub>RSA-OAEP</sub> | algorithm / pke | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`RSA-PSS`**<br><sub>RSA-PSS</sub> | algorithm / signature | N/A | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@49a8257e-8c28-4bbb-a574-8bc748e528f3`**<br><sub>secret-key@49a8257e-8c28-4bbb-a574-8bc748e528f3</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| **`key@6ca63aca-2df2-4a43-add2-679430a398b9`**<br><sub>key@6ca63aca-2df2-4a43-add2-679430a398b9</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@850650bb-69dd-4f27-aed9-3e613de63300`**<br><sub>secret-key@850650bb-69dd-4f27-aed9-3e613de63300</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`password@a1d0cea6-8132-40b4-81dd-de43b47ad3de`**<br><sub>password@a1d0cea6-8132-40b4-81dd-de43b47ad3de</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@c47d2074-3330-4deb-afaf-89b22e937822`**<br><sub>password@c47d2074-3330-4deb-afaf-89b22e937822</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`key@86010864-3401-4ced-a826-52e312a82330`**<br><sub>key@86010864-3401-4ced-a826-52e312a82330</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`secret-key@08fc815e-8823-4c2c-bbcd-0d9bd98690f9`**<br><sub>secret-key@08fc815e-8823-4c2c-bbcd-0d9bd98690f9</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HmacExample.java` |
| **`secret-key@38b966d8-bd24-4f01-a442-8a9f0855caf3`**<br><sub>secret-key@38b966d8-bd24-4f01-a442-8a9f0855caf3</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`secret-key@cfc412b2-3585-4c9b-a181-7da2e215a140`**<br><sub>secret-key@cfc412b2-3585-4c9b-a181-7da2e215a140</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`key@998cdbbd-21a0-4d1e-b0e4-df03e2de9f4b`**<br><sub>key@998cdbbd-21a0-4d1e-b0e4-df03e2de9f4b</sub> | related-crypto-material / secret-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`salt@52161419-3d80-46fa-bb6e-9839fb2ce358`**<br><sub>salt@52161419-3d80-46fa-bb6e-9839fb2ce358</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@c5ae6ffa-bee3-4130-b003-992f8ece6291`**<br><sub>password@c5ae6ffa-bee3-4130-b003-992f8ece6291</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@50a8c1c8-9e3f-4700-9c34-fc08e1a7ae63`**<br><sub>password@50a8c1c8-9e3f-4700-9c34-fc08e1a7ae63</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@5151a23f-1a72-440b-b6bb-99d51c78d269`**<br><sub>secret-key@5151a23f-1a72-440b-b6bb-99d51c78d269</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`salt@03a454b4-2fd2-430e-b0ad-64e68752bca3`**<br><sub>salt@03a454b4-2fd2-430e-b0ad-64e68752bca3</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@cbb2985f-cf77-44e1-8893-a9c4179e9fcc`**<br><sub>password@cbb2985f-cf77-44e1-8893-a9c4179e9fcc</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@353db4bc-c50b-47df-a89e-eb285b6775cf`**<br><sub>password@353db4bc-c50b-47df-a89e-eb285b6775cf</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@3ecec842-f886-4b61-829e-0b2dd05e9027`**<br><sub>password@3ecec842-f886-4b61-829e-0b2dd05e9027</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@bf40daac-a70e-4fb9-8c16-40c38b8751e1`**<br><sub>password@bf40daac-a70e-4fb9-8c16-40c38b8751e1</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`secret-key@511e97ea-ea03-4c1c-ab98-73f0f0a7fcbf`**<br><sub>secret-key@511e97ea-ea03-4c1c-ab98-73f0f0a7fcbf</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`private-key@af1d9e48-6f12-48c0-8370-2dfb7def9d18`**<br><sub>private-key@af1d9e48-6f12-48c0-8370-2dfb7def9d18</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/ed25519_example.py` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py`<br><br>`python/rsa_oaep_pss_example.py:9`<br><sub><code>return rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/rsa_oaep_pss_example.py:1`<br><sub><code>"""RSA-3072 OAEP encryption and RSA-PSS signatures using SHA-256."""</code></sub> |
| **`private-key@da4b3dff-1d58-4eb3-983d-84330f613ac4`**<br><sub>private-key@da4b3dff-1d58-4eb3-983d-84330f613ac4</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py` |
| **`secret-key@3e30b15f-a878-4361-af7a-fea591e33932`**<br><sub>secret-key@3e30b15f-a878-4361-af7a-fea591e33932</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py` |
| **`private-key@cdfe8925-4672-4b88-81bd-8da8e85bd263`**<br><sub>private-key@cdfe8925-4672-4b88-81bd-8da8e85bd263</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/private_key_serialisation_example.py` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`python/ed25519_example.py`<br><br>`python/test_crypto.py`<br><br>`python/private_key_serialisation_example.py`<br><br>`python/run_all.py:5`<br><sub><code>from ed25519_example import main as ed25519</code></sub><br><br>`python/ed25519_example.py:1`<br><sub><code>"""Ed25519 signing and verification."""</code></sub><br><br>`python/ed25519_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/ed25519_example.py:7`<br><sub><code>def sign(private_key: ed25519.Ed25519PrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/ed25519_example.py:11`<br><sub><code>def verify(public_key: ed25519.Ed25519PublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/ed25519_example.py:20`<br><sub><code>private_key = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`python/private_key_serialisation_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:7`<br><sub><code>def serialise_encrypted(private_key: ed25519.Ed25519PrivateKey, password: bytes) -> bytes:</code></sub><br><br>`python/private_key_serialisation_example.py:15`<br><sub><code>def load_encrypted(pem: bytes, password: bytes) -> ed25519.Ed25519PrivateKey:</code></sub><br><br>`python/private_key_serialisation_example.py:17`<br><sub><code>if not isinstance(key, ed25519.Ed25519PrivateKey):</code></sub><br><br>`python/private_key_serialisation_example.py:24`<br><sub><code>original = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:10`<br><sub><code>return KeyPairGenerator.getInstance("Ed25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:14`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:21`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:31`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "Ed25519 failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:43`<br><sub><code>byte[] edMsg = "ed25519 message".getBytes(StandardCharsets.UTF_8);</code></sub> |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py`<br><br>`python/x25519_hkdf_example.py`<br><br>`python/test_crypto.py`<br><br>`python/test_crypto.py` |
| **`private-key@850a1d76-9d44-4f4e-a1b4-f7d49d9b447e`**<br><sub>private-key@850a1d76-9d44-4f4e-a1b4-f7d49d9b447e</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/test_crypto.py` |
| **`RSA-2048`**<br><sub>RSA-2048</sub> | algorithm / signature | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/run_all.py:10`<br><sub><code>from rsa_oaep_pss_example import main as rsa</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/rsa_oaep_pss_example.py:5`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/rsa_oaep_pss_example.py:8`<br><sub><code>def generate_private_key() -> rsa.RSAPrivateKey:</code></sub><br><br>`python/rsa_oaep_pss_example.py:27`<br><sub><code>def encrypt(public_key: rsa.RSAPublicKey, plaintext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:31`<br><sub><code>def decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:35`<br><sub><code>def sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:39`<br><sub><code>def verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:16`<br><sub><code>KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:26`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:32`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:61`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:63`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "RSA-PSS failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:35`<br><sub><code>byte[] rsaMsg = "rsa message".getBytes(StandardCharsets.UTF_8);</code></sub> |
| **`ECDH-X25519`**<br><sub>ECDH-X25519</sub> | algorithm / key-agreement | 25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/run_all.py:11`<br><sub><code>from x25519_hkdf_example import main as x25519</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/x25519_hkdf_example.py:1`<br><sub><code>"""X25519 key agreement followed by HKDF-SHA-256 key derivation."""</code></sub><br><br>`python/x25519_hkdf_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import x25519</code></sub><br><br>`python/x25519_hkdf_example.py:10`<br><sub><code>def derive_key(private_key: x25519.X25519PrivateKey,</code></sub><br><br>`python/x25519_hkdf_example.py:11`<br><sub><code>peer_public_key: x25519.X25519PublicKey,</code></sub><br><br>`python/x25519_hkdf_example.py:24`<br><sub><code>alice = x25519.X25519PrivateKey.generate()</code></sub><br><br>`python/x25519_hkdf_example.py:25`<br><sub><code>bob = x25519.X25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:17`<br><sub><code>return KeyPairGenerator.getInstance("X25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:21`<br><sub><code>KeyAgreement agreement = KeyAgreement.getInstance("X25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:30`<br><sub><code>throw new IllegalArgumentException("IKM must be 32 bytes for X25519.");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:60`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceSecret, bobSecret), "X25519 mismatch");</code></sub> |
| **`cryptography (PyCA OpenSSL Asymmetric Primitives (RSA / ECDSA / Ed25519 / X25519))`**<br><sub>RSA-2048 / ECDSA-P256 / Ed25519 / X25519</sub> | signature / signature | 2048 / 256 | **Migrate asymmetric PKI/JWT workflows to OpenSSL 3.5+ ML-KEM (FIPS 203) and ML-DSA (FIPS 204)** | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@42.0.0` |

### 🔒 Classical Symmetric & Digest Assets

| Component Name | Primitive | Key Length | Quantum Resistance Assessment | Provenance / Location(s) |
|---|---|---|---|---|
| `AES-128` | other | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| `PBKDF2-HMAC-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-128-GCM` | ae | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| `MGF1` | other | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-256` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HashingExample.java`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| `AES-256-GCM` | ae | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py`<br>`python/run_all.py:3`<br>`python/run_all.py:15`<br>`python/x25519_hkdf_example.py:27`<br>`python/aes_key_wrap_example.py:1`<br>`python/aes_gcm_example.py:1`<br>`python/aes_gcm_example.py:5`<br>`python/aes_gcm_example.py:17`<br>`python/aes_gcm_example.py:22`<br>`python/aes_gcm_example.py:26`<br>`powershell/AesGcmExample.ps1:3`<br>`powershell/AesGcmExample.ps1:8`<br>`powershell/AesGcmExample.ps1:12`<br>`powershell/AesGcmExample.ps1:24`<br>`powershell/AesGcmExample.ps1:32`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:62`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:21`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:28`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:38`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:49`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:13`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:27`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:35` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`python/hmac_example.py`<br>`python/hmac_example.py` |
| `AES-128` | other | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`python/aes_key_wrap_example.py` |
| `HKDF-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py` |
| `PBKDF2-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/pbkdf2_example.py` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/hmac_example.py`<br>`python/hmac_example.py`<br>`python/x25519_hkdf_example.py`<br>`python/hashing_example.py`<br>`python/pbkdf2_example.py`<br>`python/hmac_example.py:1`<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`python/rsa_oaep_pss_example.py:1`<br>`python/rsa_oaep_pss_example.py:14`<br>`python/rsa_oaep_pss_example.py:15`<br>`python/rsa_oaep_pss_example.py:22`<br>`python/rsa_oaep_pss_example.py:23`<br>`python/rsa_oaep_pss_example.py:36`<br>`python/rsa_oaep_pss_example.py:41`<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:16`<br>`python/hashing_example.py:1`<br>`python/hashing_example.py:6`<br>`python/hashing_example.py:7`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:22`<br>`java/src/main/java/org/example/crypto/HashingExample.java:9`<br>`java/src/main/java/org/example/crypto/HashingExample.java:10`<br>`java/src/main/java/org/example/crypto/HashingExample.java:14`<br>`java/src/main/java/org/example/crypto/HashingExample.java:15`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:22`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:38`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:10` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/ed25519_example.py`<br>`python/test_crypto.py`<br>`python/private_key_serialisation_example.py` |
| `PBKDF2-HMAC-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/run_all.py:8`<br>`python/run_all.py:15`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:6`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:25`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:36`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:49` |
| `HMAC-SHA256` | mac | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:34`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:35`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:41`<br>`java/src/main/java/org/example/crypto/HmacExample.java:11`<br>`java/src/main/java/org/example/crypto/HmacExample.java:12` |
| `HKDF-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:5`<br>`python/x25519_hkdf_example.py:15`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:32`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:65` |
| `cryptography (PyCA OpenSSL EVP Symmetric & AEAD Suite (AES-256-GCM / ChaCha20-Poly1305 / Fernet))` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@42.0.0` |

### ⚛️ Post-Quantum Cryptography (PQC) Modernization Roadmap

NIST finalized the principal post-quantum cryptography standards in August 2024: **FIPS 203** (ML-KEM), **FIPS 204** (ML-DSA), and **FIPS 205** (SLH-DSA). Below is the recommended migration path for replacing quantum-vulnerable public key algorithms and hardening symmetric ciphers against Grover's algorithm.

#### 🗺️ Cryptographic Algorithm Replacement Matrix

| Classical Primitive | Threat Mechanism | Post-Quantum Replacement | NIST Security Level | Migration Guidance |
|---|---|---|---|---|
| **RSA / Diffie-Hellman / ECDH / X25519** (Key Exchange / KEM) | Broken by Shor's algorithm | **ML-KEM-768 / ML-KEM-1024** (FIPS 203) or Hybrid **X25519MLKEM768** | Level 3 (AES-192 equiv) / Level 5 (AES-256 equiv) | Primary general-purpose key encapsulation. For TLS 1.3 and SSH, deploy hybrid `X25519MLKEM768` for seamless interoperability. |
| **RSA-PSS / ECDSA / Ed25519** (Digital Signatures) | Broken by Shor's algorithm | **ML-DSA-65 / ML-DSA-87** (FIPS 204) | Level 3 / Level 5 | Primary general-purpose lattice signatures for PKI, X.509 certs, code signing, and API tokens. |
| **High-Assurance Root / CA Signatures** | Broken by Shor's algorithm | **SLH-DSA** (FIPS 205 / SPHINCS+) | Level 1, 3, 5 | Stateless hash-based signatures with zero lattice assumptions; ideal for long-lived root trust stores. |
| **Firmware / Secure Boot Signing** | Broken by Shor's algorithm | **LMS / XMSS** (RFC 8554 / RFC 8391, NIST SP 800-208) | Level 3 / Level 5 | Stateful hash-based signatures with minimal memory/code overhead; optimal for microcontrollers. |
| **AES-128 (Symmetric Encryption)** | Halved by Grover's (effective 64-bit security) | **AES-256-GCM** or **ChaCha20-Poly1305** | Level 5 (effective 128-bit quantum security) | Upgrade symmetric key lengths from 128-bit to 256-bit to preserve Grover resistance. |
| **SHA-1 / MD5 (Hash Functions)** | Broken classical collisions + quantum Grover | **SHA-256 / SHA-384 / SHA-512 / SHA-3-256** | Level 3 - 5 | Deprecate weak digests immediately. Use SHA-256 or SHA-3-256 as quantum-safe baseline. |

#### 💻 Multi-Language PQC Implementation Recipes

<details>
<summary><b>Swift (iOS, macOS, Server-side Swift)</b></summary>

```swift
import CryptoKit
// 1. Symmetric Grover resistance (use 256-bit keys)
let symmetricKey = SymmetricKey(size: .bits256)
let sealedBox = try AES.GCM.seal(data, using: symmetricKey)

// 2. Post-Quantum KEM via SwiftCrypto / liboqs-swift:
#if canImport(OQS)
import OQS
let kem = OQSKEM(algorithm: .mlkem768)
let (publicKey, secretKey) = try kem.generateKeyPair()
let (ciphertext, sharedSecretSender) = try kem.encapsulate(publicKey: publicKey)
let sharedSecretReceiver = try kem.decapsulate(ciphertext: ciphertext, secretKey: secretKey)
#endif
```
</details>

<details>
<summary><b>Go (Go 1.24+ crypto/mlkem & Hybrid TLS)</b></summary>

```go
package main

import (
    "crypto/mlkem" // Standard library in Go 1.24+
    "crypto/tls"
)

func main() {
    // 1. FIPS 203 ML-KEM-768 Key Encapsulation
    decapsKey, _ := mlkem.GenerateKey768()
    encapsKey := decapsKey.EncapsulationKey()
    ciphertext, sharedSecretClient := encapsKey.Encapsulate()
    sharedSecretServer, _ := decapsKey.Decapsulate(ciphertext)
    _ = sharedSecretServer

    // 2. Hybrid Post-Quantum TLS 1.3 Client
    tlsConfig := &tls.Config{
        MinVersion:       tls.VersionTLS13,
        CurvePreferences: []tls.CurveID{tls.X25519MLKEM768, tls.X25519},
    }
    _ = tlsConfig
}
```
</details>

<details>
<summary><b>Python (cryptography 44.0+ & liboqs-python)</b></summary>

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. Grover-resistant 256-bit symmetric AEAD
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# 2. FIPS 203 ML-KEM-768 via liboqs-python
import oqs
with oqs.KeyEncapsulation('ML-KEM-768') as kem:
    public_key = kem.generate_keypair()
    ciphertext, shared_secret_sender = kem.encap_secret(public_key)
    shared_secret_receiver = kem.decap_secret(ciphertext)
    assert shared_secret_sender == shared_secret_receiver
```
</details>

<details>
<summary><b>Rust (pqcrypto / aws-lc-rs)</b></summary>

```rust
use pqcrypto_kyber::kyber768; // FIPS 203 ML-KEM-768
use pqcrypto_traits::kem::{PublicKey, SecretKey, SharedSecret};

fn main() {
    let (pk, sk) = kyber768::keypair();
    let (ss_sender, ct) = kyber768::encapsulate(&pk);
    let ss_receiver = kyber768::decapsulate(&ct, &sk);
    assert_eq!(ss_sender.as_bytes(), ss_receiver.as_bytes());
}
```
</details>

<details>
<summary><b>Java / Kotlin (Bouncy Castle 1.78+)</b></summary>

```java
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.MLKEMParameterSpec;
import java.security.*;

Security.addProvider(new BouncyCastlePQCProvider());
KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM", "BCPQC");
kpg.initialize(MLKEMParameterSpec.ml_kem_768);
KeyPair kp = kpg.generateKeyPair();
```
</details>

<details>
<summary><b>TypeScript / Node.js</b></summary>

```typescript
import { mlkem768 } from '@noble/post-quantum/ml-kem';

const [aliceKeys, alicePub] = mlkem768.keygen();
const [ciphertext, sharedBob] = mlkem768.encapsulate(alicePub);
const sharedAlice = mlkem768.decapsulate(ciphertext, aliceKeys);
```
</details>

### 🌐 Open Source CBOM Intelligence & Supply Chain Attestation Locators

Third-party dependencies account for the vast majority of cryptographic attack surfaces. When upstream packages do not ship with explicit CBOM files, use the following sources and methods to uncover cryptographic metadata:

1. **OCI 1.1 / Sigstore Cosign Attestations (`application/vnd.cyclonedx+json`)**:
   - Many open-source container images and libraries attach CycloneDX CBOM attestations via Sigstore Cosign.
   - Query attestations using Cosign:
     ```bash
     cosign download attestation --predicate-type https://cyclonedx.org/bom ghcr.io/<org>/<image>:<tag> | jq -r .payload | base64 -d | jq .
     ```
2. **OpenSSF Security Insights (`SECURITY-INSIGHTS.yml`)**:
   - Repositories implementing OpenSSF Security Insights declare encryption standards and key management under `/.github/SECURITY-INSIGHTS.yml`.
3. **Package Registry Provenance & Hash Attestations**:
   - **PyPI (PEP 740)**: Inspect cryptographic provenance via `https://pypi.org/pypi/<package>/json`.
   - **npm Provenance**: Verify build provenance and sign-offs with `npm view <package> --json`.
   - **Swift Package Index**: Discover cryptography framework dependencies directly from SwiftPM manifests and DocC documentation.
4. **Direct Assimilation with `--external-cbom`**:
   - Ingest any vendor or upstream CycloneDX CBOM file directly into `jsi-bom-actions`:
     ```bash
     python scripts/analyze_cbom.py build/cbom.cyclonedx.json --sbom build/sbom.cyclonedx.json --external-cbom vendor.cbom.json
     ```
   - This directly credits verified dependencies and elevates the repository's **Audit Confidence Score**.
