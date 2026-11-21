## 🛡️ Cryptographic Bill of Materials (CBOM) & PQC Migration Assessment

**Format**: CycloneDX (v1.6) | **First-Party Code Crypto Assets**: 70 | **Total Tracked Crypto Assets**: 75

### 📊 Post-Quantum Migration Scorecard

| Metric | Count | Migration Status |
|---|---|---|
| **Post-Quantum Ready (PQC)** | **5** | 🟢 Quantum-Resistant (NIST FIPS 203/204/205) |
| **Quantum-Vulnerable (Backlog)** | **49** | 🔴 At Risk of 'Harvest Now, Decrypt Later' |
| **Classical Symmetric / Digest** | **21** | 🟡 Classical Security (Requires AES-256 / SHA-256+) |
| **Asymmetric PQC Migration Progress** | **9.3%** | (5 of 54 asymmetric/vulnerable primitives migrated) |

### 🎯 Cryptographic Supply Chain Coverage & Confidence

| Evaluation Layer | Coverage / Status | Audit Confidence Assessment |
|---|---|---|
| **First-Party Code (`src/`, `scripts/`)** | **100% Audited** (70 Crypto Primitive(s) Inventoried across Java (91), JavaScript (48), PowerShell (10), Python (120), Shell (16)) | 🟢 **HIGH** (Direct AST & SAST verified) |
| **Third-Party Supply Chain** | **94.7%** (18 of 19 dependencies cataloged) | 🟢 HIGH (Known profiles assimilated) |
| **Overall Audit Confidence Score** | **95.0%** | 🟢 HIGH (1 unassimilated supply chain dependencies) |

| **System OS Inventory** | **Pending Update** | 🟡 **Warning** (Local OS crypto components not yet inventoried) |

### ✅ Post-Quantum Ready Assets

| Component Name | Primitive | Key/Parameter Set | PQC Standard | Provenance / Location(s) |
|---|---|---|---|---|
| `ML-DSA-65` | signature | 65 | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`demo_langs.sh:131`<br>`demo_langs.sh:132`<br>`demo_langs.sh:144`<br>`demo_langs.ps1:42`<br>`demo_langs.ps1:51`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:113`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:116`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:19`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:20`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:25`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:32`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:42`<br>`javascript/src/ml_dsa_example.js:2`<br>`javascript/src/ml_dsa_example.js:10`<br>`javascript/src/ml_dsa_example.js:20`<br>`javascript/src/ml_dsa_example.js:31`<br>`javascript/src/run_all.js:69` |
| `ML-KEM-768` | kem | 768 | ML-KEM (FIPS 203) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`demo_langs.sh:131`<br>`demo_langs.sh:132`<br>`demo_langs.sh:144`<br>`demo_langs.ps1:42`<br>`demo_langs.ps1:51`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:20`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:21`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:26`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:32`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:72`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:84`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:86`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:90`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br>`javascript/src/ml_kem_example.js:2`<br>`javascript/src/ml_kem_example.js:11`<br>`javascript/src/ml_kem_example.js:20`<br>`javascript/src/ml_kem_example.js:30`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/run_all.js:55`<br>`javascript/src/run_all.js:60`<br>`javascript/src/run_all.js:86`<br>`javascript/src/hybrid_kem_example.js:2`<br>`javascript/src/hybrid_kem_example.js:33`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:49`<br>`javascript/src/hybrid_kem_example.js:50` |
| `SLH-DSA` | signature | 128s/256f | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`demo_langs.sh:145`<br>`javascript/src/slh_dsa_example.js:2`<br>`javascript/src/slh_dsa_example.js:11`<br>`javascript/src/slh_dsa_example.js:21`<br>`javascript/src/slh_dsa_example.js:32`<br>`javascript/src/run_all.js:94` |
| `@noble/post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: @noble/post-quantum@0.4.1` |
| `post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: post-quantum@0.4.0` |

### ⚠️ Quantum-Vulnerable Assets & Remediation Plan

| Component / Algorithm | Type / Primitive | Key Length / Curve | Recommended Target | Provenance / Context |
|---|---|---|---|---|
| **`secret-key@074531e7-dcd6-404e-bf89-6c8c3a179a69`**<br><sub>secret-key@074531e7-dcd6-404e-bf89-6c8c3a179a69</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`key@9dce3fd5-ce09-4859-a86b-d626f44d1311`**<br><sub>key@9dce3fd5-ce09-4859-a86b-d626f44d1311</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`RSA-OAEP`**<br><sub>RSA-OAEP</sub> | algorithm / pke | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@cb93037c-418b-44f5-a2ad-78c2233ada55`**<br><sub>secret-key@cb93037c-418b-44f5-a2ad-78c2233ada55</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HmacExample.java` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`RSA-PSS`**<br><sub>RSA-PSS</sub> | algorithm / signature | N/A | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@1d0cd126-7530-46be-bf1d-4362db75ee57`**<br><sub>password@1d0cd126-7530-46be-bf1d-4362db75ee57</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@d0c71967-e6f1-4870-881c-46066ba00fd6`**<br><sub>secret-key@d0c71967-e6f1-4870-881c-46066ba00fd6</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`password@1b7e728d-94e9-4561-a2b3-7d7c41166439`**<br><sub>password@1b7e728d-94e9-4561-a2b3-7d7c41166439</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@0672bfdb-08fb-4d8e-8ecc-b50fcd28369c`**<br><sub>password@0672bfdb-08fb-4d8e-8ecc-b50fcd28369c</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@993fb5d8-4dd3-44b7-9128-23e739e55514`**<br><sub>password@993fb5d8-4dd3-44b7-9128-23e739e55514</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`secret-key@c44d4461-8e52-4618-9fe7-fc3609fb76fb`**<br><sub>secret-key@c44d4461-8e52-4618-9fe7-fc3609fb76fb</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`key@2a899ea5-2fb0-4924-a720-34e6d14c517c`**<br><sub>key@2a899ea5-2fb0-4924-a720-34e6d14c517c</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`salt@c95160bf-3a6a-43b1-80e6-fcc1beff062b`**<br><sub>salt@c95160bf-3a6a-43b1-80e6-fcc1beff062b</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`key@6447559a-0515-4841-a0de-34be51473c65`**<br><sub>key@6447559a-0515-4841-a0de-34be51473c65</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@9e3ac123-3fc1-4dbc-862e-c7cec349afbf`**<br><sub>secret-key@9e3ac123-3fc1-4dbc-862e-c7cec349afbf</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@7f3fb5b5-6db1-495e-a293-875627e5dade`**<br><sub>secret-key@7f3fb5b5-6db1-495e-a293-875627e5dade</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@7cc17866-3d9a-4e38-8deb-d0911fc007e0`**<br><sub>password@7cc17866-3d9a-4e38-8deb-d0911fc007e0</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@02c0dbbb-e917-4188-ba94-82c2388fa38e`**<br><sub>password@02c0dbbb-e917-4188-ba94-82c2388fa38e</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@2d2a5ad3-7ba6-47fb-8229-24b7d7d64bb7`**<br><sub>password@2d2a5ad3-7ba6-47fb-8229-24b7d7d64bb7</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@afe5f299-fd4d-4255-8e6f-beed8a233d7b`**<br><sub>secret-key@afe5f299-fd4d-4255-8e6f-beed8a233d7b</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`secret-key@62e0a713-ddf9-4a38-9b0b-875639f4877d`**<br><sub>secret-key@62e0a713-ddf9-4a38-9b0b-875639f4877d</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`key@0df95e19-f513-4edc-ad92-3f3814f89c53`**<br><sub>key@0df95e19-f513-4edc-ad92-3f3814f89c53</sub> | related-crypto-material / secret-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@2e19e34e-9c4a-4dc5-b943-7411626e5373`**<br><sub>secret-key@2e19e34e-9c4a-4dc5-b943-7411626e5373</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`secret-key@f4d131ee-2dbf-4cb0-8bf9-e8aba24b12ae`**<br><sub>secret-key@f4d131ee-2dbf-4cb0-8bf9-e8aba24b12ae</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| **`secret-key@d6f3eb36-2e56-4f34-bd58-cd0cf66c9f2f`**<br><sub>secret-key@d6f3eb36-2e56-4f34-bd58-cd0cf66c9f2f</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`secret-key@297169dc-4f02-4369-b7be-8be4049d9b98`**<br><sub>secret-key@297169dc-4f02-4369-b7be-8be4049d9b98</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| **`password@85cb149c-5716-4e83-9103-2ae40de41b48`**<br><sub>password@85cb149c-5716-4e83-9103-2ae40de41b48</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`key@a23e670e-e6e6-496a-bddd-2f3226f2a085`**<br><sub>key@a23e670e-e6e6-496a-bddd-2f3226f2a085</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java` |
| **`secret-key@2f8ab657-78d6-45d4-8f24-22f0260d0e2c`**<br><sub>secret-key@2f8ab657-78d6-45d4-8f24-22f0260d0e2c</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`salt@014cd65d-930f-4393-8f20-c557abbf24aa`**<br><sub>salt@014cd65d-930f-4393-8f20-c557abbf24aa</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@8c5e8ab8-b776-4214-b41e-cf6f0bbe9696`**<br><sub>password@8c5e8ab8-b776-4214-b41e-cf6f0bbe9696</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`private-key@ec2190da-6689-465f-accf-20dccaf913d2`**<br><sub>private-key@ec2190da-6689-465f-accf-20dccaf913d2</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/test_crypto.py` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py`<br><br>`python/gcp_kms_byok_cmk_example.py`<br><br>`python/azure_keyvault_byok_cmk_example.py`<br><br>`demo_langs.sh:111`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Running SHA-256, HMAC, PBKDF2, AES-256-GCM, RSA-3072, Ed25519, X25519+HKDF, AES-KW, and</code></sub><br><br>`python/rsa_oaep_pss_example.py:9`<br><sub><code>return rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/rsa_oaep_pss_example.py:1`<br><sub><code>"""RSA-3072 OAEP encryption and RSA-PSS signatures using SHA-256."""</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:46`<br><sub><code>self._import_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:47`<br><sub><code>self._kek_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub> |
| **`private-key@cec43f0f-4ad9-405f-a72b-352a87256231`**<br><sub>private-key@cec43f0f-4ad9-405f-a72b-352a87256231</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/test_crypto.py` |
| **`private-key@80ff727e-0545-4055-85fc-184e53996f15`**<br><sub>private-key@80ff727e-0545-4055-85fc-184e53996f15</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py` |
| **`private-key@7b142e86-a632-4f4b-8f29-bdb54d75139d`**<br><sub>private-key@7b142e86-a632-4f4b-8f29-bdb54d75139d</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/azure_keyvault_byok_cmk_example.py` |
| **`private-key@b848b30e-d46e-4789-9bc7-ff855343128d`**<br><sub>private-key@b848b30e-d46e-4789-9bc7-ff855343128d</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/ed25519_example.py` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`python/private_key_serialisation_example.py`<br><br>`python/test_crypto.py`<br><br>`python/test_crypto.py`<br><br>`python/ed25519_example.py`<br><br>`python/run_all.py:5`<br><sub><code>from ed25519_example import main as ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:7`<br><sub><code>def serialise_encrypted(private_key: ed25519.Ed25519PrivateKey, password: bytes) -> bytes:</code></sub><br><br>`python/private_key_serialisation_example.py:15`<br><sub><code>def load_encrypted(pem: bytes, password: bytes) -> ed25519.Ed25519PrivateKey:</code></sub><br><br>`python/private_key_serialisation_example.py:17`<br><sub><code>if not isinstance(key, ed25519.Ed25519PrivateKey):</code></sub><br><br>`python/private_key_serialisation_example.py:24`<br><sub><code>original = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`python/ed25519_example.py:1`<br><sub><code>"""Ed25519 signing and verification."""</code></sub><br><br>`python/ed25519_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/ed25519_example.py:7`<br><sub><code>def sign(private_key: ed25519.Ed25519PrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/ed25519_example.py:11`<br><sub><code>def verify(public_key: ed25519.Ed25519PublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/ed25519_example.py:20`<br><sub><code>private_key = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:57`<br><sub><code>byte[] edMsg = "ed25519 message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:59`<br><sub><code>CryptoSupport.require(Ed25519Example.verify(edKeys.getPublic(), edMsg, edSig), "Ed25519 verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:60`<br><sub><code>CryptoSupport.require(!Ed25519Example.verify(edKeys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), edSig), "E</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:10`<br><sub><code>return KeyPairGenerator.getInstance("Ed25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:14`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:21`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:31`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "Ed25519 failed");</code></sub> |
| **`private-key@3fba379c-eaaf-41f8-86dd-370529bf1396`**<br><sub>private-key@3fba379c-eaaf-41f8-86dd-370529bf1396</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/private_key_serialisation_example.py` |
| **`secret-key@14755956-e3c0-412b-bccc-501c06dcfae0`**<br><sub>secret-key@14755956-e3c0-412b-bccc-501c06dcfae0</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py` |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py`<br><br>`python/x25519_hkdf_example.py`<br><br>`python/test_crypto.py`<br><br>`python/test_crypto.py` |
| **`private-key@6be6c2a9-c3e3-4c40-b952-c3f27921b30c`**<br><sub>private-key@6be6c2a9-c3e3-4c40-b952-c3f27921b30c</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/gcp_kms_byok_cmk_example.py` |
| **`ECDH-X25519`**<br><sub>ECDH-X25519</sub> | algorithm / key-agreement | 25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`demo_langs.sh:111`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Running SHA-256, HMAC, PBKDF2, AES-256-GCM, RSA-3072, Ed25519, X25519+HKDF, AES-KW, and</code></sub><br><br>`demo_langs.sh:130`<br><sub><code>echo -e "  ${MAGENTA}[PROBLEM]${NC} Quantum computers running Shor's algorithm will break RSA, X25519, and Ed25519 ('Har</code></sub><br><br>`demo_langs.sh:131`<br><sub><code>echo -e "  ${CYAN}[WHAT]${NC}    Compiling and running Java 25 JCA/JCE examples including ML-KEM-768, Hybrid X25519+ML-K</code></sub><br><br>`python/run_all.py:11`<br><sub><code>from x25519_hkdf_example import main as x25519</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/x25519_hkdf_example.py:1`<br><sub><code>"""X25519 key agreement followed by HKDF-SHA-256 key derivation."""</code></sub><br><br>`python/x25519_hkdf_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import x25519</code></sub><br><br>`python/x25519_hkdf_example.py:10`<br><sub><code>def derive_key(private_key: x25519.X25519PrivateKey,</code></sub><br><br>`python/x25519_hkdf_example.py:11`<br><sub><code>peer_public_key: x25519.X25519PublicKey,</code></sub><br><br>`python/x25519_hkdf_example.py:24`<br><sub><code>alice = x25519.X25519PrivateKey.generate()</code></sub><br><br>`python/x25519_hkdf_example.py:25`<br><sub><code>bob = x25519.X25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypted), "Hybrid X25519+ML-KEM-768 round-trip failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:17`<br><sub><code>return KeyPairGenerator.getInstance("X25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:21`<br><sub><code>KeyAgreement agreement = KeyAgreement.getInstance("X25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:30`<br><sub><code>throw new IllegalArgumentException("IKM must be 32 bytes for X25519.");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:60`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceSecret, bobSecret), "X25519 mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:69`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceKey, bobKey), "X25519-HKDF mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br><sub><code>"Hybrid X25519+ML-KEM-768 round-trip failed"</code></sub><br><br>`javascript/src/run_all.js:86`<br><sub><code>throw new Error('Hybrid X25519+ML-KEM-768 round-trip failed');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:9`<br><sub><code>return generateKeyPairSync('x25519');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:35`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:50`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub> |
| **`RSA-2048`**<br><sub>RSA-2048</sub> | algorithm / signature | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`demo_langs.sh:130`<br><sub><code>echo -e "  ${MAGENTA}[PROBLEM]${NC} Quantum computers running Shor's algorithm will break RSA, X25519, and Ed25519 ('Har</code></sub><br><br>`python/rsa_oaep_pss_example.py:5`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/rsa_oaep_pss_example.py:8`<br><sub><code>def generate_private_key() -> rsa.RSAPrivateKey:</code></sub><br><br>`python/rsa_oaep_pss_example.py:27`<br><sub><code>def encrypt(public_key: rsa.RSAPublicKey, plaintext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:31`<br><sub><code>def decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:35`<br><sub><code>def sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:39`<br><sub><code>def verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/run_all.py:10`<br><sub><code>from rsa_oaep_pss_example import main as rsa</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:17`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:75`<br><sub><code>def prepare_gcp_byok_blob(import_job_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:18`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:52`<br><sub><code>"""Unwrap a BYOK blob (RSA-OAEP-256 wrapped AES-KWP key) inside the HSM boundary."""</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:67`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:79`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:91`<br><sub><code>def prepare_azure_byok_blob(hsm_kek_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:120`<br><sub><code>wrapped_dek = crypto_client.wrap_key("RSA-OAEP-256", dek)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:132`<br><sub><code>dek = crypto_client.unwrap_key("RSA-OAEP-256", envelope.wrapped_dek)</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:16`<br><sub><code>KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:26`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:32`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:61`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:63`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "RSA-PSS failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:48`<br><sub><code>byte[] rsaMsg = "rsa message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:50`<br><sub><code>CryptoSupport.require(Arrays.equals(rsaMsg, RsaOaepPssExample.decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed"</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:52`<br><sub><code>CryptoSupport.require(RsaOaepPssExample.verify(keys.getPublic(), rsaMsg, signature), "RSA-PSS verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:53`<br><sub><code>CryptoSupport.require(!RsaOaepPssExample.verify(keys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), signature</code></sub> |
| **`Diffie-Hellman`**<br><sub>Diffie-Hellman</sub> | algorithm / key-agreement | 2048 | **ML-KEM (KEM) or ML-DSA (Signatures)** | First-Party Code (SAST/AST)<br>`javascript/src/hybrid_kem_example.js:1`<br><sub><code>import { diffieHellman, generateKeyPairSync, hkdfSync, randomBytes } from 'node:crypto';</code></sub><br><br>`javascript/src/hybrid_kem_example.js:29`<br><sub><code>const x25519Secret = diffieHellman({</code></sub><br><br>`javascript/src/hybrid_kem_example.js:45`<br><sub><code>const x25519Secret = diffieHellman({</code></sub> |
| **`cryptography (PyCA OpenSSL Asymmetric Primitives (RSA / ECDSA / Ed25519 / X25519))`**<br><sub>RSA-2048 / ECDSA-P256 / Ed25519 / X25519</sub> | signature / signature | 2048 / 256 | **Migrate asymmetric PKI/JWT workflows to OpenSSL 3.5+ ML-KEM (FIPS 203) and ML-DSA (FIPS 204)** | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@44.0.1` |

### 🔒 Classical Symmetric & Digest Assets

| Component Name | Primitive | Key Length | Quantum Resistance Assessment | Provenance / Location(s) |
|---|---|---|---|---|
| `AES-128` | block-cipher | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `PBKDF2-HMAC-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-128-GCM` | ae | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| `MGF1` | other | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-256` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/HashingExample.java` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| `AES-256-GCM` | ae | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py`<br>`demo_langs.sh:111`<br>`demo_langs.sh:154`<br>`demo_langs.ps1:60`<br>`powershell/AesGcmExample.ps1:3`<br>`powershell/AesGcmExample.ps1:8`<br>`powershell/AesGcmExample.ps1:12`<br>`powershell/AesGcmExample.ps1:24`<br>`powershell/AesGcmExample.ps1:32`<br>`python/run_all.py:3`<br>`python/run_all.py:15`<br>`python/aes_gcm_example.py:1`<br>`python/aes_gcm_example.py:5`<br>`python/aes_gcm_example.py:17`<br>`python/aes_gcm_example.py:22`<br>`python/aes_gcm_example.py:26`<br>`python/x25519_hkdf_example.py:27`<br>`python/gcp_kms_byok_cmk_example.py:18`<br>`python/gcp_kms_byok_cmk_example.py:67`<br>`python/gcp_kms_byok_cmk_example.py:72`<br>`python/gcp_kms_byok_cmk_example.py:104`<br>`python/gcp_kms_byok_cmk_example.py:108`<br>`python/gcp_kms_byok_cmk_example.py:119`<br>`python/azure_keyvault_byok_cmk_example.py:19`<br>`python/azure_keyvault_byok_cmk_example.py:52`<br>`python/azure_keyvault_byok_cmk_example.py:118`<br>`python/azure_keyvault_byok_cmk_example.py:122`<br>`python/azure_keyvault_byok_cmk_example.py:133`<br>`python/aes_key_wrap_example.py:1`<br>`python/stage3_multi_cloud_ekm_orchestration.py:18`<br>`python/stage3_multi_cloud_ekm_orchestration.py:58`<br>`python/stage3_multi_cloud_ekm_orchestration.py:62`<br>`python/stage3_multi_cloud_ekm_orchestration.py:79`<br>`python/stage3_multi_cloud_ekm_orchestration.py:80`<br>`python/ciphertrust_ekm_example.py:22`<br>`python/ciphertrust_ekm_example.py:136`<br>`python/ciphertrust_ekm_example.py:153`<br>`python/ciphertrust_ekm_example.py:194`<br>`python/ciphertrust_ekm_example.py:253`<br>`python/ciphertrust_ekm_example.py:263`<br>`python/external_kms_ekm_example.py:20`<br>`python/external_kms_ekm_example.py:91`<br>`python/external_kms_ekm_example.py:97`<br>`python/external_kms_ekm_example.py:160`<br>`python/external_kms_ekm_example.py:173`<br>`python/vault_ekm_proxy_example.py:22`<br>`python/vault_ekm_proxy_example.py:83`<br>`python/vault_ekm_proxy_example.py:92`<br>`python/vault_ekm_proxy_example.py:111`<br>`python/vault_ekm_proxy_example.py:122`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:47`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:56`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:13`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:27`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:35`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:59`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:80`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:62`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:37`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:44`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:76`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:21`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:28`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:38`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:49`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/aes_gcm_example.js:20`<br>`javascript/src/aes_gcm_example.js:23`<br>`javascript/src/aes_gcm_example.js:41`<br>`javascript/src/aes_gcm_example.js:43`<br>`javascript/src/run_all.js:46`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:50` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`python/hmac_example.py`<br>`python/hmac_example.py` |
| `AES-128` | other | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`python/gcp_kms_byok_cmk_example.py`<br>`python/azure_keyvault_byok_cmk_example.py`<br>`python/aes_key_wrap_example.py` |
| `HKDF-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py` |
| `PBKDF2-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/pbkdf2_example.py` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py`<br>`python/hmac_example.py`<br>`python/hmac_example.py`<br>`python/pbkdf2_example.py`<br>`python/hashing_example.py`<br>`demo_langs.sh:111`<br>`python/rsa_oaep_pss_example.py:1`<br>`python/rsa_oaep_pss_example.py:14`<br>`python/rsa_oaep_pss_example.py:15`<br>`python/rsa_oaep_pss_example.py:22`<br>`python/rsa_oaep_pss_example.py:23`<br>`python/rsa_oaep_pss_example.py:36`<br>`python/rsa_oaep_pss_example.py:41`<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:16`<br>`python/hmac_example.py:1`<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`python/gcp_kms_byok_cmk_example.py:56`<br>`python/gcp_kms_byok_cmk_example.py:57`<br>`python/gcp_kms_byok_cmk_example.py:81`<br>`python/gcp_kms_byok_cmk_example.py:82`<br>`python/azure_keyvault_byok_cmk_example.py:57`<br>`python/azure_keyvault_byok_cmk_example.py:58`<br>`python/azure_keyvault_byok_cmk_example.py:72`<br>`python/azure_keyvault_byok_cmk_example.py:73`<br>`python/azure_keyvault_byok_cmk_example.py:84`<br>`python/azure_keyvault_byok_cmk_example.py:85`<br>`python/azure_keyvault_byok_cmk_example.py:97`<br>`python/azure_keyvault_byok_cmk_example.py:98`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:22`<br>`python/hashing_example.py:1`<br>`python/hashing_example.py:6`<br>`python/hashing_example.py:7`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:22`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:38`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:13`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:14`<br>`java/src/main/java/org/example/crypto/HashingExample.java:9`<br>`java/src/main/java/org/example/crypto/HashingExample.java:10`<br>`java/src/main/java/org/example/crypto/HashingExample.java:14`<br>`java/src/main/java/org/example/crypto/HashingExample.java:15`<br>`javascript/src/ml_kem_example.js:41`<br>`javascript/src/hashing.js:8`<br>`javascript/src/hashing.js:9`<br>`javascript/src/hmac_example.js:10`<br>`javascript/src/run_all.js:2`<br>`javascript/src/run_all.js:28`<br>`javascript/src/hybrid_kem_example.js:22` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/private_key_serialisation_example.py`<br>`python/test_crypto.py`<br>`python/test_crypto.py`<br>`python/ed25519_example.py` |
| `PBKDF2-HMAC-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`demo_langs.sh:111`<br>`python/run_all.py:8`<br>`python/run_all.py:15`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:6`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:25`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:36`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:49`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:29`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:30` |
| `HKDF-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:5`<br>`python/x25519_hkdf_example.py:15`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:32`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:65`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:69` |
| `HMAC-SHA256` | mac | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`java/src/main/java/org/example/crypto/HmacExample.java:11`<br>`java/src/main/java/org/example/crypto/HmacExample.java:12`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:25`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:27`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:30`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:34`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:35`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:41`<br>`javascript/src/hmac_example.js:10` |
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
