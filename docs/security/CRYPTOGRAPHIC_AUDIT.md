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
| **First-Party Code (`src/`, `scripts/`)** | **100% Audited** (70 Crypto Primitive(s) Inventoried across Java (91), JavaScript (48), PowerShell (10), Python (111), Shell (5)) | 🟢 **HIGH** (Direct AST & SAST verified) |
| **Third-Party Supply Chain** | **94.7%** (18 of 19 dependencies cataloged) | 🟢 HIGH (Known profiles assimilated) |
| **Overall Audit Confidence Score** | **95.0%** | 🟢 HIGH (1 unassimilated supply chain dependencies) |

| **System OS Inventory** | **Pending Update** | 🟡 **Warning** (Local OS crypto components not yet inventoried) |

### ✅ Post-Quantum Ready Assets

| Component Name | Primitive | Key/Parameter Set | PQC Standard | Provenance / Location(s) |
|---|---|---|---|---|
| `ML-DSA-65` | signature | 65 | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java`<br>`demo_langs.sh:28`<br>`demo_langs.sh:38`<br>`demo_langs.ps1:29`<br>`demo_langs.ps1:38`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:19`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:20`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:25`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:32`<br>`java/src/main/java/org/example/crypto/MlDsaExample.java:42`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:113`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:116`<br>`javascript/src/ml_dsa_example.js:2`<br>`javascript/src/ml_dsa_example.js:10`<br>`javascript/src/ml_dsa_example.js:20`<br>`javascript/src/ml_dsa_example.js:31`<br>`javascript/src/run_all.js:69` |
| `ML-KEM-768` | kem | 768 | ML-KEM (FIPS 203) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`demo_langs.sh:28`<br>`demo_langs.sh:38`<br>`demo_langs.ps1:29`<br>`demo_langs.ps1:38`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:20`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:21`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:26`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:32`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:72`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:84`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:86`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:90`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br>`javascript/src/hybrid_kem_example.js:2`<br>`javascript/src/hybrid_kem_example.js:33`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:49`<br>`javascript/src/hybrid_kem_example.js:50`<br>`javascript/src/ml_kem_example.js:2`<br>`javascript/src/ml_kem_example.js:11`<br>`javascript/src/ml_kem_example.js:20`<br>`javascript/src/ml_kem_example.js:30`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/run_all.js:55`<br>`javascript/src/run_all.js:60`<br>`javascript/src/run_all.js:86` |
| `SLH-DSA` | signature | 128s/256f | ML-DSA (FIPS 204) | First-Party Code (SAST/AST)<br>`javascript/src/slh_dsa_example.js:2`<br>`javascript/src/slh_dsa_example.js:11`<br>`javascript/src/slh_dsa_example.js:21`<br>`javascript/src/slh_dsa_example.js:32`<br>`javascript/src/run_all.js:94` |
| `@noble/post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: @noble/post-quantum@0.4.1` |
| `post-quantum (Noble Post-Quantum KEM & Signatures (ML-KEM-768 / ML-DSA-65 / SLH-DSA))` | kem | 768 / 65 | ML-KEM (FIPS 203) | Assimilated Upstream CBOM: Noble Audited Post-Quantum Cryptography (ML-KEM / ML-DSA / SLH-DSA)<br>`Dependency: post-quantum@0.4.0` |

### ⚠️ Quantum-Vulnerable Assets & Remediation Plan

| Component / Algorithm | Type / Primitive | Key Length / Curve | Recommended Target | Provenance / Context |
|---|---|---|---|---|
| **`password@dfced11c-d507-479e-9800-48ea6efca593`**<br><sub>password@dfced11c-d507-479e-9800-48ea6efca593</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`RSA-OAEP`**<br><sub>RSA-OAEP</sub> | algorithm / pke | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@a26615d0-8a10-4699-90fd-1f7b84a2abb0`**<br><sub>secret-key@a26615d0-8a10-4699-90fd-1f7b84a2abb0</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`RSA-PSS`**<br><sub>RSA-PSS</sub> | algorithm / signature | N/A | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`secret-key@4762f036-b1f0-4fb1-ac3d-be8979bec236`**<br><sub>secret-key@4762f036-b1f0-4fb1-ac3d-be8979bec236</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`key@b2a84f42-04cc-4a3e-8ca2-c4f77303f117`**<br><sub>key@b2a84f42-04cc-4a3e-8ca2-c4f77303f117</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`secret-key@52f1a83d-473a-4852-8f4a-b1104fbba3a9`**<br><sub>secret-key@52f1a83d-473a-4852-8f4a-b1104fbba3a9</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@8ed03032-259a-4cd6-a6e3-6406695b6bf8`**<br><sub>password@8ed03032-259a-4cd6-a6e3-6406695b6bf8</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@11435366-e506-48c3-beea-145f16e7b323`**<br><sub>secret-key@11435366-e506-48c3-beea-145f16e7b323</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java` |
| **`key@2a62122d-187a-4156-8a2f-543f73d96f41`**<br><sub>key@2a62122d-187a-4156-8a2f-543f73d96f41</sub> | related-crypto-material / secret-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| **`secret-key@a45e9a9d-bd37-4d7d-95e7-05f4f10e524e`**<br><sub>secret-key@a45e9a9d-bd37-4d7d-95e7-05f4f10e524e</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@98fe53da-c3d1-43c8-adf5-781d668ec42a`**<br><sub>secret-key@98fe53da-c3d1-43c8-adf5-781d668ec42a</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`key@f1b8dd10-de54-41e9-88a4-e7cbd07cb635`**<br><sub>key@f1b8dd10-de54-41e9-88a4-e7cbd07cb635</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`key@813d02ea-f071-47f9-bf66-d12c353aa4e7`**<br><sub>key@813d02ea-f071-47f9-bf66-d12c353aa4e7</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlDsaExample.java` |
| **`password@596742c9-55df-4979-bc05-132abceeb51b`**<br><sub>password@596742c9-55df-4979-bc05-132abceeb51b</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`salt@1f7635f9-5b3d-4a3b-a094-56178d1c21e1`**<br><sub>salt@1f7635f9-5b3d-4a3b-a094-56178d1c21e1</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@31bc7d07-fc41-4ee5-8990-d88ea14d8892`**<br><sub>password@31bc7d07-fc41-4ee5-8990-d88ea14d8892</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`password@7f0b95da-9ac1-4db1-98aa-e5aa7dc926b9`**<br><sub>password@7f0b95da-9ac1-4db1-98aa-e5aa7dc926b9</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`secret-key@bfab302d-0ae7-4dac-9d55-c1b65fd9715d`**<br><sub>secret-key@bfab302d-0ae7-4dac-9d55-c1b65fd9715d</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`secret-key@93527518-ad6e-4830-975e-7292d5bd4d21`**<br><sub>secret-key@93527518-ad6e-4830-975e-7292d5bd4d21</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| **`secret-key@4ed5e4be-18fa-4956-8f85-90bee49cceb8`**<br><sub>secret-key@4ed5e4be-18fa-4956-8f85-90bee49cceb8</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java` |
| **`secret-key@37cc2de2-cde1-4c55-9567-0177ab21cba3`**<br><sub>secret-key@37cc2de2-cde1-4c55-9567-0177ab21cba3</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`password@192c4db3-d872-4c42-bbbc-bd7e14085fd6`**<br><sub>password@192c4db3-d872-4c42-bbbc-bd7e14085fd6</sub> | related-crypto-material / password | 112 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@87bac186-0e4a-4300-b6e0-742f5fc864ae`**<br><sub>secret-key@87bac186-0e4a-4300-b6e0-742f5fc864ae</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HmacExample.java` |
| **`password@c75a47bc-dd03-4afb-bd0a-0a04673511d2`**<br><sub>password@c75a47bc-dd03-4afb-bd0a-0a04673511d2</sub> | related-crypto-material / password | 224 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`key@be3cb68f-f0b5-427f-bee3-f8a836c53c2d`**<br><sub>key@be3cb68f-f0b5-427f-bee3-f8a836c53c2d</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java` |
| **`salt@78faf906-607b-4a3a-8727-ba1111a58c49`**<br><sub>salt@78faf906-607b-4a3a-8727-ba1111a58c49</sub> | related-crypto-material / salt | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| **`password@7d697078-ed2e-41ab-adcf-024279891713`**<br><sub>password@7d697078-ed2e-41ab-adcf-024279891713</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@4b86d476-9518-4614-8c78-acfc1def21fd`**<br><sub>secret-key@4b86d476-9518-4614-8c78-acfc1def21fd</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| **`secret-key@449b41ae-b00d-464a-a7f9-a626ce6be16b`**<br><sub>secret-key@449b41ae-b00d-464a-a7f9-a626ce6be16b</sub> | related-crypto-material / secret-key | 256 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| **`password@d8942c49-fdf2-4411-b3a1-8c464b965574`**<br><sub>password@d8942c49-fdf2-4411-b3a1-8c464b965574</sub> | related-crypto-material / password | 104 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/TestCrypto.java` |
| **`secret-key@6ce65a2a-0c05-4989-9535-3b70799c8151`**<br><sub>secret-key@6ce65a2a-0c05-4989-9535-3b70799c8151</sub> | related-crypto-material / secret-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py` |
| **`private-key@05acea24-83e4-4a6c-8ad1-ce0de641d2cd`**<br><sub>private-key@05acea24-83e4-4a6c-8ad1-ce0de641d2cd</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/azure_keyvault_byok_cmk_example.py` |
| **`private-key@fb95d501-ddc6-47ab-8d8b-acb8a602129f`**<br><sub>private-key@fb95d501-ddc6-47ab-8d8b-acb8a602129f</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/test_crypto.py` |
| **`RSA-3072`**<br><sub>RSA-3072</sub> | algorithm / pke | 3072 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py`<br><br>`python/gcp_kms_byok_cmk_example.py`<br><br>`python/azure_keyvault_byok_cmk_example.py`<br><br>`python/rsa_oaep_pss_example.py:9`<br><sub><code>return rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/rsa_oaep_pss_example.py:1`<br><sub><code>"""RSA-3072 OAEP encryption and RSA-PSS signatures using SHA-256."""</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:46`<br><sub><code>self._import_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:47`<br><sub><code>self._kek_private = rsa.generate_private_key(public_exponent=65537, key_size=3072)</code></sub> |
| **`private-key@3764edde-1afe-4247-a699-7fb178c502bb`**<br><sub>private-key@3764edde-1afe-4247-a699-7fb178c502bb</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/test_crypto.py` |
| **`private-key@49b2b1a8-f23c-4f3c-9bcf-b3d0f900df32`**<br><sub>private-key@49b2b1a8-f23c-4f3c-9bcf-b3d0f900df32</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/rsa_oaep_pss_example.py` |
| **`private-key@d6f2b995-3ef8-4b8b-bf43-ade2c128a84f`**<br><sub>private-key@d6f2b995-3ef8-4b8b-bf43-ade2c128a84f</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/ed25519_example.py` |
| **`private-key@f6b29ba0-6391-4d4c-a3d1-e1d956350619`**<br><sub>private-key@f6b29ba0-6391-4d4c-a3d1-e1d956350619</sub> | related-crypto-material / private-key | Key | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/private_key_serialisation_example.py` |
| **`Ed25519`**<br><sub>Ed25519</sub> | algorithm / signature | Edwards25519 | **ML-DSA-65 / Dilithium (FIPS 204)** | First-Party Code (SAST/AST)<br>`python/ed25519_example.py`<br><br>`python/test_crypto.py`<br><br>`python/test_crypto.py`<br><br>`python/private_key_serialisation_example.py`<br><br>`python/run_all.py:5`<br><sub><code>from ed25519_example import main as ed25519</code></sub><br><br>`python/ed25519_example.py:1`<br><sub><code>"""Ed25519 signing and verification."""</code></sub><br><br>`python/ed25519_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/ed25519_example.py:7`<br><sub><code>def sign(private_key: ed25519.Ed25519PrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/ed25519_example.py:11`<br><sub><code>def verify(public_key: ed25519.Ed25519PublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/ed25519_example.py:20`<br><sub><code>private_key = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`python/private_key_serialisation_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import ed25519</code></sub><br><br>`python/private_key_serialisation_example.py:7`<br><sub><code>def serialise_encrypted(private_key: ed25519.Ed25519PrivateKey, password: bytes) -> bytes:</code></sub><br><br>`python/private_key_serialisation_example.py:15`<br><sub><code>def load_encrypted(pem: bytes, password: bytes) -> ed25519.Ed25519PrivateKey:</code></sub><br><br>`python/private_key_serialisation_example.py:17`<br><sub><code>if not isinstance(key, ed25519.Ed25519PrivateKey):</code></sub><br><br>`python/private_key_serialisation_example.py:24`<br><sub><code>original = ed25519.Ed25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:10`<br><sub><code>return KeyPairGenerator.getInstance("Ed25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:14`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:21`<br><sub><code>Signature signature = Signature.getInstance("Ed25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/Ed25519Example.java:31`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "Ed25519 failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:57`<br><sub><code>byte[] edMsg = "ed25519 message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:59`<br><sub><code>CryptoSupport.require(Ed25519Example.verify(edKeys.getPublic(), edMsg, edSig), "Ed25519 verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:60`<br><sub><code>CryptoSupport.require(!Ed25519Example.verify(edKeys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), edSig), "E</code></sub> |
| **`x25519`**<br><sub>x25519</sub> | algorithm / key-agree | Curve25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py`<br><br>`python/x25519_hkdf_example.py`<br><br>`python/test_crypto.py`<br><br>`python/test_crypto.py` |
| **`private-key@2b7b714f-6deb-4932-b858-06cd521aa703`**<br><sub>private-key@2b7b714f-6deb-4932-b858-06cd521aa703</sub> | related-crypto-material / private-key | 3072 | **ML-DSA-65 / SLH-DSA X.509 Certificate & KMS Key Rotation** | First-Party Code (SAST/AST)<br>`python/gcp_kms_byok_cmk_example.py` |
| **`RSA-2048`**<br><sub>RSA-2048</sub> | algorithm / signature | 2048 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/run_all.py:10`<br><sub><code>from rsa_oaep_pss_example import main as rsa</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/rsa_oaep_pss_example.py:5`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/rsa_oaep_pss_example.py:8`<br><sub><code>def generate_private_key() -> rsa.RSAPrivateKey:</code></sub><br><br>`python/rsa_oaep_pss_example.py:27`<br><sub><code>def encrypt(public_key: rsa.RSAPublicKey, plaintext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:31`<br><sub><code>def decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:35`<br><sub><code>def sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:</code></sub><br><br>`python/rsa_oaep_pss_example.py:39`<br><sub><code>def verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:17`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/gcp_kms_byok_cmk_example.py:75`<br><sub><code>def prepare_gcp_byok_blob(import_job_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:18`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import padding, rsa</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:52`<br><sub><code>"""Unwrap a BYOK blob (RSA-OAEP-256 wrapped AES-KWP key) inside the HSM boundary."""</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:67`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:79`<br><sub><code>if algorithm != "RSA-OAEP-256":</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:91`<br><sub><code>def prepare_azure_byok_blob(hsm_kek_public: rsa.RSAPublicKey, target_key_material: bytes) -> bytes:</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:120`<br><sub><code>wrapped_dek = crypto_client.wrap_key("RSA-OAEP-256", dek)</code></sub><br><br>`python/azure_keyvault_byok_cmk_example.py:132`<br><sub><code>dek = crypto_client.unwrap_key("RSA-OAEP-256", envelope.wrapped_dek)</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:16`<br><sub><code>KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:26`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:32`<br><sub><code>Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPPadding");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:61`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:63`<br><sub><code>CryptoSupport.require(verify(keys.getPublic(), message, signature), "RSA-PSS failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:48`<br><sub><code>byte[] rsaMsg = "rsa message".getBytes(StandardCharsets.UTF_8);</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:50`<br><sub><code>CryptoSupport.require(Arrays.equals(rsaMsg, RsaOaepPssExample.decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed"</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:52`<br><sub><code>CryptoSupport.require(RsaOaepPssExample.verify(keys.getPublic(), rsaMsg, signature), "RSA-PSS verify failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:53`<br><sub><code>CryptoSupport.require(!RsaOaepPssExample.verify(keys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), signature</code></sub> |
| **`ECDH-X25519`**<br><sub>ECDH-X25519</sub> | algorithm / key-agreement | 25519 | **ML-KEM-768 / Kyber (FIPS 203)** | First-Party Code (SAST/AST)<br>`python/run_all.py:11`<br><sub><code>from x25519_hkdf_example import main as x25519</code></sub><br><br>`python/run_all.py:15`<br><sub><code>for example in (hashing, hmac, pbkdf2, aes_gcm, rsa, ed25519, x25519, aes_key_wrap, private_key_serialisation):</code></sub><br><br>`python/x25519_hkdf_example.py:1`<br><sub><code>"""X25519 key agreement followed by HKDF-SHA-256 key derivation."""</code></sub><br><br>`python/x25519_hkdf_example.py:4`<br><sub><code>from cryptography.hazmat.primitives.asymmetric import x25519</code></sub><br><br>`python/x25519_hkdf_example.py:10`<br><sub><code>def derive_key(private_key: x25519.X25519PrivateKey,</code></sub><br><br>`python/x25519_hkdf_example.py:11`<br><sub><code>peer_public_key: x25519.X25519PublicKey,</code></sub><br><br>`python/x25519_hkdf_example.py:24`<br><sub><code>alice = x25519.X25519PrivateKey.generate()</code></sub><br><br>`python/x25519_hkdf_example.py:25`<br><sub><code>bob = x25519.X25519PrivateKey.generate()</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:17`<br><sub><code>return KeyPairGenerator.getInstance("X25519").generateKeyPair();</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:21`<br><sub><code>KeyAgreement agreement = KeyAgreement.getInstance("X25519");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:30`<br><sub><code>throw new IllegalArgumentException("IKM must be 32 bytes for X25519.");</code></sub><br><br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:60`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceSecret, bobSecret), "X25519 mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br><sub><code>"hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)</code></sub><br><br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:100`<br><sub><code>CryptoSupport.require(Arrays.equals(message, decrypted), "Hybrid X25519+ML-KEM-768 round-trip failed");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:69`<br><sub><code>CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceKey, bobKey), "X25519-HKDF mismatch");</code></sub><br><br>`java/src/main/java/org/example/crypto/TestCrypto.java:106`<br><sub><code>"Hybrid X25519+ML-KEM-768 round-trip failed"</code></sub><br><br>`javascript/src/hybrid_kem_example.js:9`<br><sub><code>return generateKeyPairSync('x25519');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:35`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub><br><br>`javascript/src/hybrid_kem_example.js:50`<br><sub><code>const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');</code></sub><br><br>`javascript/src/run_all.js:86`<br><sub><code>throw new Error('Hybrid X25519+ML-KEM-768 round-trip failed');</code></sub> |
| **`Diffie-Hellman`**<br><sub>Diffie-Hellman</sub> | algorithm / key-agreement | 2048 | **ML-KEM (KEM) or ML-DSA (Signatures)** | First-Party Code (SAST/AST)<br>`javascript/src/hybrid_kem_example.js:1`<br><sub><code>import { diffieHellman, generateKeyPairSync, hkdfSync, randomBytes } from 'node:crypto';</code></sub><br><br>`javascript/src/hybrid_kem_example.js:29`<br><sub><code>const x25519Secret = diffieHellman({</code></sub><br><br>`javascript/src/hybrid_kem_example.js:45`<br><sub><code>const x25519Secret = diffieHellman({</code></sub> |
| **`cryptography (PyCA OpenSSL Asymmetric Primitives (RSA / ECDSA / Ed25519 / X25519))`**<br><sub>RSA-2048 / ECDSA-P256 / Ed25519 / X25519</sub> | signature / signature | 2048 / 256 | **Migrate asymmetric PKI/JWT workflows to OpenSSL 3.5+ ML-KEM (FIPS 203) and ML-DSA (FIPS 204)** | Assimilated Upstream CBOM: PyCA Cryptography / OpenSSL 3.x EVP Reference CBOM<br>`Dependency: cryptography@44.0.1` |

### 🔒 Classical Symmetric & Digest Assets

| Component Name | Primitive | Key Length | Quantum Resistance Assessment | Provenance / Location(s) |
|---|---|---|---|---|
| `AES-128` | block-cipher | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/MlKemExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `PBKDF2-HMAC-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java` |
| `AES-128-GCM` | ae | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java` |
| `MGF1` | other | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `AES-256` | block-cipher | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/AesGcmExample.java`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/HashingExample.java`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/HmacExample.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java`<br>`java/src/main/java/org/example/crypto/Ed25519Example.java` |
| `AES-256-GCM` | ae | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/aes_gcm_example.py`<br>`demo_langs.sh:47`<br>`demo_langs.ps1:47`<br>`python/ciphertrust_ekm_example.py:22`<br>`python/ciphertrust_ekm_example.py:82`<br>`python/ciphertrust_ekm_example.py:94`<br>`python/ciphertrust_ekm_example.py:109`<br>`python/ciphertrust_ekm_example.py:150`<br>`python/ciphertrust_ekm_example.py:201`<br>`python/ciphertrust_ekm_example.py:211`<br>`python/run_all.py:3`<br>`python/run_all.py:15`<br>`python/x25519_hkdf_example.py:27`<br>`python/external_kms_ekm_example.py:20`<br>`python/external_kms_ekm_example.py:91`<br>`python/external_kms_ekm_example.py:97`<br>`python/external_kms_ekm_example.py:160`<br>`python/external_kms_ekm_example.py:173`<br>`python/gcp_kms_byok_cmk_example.py:18`<br>`python/gcp_kms_byok_cmk_example.py:67`<br>`python/gcp_kms_byok_cmk_example.py:72`<br>`python/gcp_kms_byok_cmk_example.py:104`<br>`python/gcp_kms_byok_cmk_example.py:108`<br>`python/gcp_kms_byok_cmk_example.py:119`<br>`python/aes_key_wrap_example.py:1`<br>`python/aes_gcm_example.py:1`<br>`python/aes_gcm_example.py:5`<br>`python/aes_gcm_example.py:17`<br>`python/aes_gcm_example.py:22`<br>`python/aes_gcm_example.py:26`<br>`python/azure_keyvault_byok_cmk_example.py:19`<br>`python/azure_keyvault_byok_cmk_example.py:52`<br>`python/azure_keyvault_byok_cmk_example.py:118`<br>`python/azure_keyvault_byok_cmk_example.py:122`<br>`python/azure_keyvault_byok_cmk_example.py:133`<br>`powershell/AesGcmExample.ps1:3`<br>`powershell/AesGcmExample.ps1:8`<br>`powershell/AesGcmExample.ps1:12`<br>`powershell/AesGcmExample.ps1:24`<br>`powershell/AesGcmExample.ps1:32`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:45`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:47`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:54`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:56`<br>`java/src/main/java/org/example/crypto/MlKemExample.java:77`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:62`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:21`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:28`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:38`<br>`java/src/main/java/org/example/crypto/AesGcmExample.java:49`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:13`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:27`<br>`java/src/main/java/org/example/crypto/AesKeyWrapExample.java:35`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:57`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:59`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:78`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:80`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:37`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:44`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:76`<br>`javascript/src/hybrid_kem_example.js:35`<br>`javascript/src/hybrid_kem_example.js:50`<br>`javascript/src/ml_kem_example.js:54`<br>`javascript/src/ml_kem_example.js:68`<br>`javascript/src/aes_gcm_example.js:20`<br>`javascript/src/aes_gcm_example.js:23`<br>`javascript/src/aes_gcm_example.js:41`<br>`javascript/src/aes_gcm_example.js:43`<br>`javascript/src/run_all.js:46` |
| `HMAC-SHA-256` | mac | N/A | Review key length for Grover resistance | First-Party Code (SAST/AST)<br>`python/hmac_example.py`<br>`python/hmac_example.py` |
| `AES-128` | other | 128 | Legacy bit-length (Recommend 256-bit upgrade) | First-Party Code (SAST/AST)<br>`python/gcp_kms_byok_cmk_example.py`<br>`python/aes_key_wrap_example.py`<br>`python/azure_keyvault_byok_cmk_example.py` |
| `HKDF-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py` |
| `PBKDF2-SHA-256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/pbkdf2_example.py` |
| `SHA-256` | hash | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/hmac_example.py`<br>`python/hmac_example.py`<br>`python/x25519_hkdf_example.py`<br>`python/hashing_example.py`<br>`python/pbkdf2_example.py`<br>`python/hmac_example.py:1`<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`python/rsa_oaep_pss_example.py:1`<br>`python/rsa_oaep_pss_example.py:14`<br>`python/rsa_oaep_pss_example.py:15`<br>`python/rsa_oaep_pss_example.py:22`<br>`python/rsa_oaep_pss_example.py:23`<br>`python/rsa_oaep_pss_example.py:36`<br>`python/rsa_oaep_pss_example.py:41`<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:16`<br>`python/hashing_example.py:1`<br>`python/hashing_example.py:6`<br>`python/hashing_example.py:7`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:22`<br>`python/gcp_kms_byok_cmk_example.py:56`<br>`python/gcp_kms_byok_cmk_example.py:57`<br>`python/gcp_kms_byok_cmk_example.py:81`<br>`python/gcp_kms_byok_cmk_example.py:82`<br>`python/azure_keyvault_byok_cmk_example.py:57`<br>`python/azure_keyvault_byok_cmk_example.py:58`<br>`python/azure_keyvault_byok_cmk_example.py:72`<br>`python/azure_keyvault_byok_cmk_example.py:73`<br>`python/azure_keyvault_byok_cmk_example.py:84`<br>`python/azure_keyvault_byok_cmk_example.py:85`<br>`python/azure_keyvault_byok_cmk_example.py:97`<br>`python/azure_keyvault_byok_cmk_example.py:98`<br>`java/src/main/java/org/example/crypto/HashingExample.java:9`<br>`java/src/main/java/org/example/crypto/HashingExample.java:10`<br>`java/src/main/java/org/example/crypto/HashingExample.java:14`<br>`java/src/main/java/org/example/crypto/HashingExample.java:15`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:22`<br>`java/src/main/java/org/example/crypto/RsaOaepPssExample.java:38`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:13`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:14`<br>`javascript/src/hybrid_kem_example.js:22`<br>`javascript/src/ml_kem_example.js:41`<br>`javascript/src/hmac_example.js:10`<br>`javascript/src/hashing.js:8`<br>`javascript/src/hashing.js:9`<br>`javascript/src/run_all.js:2`<br>`javascript/src/run_all.js:28` |
| `SHA-512` | hash | 512 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/ed25519_example.py`<br>`python/test_crypto.py`<br>`python/test_crypto.py`<br>`python/private_key_serialisation_example.py` |
| `TLS-1.3` | protocol | v1.3 | TLS 1.3 Transport (Enable hybrid X25519MLKEM768 via OpenSSL 3.5+) | First-Party Code (SAST/AST)<br>`python/ciphertrust_ekm_example.py:47` |
| `PBKDF2-HMAC-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/run_all.py:8`<br>`python/run_all.py:15`<br>`python/pbkdf2_example.py:1`<br>`python/pbkdf2_example.py:6`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:25`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:36`<br>`java/src/main/java/org/example/crypto/Pbkdf2Example.java:49`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:29`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:30` |
| `HMAC-SHA256` | mac | 256 | Quantum-Resistant (Grover's proof) | First-Party Code (SAST/AST)<br>`python/hmac_example.py:10`<br>`python/hmac_example.py:16`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:34`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:35`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:41`<br>`java/src/main/java/org/example/crypto/HmacExample.java:11`<br>`java/src/main/java/org/example/crypto/HmacExample.java:12`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:25`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:27`<br>`java/src/main/java/org/example/crypto/HybridX25519MlKemExample.java:30`<br>`javascript/src/hmac_example.js:10` |
| `HKDF-SHA256` | kdf | 256 | Quantum-Resistant KDF / Password Hashing (Grover-resistant) | First-Party Code (SAST/AST)<br>`python/x25519_hkdf_example.py:1`<br>`python/x25519_hkdf_example.py:5`<br>`python/x25519_hkdf_example.py:15`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:32`<br>`java/src/main/java/org/example/crypto/X25519HkdfExample.java:65`<br>`java/src/main/java/org/example/crypto/TestCrypto.java:69` |
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
