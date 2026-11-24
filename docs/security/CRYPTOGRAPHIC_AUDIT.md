## 🛡️ Cryptographic Bill of Materials (CBOM) & PQC Migration Assessment

**Format**: CycloneDX (v1.6) | **First-Party Code Crypto Assets**: 54 | **Total Tracked Crypto Assets**: 59

### 📊 Post-Quantum Migration Scorecard

| Metric | Count | Migration Status |
|---|---|---|
| **Post-Quantum Ready (PQC)** | **5** | 🟢 Quantum-Resistant (NIST FIPS 203/204/205) |
| **Quantum-Vulnerable (Backlog)** | **39** | 🔴 At Risk of 'Harvest Now, Decrypt Later' |
| **Classical Symmetric / Digest** | **15** | 🟡 Classical Security (Requires AES-256 / SHA-256+) |
| **Asymmetric PQC Migration Progress** | **11.4%** | (5 of 44 asymmetric/vulnerable primitives migrated) |

### 🎯 Cryptographic Supply Chain Coverage & Confidence

| Evaluation Layer | Coverage / Status | Audit Confidence Assessment |
|---|---|---|
| **First-Party Code (`src/`, `scripts/`)** | **100% Audited** (54 Crypto Primitive(s) Inventoried across Java (91), JavaScript (48), PowerShell (10), Python (120), Shell (16)) | 🟢 **HIGH** (Direct AST & SAST verified) |
| **Third-Party Supply Chain** | **94.7%** (18 of 19 dependencies cataloged) | 🟢 HIGH (Known profiles assimilated) |
| **Overall Audit Confidence Score** | **95.0%** | 🟢 HIGH (1 unassimilated supply chain dependencies) |

| **System OS Inventory** | **Pending Update** | 🟡 **Warning** (Local OS crypto components not yet inventoried) |

### ✅ Post-Quantum Ready Assets

| Component Name | Primitive | Key/Parameter Set | PQC Standard | Provenance / Location(s) |
|---|---|---|---|---|
| `ML-DSA-65` | signature | 65 | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`demo_langs.ps1:42`<br>`demo_langs.ps1:51`<br>`demo_langs.sh:131`<br>`demo_langs.sh:132`<br>`demo_langs.sh:144`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:113`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:116`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:19`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:20`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:25`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:32`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:42`<br>`javascript/src/run_all.js:69`<br>`javascript/src/ml_dsa_example.js:2`<br>`javascript/src/ml_dsa_example.js:10`<br>`javascript/src/ml_dsa_example.js:20`<br>`javascript/src/ml_dsa_example.js:31` |
| `ML-KEM-768` | kem | 768 | ML-KEM (FIPS 203) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`demo_langs.ps1:42`<br>`demo_langs.ps1:51`<br>`demo_langs.sh:131`<br>`demo_langs.sh:132`<br>`demo_langs.sh:144`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:84`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:86`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:90`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:20`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:21`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:26`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:32`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:72`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br>`javascript/src/run_all.js:55`<br>`javascript/src/run_all.js:60`<br>`javascript/src/run_all.js:86`<br>`javascript/src/ml_kem_example.js:2`<br>`javascript/src/ml_kem_example.js:11`<br>`javascript/src/ml_kem_example.js:20`<br>`javascript/src/ml_kem_example.js:30`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/hybrid_kem_example.js:2`<br>`javascript/src/hybrid_kem_example.js:33`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:49`<br>`javascript/src/hybrid_kem_example.js:50` |
| `SLH-DSA` | signature | 128s/256f | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`demo_langs.sh:145`<br>`javascript/src/run_all.js:94`<br>`javascript/src/slh_dsa_example.js:2`<br>`javascript/src/slh_dsa_example.js:11`<br>`javascript/src/slh_dsa_example.js:21`<br>`javascript/src/slh_dsa_example.js:32` |
| `@noble/post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: @noble/post-quantum@0.4.1` |
| `post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: post-quantum@0.4.0` |

### ⚠️ Quantum-Vulnerable Assets & Remediation Plan

| Component / Algorithm | Type / Primitive | Key Length / Curve | Recommended Target | Provenance / Context |
|---|---|---|---|---|
| **`secret-key@6645825c-82db-4e0c-ad5f-36e99363a43d`**<br><sub>secret-key@6645825c-82db-4e0c-ad5f-36e99363a43d</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`RSA-OAEP`**<br><sub>RSA-OAEP</sub> | algorithm / pke | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@92f84ed5-ffdc-4182-a1ce-f886194eb273`**<br><sub>secret-key@92f84ed5-ffdc-4182-a1ce-f886194eb273</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`demo_langs.sh:111`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Running SHA-256, HMAC, PBKDF2, AES-256-GCM, RSA-3072, Ed25519, X25519+HKDF, AES-KW, and</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:46`<br><sub><code>self._import_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:47`<br><sub><code>self._kek_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/rsa_oaep_pss_example.py:9`<br><sub><code>return rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/rsa_oaep_pss_example.py:1`<br><sub><code>"""RSA-3072 OAEP encryption and RSA-PSS signatures using SHA-256."""</code></sub> |
| **`password@cd5c682a-8a9e-4d68-b5ac-60cea11f3810`**<br><sub>password@cd5c682a-8a9e-4d68-b5ac-60cea11f3810</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`key@44f8f086-d8b2-472e-a7b1-87719812c3f8`**<br><sub>key@44f8f086-d8b2-472e-a7b1-87719812c3f8</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`RSA-PSS`**<br><sub>RSA-PSS</sub> | algorithm / signature | N/A | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@7f4a5519-0dd8-4d1d-bb96-4ddaa4bb3786`**<br><sub>password@7f4a5519-0dd8-4d1d-bb96-4ddaa4bb3786</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`key@40f5c8a7-26fe-42b4-90c7-b95b3169b50c`**<br><sub>key@40f5c8a7-26fe-42b4-90c7-b95b3169b50c</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@4868d07f-ca1e-4407-96cf-cbc8f1d69fad`**<br><sub>secret-key@4868d07f-ca1e-4407-96cf-cbc8f1d69fad</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`secret-key@1f64c78c-59af-4dd3-8d1c-7c0c755e6589`**<br><sub>secret-key@1f64c78c-59af-4dd3-8d1c-7c0c755e6589</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@06eef425-fc55-48e8-91ff-489e6ae13c12`**<br><sub>secret-key@06eef425-fc55-48e8-91ff-489e6ae13c12</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`secret-key@b8cfe775-1649-4f44-8e33-95626f60d47e`**<br><sub>secret-key@b8cfe775-1649-4f44-8e33-95626f60d47e</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@cec785aa-ab53-4598-8b8f-7c6a8e610762`**<br><sub>secret-key@cec785aa-ab53-4598-8b8f-7c6a8e610762</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:57`<br><sub><code>byte[] edMsg = "ed25519 message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:59`<br><sub><code>CryptoSupport.require(Ed25519Example.verify(edKeys.getPublic(), edMsg, edSig), "Ed25519 verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:60`<br><sub><code>CryptoSupport.require(!Ed25519Example.verify(edKeys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), edSig), "E</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:10`<br><sub><code>return KeyPairGenerator.getInstance("Ed25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:14`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:21`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:31`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "Ed25519 failed");</code></sub><br><br>`python/ed25519_example.py:1`<br><sub><code>"""Ed25519 signing and verification."""</code></sub><br><br>`python/ed25519_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/ed25519_example.py:7`<br><sub><code>def sign(private_key: ed25519.Ed25519PrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/ed25519_example.py:11`<br><sub><code>def verify(public_key: ed25519.Ed25519PublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/ed25519_example.py:20`<br><sub><code>private_key = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`python/run_all.py:5`<br><sub><code>from ed25519_example import main as ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:7`<br><sub><code>def serialise_encrypted(private_key: ed25519.Ed25519PrivateKey, password: bytes) -> bytes:</code></sub><br><br>`python/private_key_serialisation_example.py:15`<br><sub><code>def load_encrypted(pem: bytes, password: bytes) -> ed25519.Ed25519PrivateKey:</code></sub><br><br>`python/private_key_serialisation_example.py:17`<br><sub><code>if not isinstance(key, ed25519.Ed25519PrivateKey):</code></sub><br><br>`python/private_key_serialisation_example.py:24`<br><sub><code>original = ed25519.Ed25519PrivateKey.generate()</code></sub> |
| **`salt@7c91d385-7d19-4f99-a9d3-c7f61961f6f1`**<br><sub>salt@7c91d385-7d19-4f99-a9d3-c7f61961f6f1</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@f535b203-13dd-4044-b6e0-41372dab8453`**<br><sub>secret-key@f535b203-13dd-4044-b6e0-41372dab8453</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| **`password@10cc287e-8a45-457a-a78e-b07092daf81f`**<br><sub>password@10cc287e-8a45-457a-a78e-b07092daf81f</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@c819517e-0265-4c56-8ce0-392e36f522a3`**<br><sub>secret-key@c819517e-0265-4c56-8ce0-392e36f522a3</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`secret-key@8a2b0885-d4c5-4947-be7c-87b090eba624`**<br><sub>secret-key@8a2b0885-d4c5-4947-be7c-87b090eba624</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| **`key@0f6daa71-4d5e-47fd-ba6f-dafaf6417aee`**<br><sub>key@0f6daa71-4d5e-47fd-ba6f-dafaf6417aee</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java` |
| **`salt@447ccd21-960b-4df3-8cd6-40c627ea046c`**<br><sub>salt@447ccd21-960b-4df3-8cd6-40c627ea046c</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@59813764-a373-4a35-8965-218ae0d9f4ab`**<br><sub>password@59813764-a373-4a35-8965-218ae0d9f4ab</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@49def583-2e46-4b15-8117-94dc490b761c`**<br><sub>password@49def583-2e46-4b15-8117-94dc490b761c</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@99924ddc-4f86-490a-8727-747bda44f15c`**<br><sub>password@99924ddc-4f86-490a-8727-747bda44f15c</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`key@55a8e46d-97e1-4265-a986-3a42672b112c`**<br><sub>key@55a8e46d-97e1-4265-a986-3a42672b112c</sub> | related-crypto-material / secret-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@081dba50-4f96-448c-84ca-bc374241c9b4`**<br><sub>secret-key@081dba50-4f96-448c-84ca-bc374241c9b4</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@9363fb76-85ca-4cd3-a341-9853929f3776`**<br><sub>password@9363fb76-85ca-4cd3-a341-9853929f3776</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@d70dc76c-c81f-41be-92a7-87e6b71547e5`**<br><sub>secret-key@d70dc76c-c81f-41be-92a7-87e6b71547e5</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HmacExample.java` |
| **`secret-key@218e890b-9126-46b1-b395-f47a0b919421`**<br><sub>secret-key@218e890b-9126-46b1-b395-f47a0b919421</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`password@20fd93f4-43a1-4bc4-9c0a-176fe5fcb94d`**<br><sub>password@20fd93f4-43a1-4bc4-9c0a-176fe5fcb94d</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@f8e6d270-b704-412b-a27b-0e92decffcb4`**<br><sub>password@f8e6d270-b704-412b-a27b-0e92decffcb4</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`key@281cc03d-95c8-467c-b6c8-8da8ddc75306`**<br><sub>key@281cc03d-95c8-467c-b6c8-8da8ddc75306</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`password@22e4d565-487b-46e7-b8e0-c6f9a0b5b5dc`**<br><sub>password@22e4d565-487b-46e7-b8e0-c6f9a0b5b5dc</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`ECDH-X25519`**<br><sub>ECDH-X25519</sub> | algorithm / key-agreement | 25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`demo_langs.sh:111`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Running SHA-256, HMAC, PBKDF2, AES-256-GCM, RSA-3072, Ed25519, X25519+HKDF, AES-KW, and</code></sub><br><br>`demo_langs.sh:130`<br><sub><code>echo -e "  ${MAGENTA}[PROBLEM]${NC} Quantum computers running Shor's algorithm will break RSA, X25519, and Ed25519 ('Har</code></sub><br><br>`demo_langs.sh:131`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Compiling and running Java 25 JCA/JCE examples including ML-KEM-768, Hybrid X25519+ML-K</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:17`<br><sub><code>return KeyPairGenerator.getInstance("X25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:21`<br><sub><code>KeyAgreement agreement = KeyAgreement.getInstance("X25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:30`<br><sub><code>throw new IllegalArgumentException("IKM must be 32 bytes for X25519.");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:60`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceSecret, bobSecret), "X25519 mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:69`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceKey, bobKey), "X25519-HKDF mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br><sub><code>"Hybrid X25519+ML-KEM-768 round-trip failed"</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypted), "Hybrid X25519+ML-KEM-768 round-trip failed");</code></sub><br><br>`javascript/src/run_all.js:86`<br><sub><code>throw new Error('Hybrid X25519+ML-KEM-768 round-trip failed');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:9`<br><sub><code>return generateKeyPairSync('x25519');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:35`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:50`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub><br><br>`python/x25519_hkdf_example.py:1`<br><sub><code>"""X25519 key agreement followed by HKDF-SHA-256 key derivation."""</code></sub><br><br>`python/x25519_hkdf_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import x25519</code></sub><br><br>`python/x25519_hkdf_example.py:10`<br><sub><code>def derive_key(private_key: x25519.X25519PrivateKey,</code></sub><br><br>`python/x25519_hkdf_example.py:11`<br><sub><code>peer_public_key: x25519.X25519PublicKey,</code></sub><br><br>`python/x25519_hkdf_example.py:24`<br><sub><code>alice = x25519.X25519PrivateKey.generate()</code></sub><br><br>`python/x25519_hkdf_example.py:25`<br><sub><code>bob = x25519.X25519PrivateKey.generate()</code></sub><br><br>`python/run_all.py:11`<br><sub><code>from x25519_hkdf_example import main as x25519</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub> |
| **`RSA-2048`**<br><sub>RSA-2048</sub> | algorithm / signature | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`demo_langs.sh:130`<br><sub><code>echo -e "  ${MAGENTA}[PROBLEM]${NC} Quantum computers running Shor's algorithm will break RSA, X25519, and Ed25519 ('Har</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:48`<br><sub><code>byte[] rsaMsg = "rsa message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:50`<br><sub><code>CryptoSupport.require(Arrays.equals(rsaMsg, RsaOaepPssExample.decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed"</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:52`<br><sub><code>CryptoSupport.require(RsaOaepPssExample.verify(keys.getPublic(), rsaMsg, signature), "RSA-PSS verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:53`<br><sub><code>CryptoSupport.require(!RsaOaepPssExample.verify(keys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), signature</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:16`<br><sub><code>KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:26`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:32`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:61`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:63`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "RSA-PSS failed");</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:17`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:75`<br><sub><code>def prepare_gcp_byok_blob(import_job_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:18`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:52`<br><sub><code>"""Unwrap a BYOK blob (RSA-OAEP-256 wrapped AES-KWP key) inside the HSM boundary."""</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:67`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:79`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:91`<br><sub><code>def prepare_azure_byok_blob(hsm_kek_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:120`<br><sub><code>wrapped_dek = crypto_client.wrap_key("RSA-OAEP-256", dek)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:132`<br><sub><code>dek = crypto_client.unwrap_key("RSA-OAEP-256", envelope.wrapped_dek)</code></sub><br><br>`python/rsa_oaep_pss_example.py:5`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/rsa_oaep_pss_example.py:8`<br><sub><code>def generate_private_key() -> rsa.RSAPrivateKey:</code></sub><br><br>`python/rsa_oaep_pss_example.py:27`<br><sub><code>def encrypt(public_key: rsa.RSAPublicKey, plaintext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:31`<br><sub><code>def decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:35`<br><sub><code>def sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:39`<br><sub><code>def verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/run_all.py:10`<br><sub><code>from rsa_oaep_pss_example import main as rsa</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub> |
| **`Diffie-Hellman`**<br><sub>Diffie-Hellman</sub> | algorithm / key-agreement | 2048 | **ML-KEM (KEM) or ML-DSA (Signatures)** | First-Party Code (SAST/AST)<br>`javascript/src/hybrid_kem_example.js:1`<br><sub><code>import { diffieHellman, generateKeyPairSync, hkdfSync, randomBytes } from 'node:crypto';</code></sub><br><br>`javascript/src/hybrid_kem_example.js:29`<br><sub><code>const x25519Secret = diffieHellman({</code></sub><br><br>`javascript/src/hybrid_kem_example.js:45`<br><sub><code>const x25519Secret = diffieHellman({</code></sub> |
| **`cryptography (PyCA OpenSSL Asymmetric Primitives (RSA / ECDSA / Ed25519 / X25519))`**<br><sub>RSA-2048 / ECDSA-P256 / Ed25519 / X25519</sub> | signature / signature | 2048 / 256 | **Migrate asymmetric PKI/JWT workflows to OpenSSL 3.5+ ML-KEM (FIPS 203) and ML-DSA (FIPS 204)** | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@44.0.1` |

### 🔒 Classical Symmetric & Digest Assets

| Component Name | Primitive | Key Length | Quantum Resistance Assessment | Provenance / Location(s) |
|---|---|---|---|---|
| `AES-128` | block-cipher | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `PBKDF2-HMAC-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-128-GCM` | ae | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| `MGF1` | other | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `AES-256` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HashingExample.java`<br>`demo_langs.sh:111`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:13`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:14`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:22`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:38`<br>`java/src/main/java/org/example/crypto/HashingExample.java:9`<br>`java/src/main/java/org/example/crypto/HashingExample.java:10`<br>`java/src/main/java/org/example/crypto/HashingExample.java:14`<br>`java/src/main/java/org/example/crypto/HashingExample.java:15`<br>`javascript/src/run_all.js:2`<br>`javascript/src/run_all.js:28`<br>`javascript/src/hashing.js:8`<br>`javascript/src/hashing.js:9`<br>`javascript/src/hmac_example.js:10`<br>`javascript/src/ml_kem_example.js:41`<br>`javascript/src/hybrid_kem_example.js:22`<br>`python/gcp_kms_byok_cmk_example.py:56`<br>`python/gcp_kms_byok_cmk_example.py:57`<br>`python/gcp_kms_byok_cmk_example.py:81`<br>`python/gcp_kms_byok_cmk_example.py:82`<br>`python/azure_keyvault_byok_cmk_example.py:57`<br>`python/azure_keyvault_byok_cmk_example.py:58`<br>`python/azure_keyvault_byok_cmk_example.py:72`<br>`python/azure_keyvault_byok_cmk_example.py:73`<br>`python/azure_keyvault_byok_cmk_example.py:84`<br>`python/azure_keyvault_byok_cmk_example.py:85`<br>`python/azure_keyvault_byok_cmk_example.py:97`<br>`python/azure_keyvault_byok_cmk_example.py:98`<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:16`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:22`<br>`python/rsa_oaep_pss_example.py:1`<br>`python/rsa_oaep_pss_example.py:14`<br>`python/rsa_oaep_pss_example.py:15`<br>`python/rsa_oaep_pss_example.py:22`<br>`python/rsa_oaep_pss_example.py:23`<br>`python/rsa_oaep_pss_example.py:36`<br>`python/rsa_oaep_pss_example.py:41`<br>`python/hashing_example.py:1`<br>`python/hashing_example.py:6`<br>`python/hashing_example.py:7`<br>`python/hmac_example.py:1`<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| `AES-256-GCM` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`demo_langs.ps1:60`<br>`demo_langs.sh:111`<br>`demo_langs.sh:154`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:62`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:21`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:28`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:38`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:49`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:37`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:44`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:76`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:47`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:56`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:13`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:27`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:35`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:59`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:80`<br>`javascript/src/run_all.js:46`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:50`<br>`javascript/src/aes_gcm_example.js:20`<br>`javascript/src/aes_gcm_example.js:23`<br>`javascript/src/aes_gcm_example.js:41`<br>`javascript/src/aes_gcm_example.js:43`<br>`python/gcp_kms_byok_cmk_example.py:18`<br>`python/gcp_kms_byok_cmk_example.py:67`<br>`python/gcp_kms_byok_cmk_example.py:72`<br>`python/gcp_kms_byok_cmk_example.py:104`<br>`python/gcp_kms_byok_cmk_example.py:108`<br>`python/gcp_kms_byok_cmk_example.py:119`<br>`python/azure_keyvault_byok_cmk_example.py:19`<br>`python/azure_keyvault_byok_cmk_example.py:52`<br>`python/azure_keyvault_byok_cmk_example.py:118`<br>`python/azure_keyvault_byok_cmk_example.py:122`<br>`python/azure_keyvault_byok_cmk_example.py:133`<br>`python/vault_ekm_proxy_example.py:22`<br>`python/vault_ekm_proxy_example.py:83`<br>`python/vault_ekm_proxy_example.py:92`<br>`python/vault_ekm_proxy_example.py:111`<br>`python/vault_ekm_proxy_example.py:122`<br>`python/x25519_hkdf_example.py:27`<br>`python/aes_key_wrap_example.py:1`<br>`python/ciphertrust_ekm_example.py:22`<br>`python/ciphertrust_ekm_example.py:136`<br>`python/ciphertrust_ekm_example.py:153`<br>`python/ciphertrust_ekm_example.py:194`<br>`python/ciphertrust_ekm_example.py:253`<br>`python/ciphertrust_ekm_example.py:263`<br>`python/aes_gcm_example.py:1`<br>`python/aes_gcm_example.py:5`<br>`python/aes_gcm_example.py:17`<br>`python/aes_gcm_example.py:22`<br>`python/aes_gcm_example.py:26`<br>`python/stage3_multi_cloud_ekm_orchestration.py:18`<br>`python/stage3_multi_cloud_ekm_orchestration.py:58`<br>`python/stage3_multi_cloud_ekm_orchestration.py:62`<br>`python/stage3_multi_cloud_ekm_orchestration.py:79`<br>`python/stage3_multi_cloud_ekm_orchestration.py:80`<br>`python/run_all.py:3`<br>`python/run_all.py:15`<br>`python/external_kms_ekm_example.py:20`<br>`python/external_kms_ekm_example.py:91`<br>`python/external_kms_ekm_example.py:97`<br>`python/external_kms_ekm_example.py:160`<br>`python/external_kms_ekm_example.py:173`<br>`powershell/AesGcmExample.ps1:3`<br>`powershell/AesGcmExample.ps1:8`<br>`powershell/AesGcmExample.ps1:12`<br>`powershell/AesGcmExample.ps1:24`<br>`powershell/AesGcmExample.ps1:32` |
| `PBKDF2-HMAC-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`demo_langs.sh:111`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:29`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:30`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:25`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:36`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:49`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:6`<br>`python/run_all.py:8`<br>`python/run_all.py:15` |
| `HKDF-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:32`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:65`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:69`<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:5`<br>`python/x25519_hkdf_example.py:15` |
| `HMAC-SHA256` | mac | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:34`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:35`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:41`<br>`java/src/main/java/org/example/crypto/HmacExample.java:11`<br>`java/src/main/java/org/example/crypto/HmacExample.java:12`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:25`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:27`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:30`<br>`javascript/src/hmac_example.js:10`<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16` |
| `TLS-1.3` | protocol | v1.3 | TLS 1.3 Transport (Enable hybrid X25519MLKEM768 via OpenSSL 3.5+) | First-Party Code (SAST/AST)<br>`python/ciphertrust_ekm_example.py:47` |
| `@noble/hashes (Noble Cryptographic Digest & KDF Suite (SHA-256 / SHA-512 / SHA3-256 / HKDF / scrypt))` | hash | 256 / 512 | Quantum-Resistant (Grover's proof) | Assimilated Upstream CBOM: Noble Audited JavaScript Hashes & KDFs (SHA-2 / SHA-3 / HKDF / PBKDF2 / scrypt)<br>`Dependency: @noble/hashes@1.8.0` |
| `cryptography (PyCA OpenSSL EVP Symmetric & AEAD Suite (AES-256-GCM / ChaCha20-Poly1305 / Fernet))` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@44.0.1` |

### ⚠️ Unassimilated Third-Party Binaries & Cryptographic Blind Spots

> ℹ️ *The following third-party dependencies do not have verified upstream CBOM attestations in the catalog. They lower the audit confidence score until explicit CBOMs or attestations are published.* 

| Dependency Name | Version | Package URL (purl) | Status |
|---|---|---|---|
| `crypto-lab-js` | 1.1.0 | `pkg:npm/crypto-lab-js@1.1.0` | 🟡 Unassimilated (No upstream CBOM) |

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
