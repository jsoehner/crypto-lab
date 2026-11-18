# Changelog

All notable changes to this project are documented in this file.

## [1.4.0] - 2026-11-18

### Added
- **CipherTrust Manager CE REST Client (`python/ciphertrust_ekm_example.py`)**: Added a CipherTrust Manager REST API (`/api/v1/auth/tokens`, `/api/v1/vault/keys2`, `/api/v1/crypto/{encrypt,decrypt}`) envelope-encryption client supporting live `CIPHERTRUST_URL` + mTLS and an offline protocol simulator, with unit tests in `python/test_cloud_kms.py`.

## [1.3.0] - 2026-11-18

### Added
- **Azure Key Vault / Managed HSM (BYOK & CMK)**: Added `python/azure_keyvault_byok_cmk_example.py` demonstrating RSA-OAEP-256 + AES-256-KWP BYOK wrapping and CMK envelope encryption without an EKM platform.
- **GCP Cloud KMS / Cloud HSM (BYOK & CMK)**: Added `python/gcp_kms_byok_cmk_example.py` demonstrating ImportJob BYOK wrapping and Cloud HSM CMK envelope encryption with AAD.
- **External KMS (EKM / HYOK) Control Plane**: Added `python/external_kms_ekm_example.py` demonstrating sovereign remote wrap/unwrap, caller allowlists, justification AAD binding, immutable audit logging, and an instant cryptographic kill-switch (`disable_key` / `destroy_key`).
- **Cloud KMS Unit Tests & ADR-011**: Added `python/test_cloud_kms.py` and `ADRs/011-cloud-hsm-byok-cmk-and-ekm-control.md`.

## [1.2.0] - 2026-11-18

### Added
- **Hybrid PQC Key Agreement**: Added `HybridX25519MlKemExample.java` (Java 25) and `javascript/src/hybrid_kem_example.js` (Node.js 22) combining classical `X25519` with `ML-KEM-768` via `HKDF-SHA-256` and `AES-256-GCM`.
- **PQC KEM-DEM Encryption (Replaces RSA-OAEP)**: Added `encryptWithKem`/`decryptWithKem` to `MlKemExample.java` and `javascript/src/ml_kem_example.js`.
- **SLH-DSA (NIST FIPS 205)**: Added `javascript/src/slh_dsa_example.js` for stateless hash-based signatures (`slh_dsa_sha2_128f`).
- **PQC Migration Assessment**: Added `docs/security/PQC_MIGRATION_ASSESSMENT.md` mapping every classical function in the repository to its quantum-resistant equivalent.

## [1.1.0] - 2026-11-18

### Added
- **JavaScript / Node.js Reference Suite (`javascript/`)**: Added an ESM Node.js 22+ package implementing SHA-256, HMAC-SHA-256, AES-256-GCM, NIST FIPS 203 `ML-KEM-768` + HKDF-SHA-256, and NIST FIPS 204 `ML-DSA-65` (via `@noble/post-quantum`), with `node:test` unit tests.
- **Java 25 Post-Quantum Examples**: Added `MlKemExample.java` (FIPS 203 `ML-KEM-768`) and `MlDsaExample.java` (FIPS 204 `ML-DSA-65`) using standard JDK 25 JCA/JCE providers.
- **Multi-Language CI Workflow**: Added `.github/workflows/ci-tests.yml` to run Python, Java 25, and Node.js test suites on pushes and pull requests.
- **ADR-010**: Documented the adoption of ML-KEM-768 and ML-DSA-65 in `ADRs/010-post-quantum-cryptography-ml-kem-ml-dsa.md`.
- **Versioning**: Added `VERSION` (`1.1.0`) and `CHANGELOG.md`.

### Changed
- **Python Dependency**: Bumped `cryptography>=44.0.1` in `python/requirements.txt` per `SECURITY_AUDIT.md`.
- **Test Coverage**: Expanded `python/test_crypto.py` and `TestCrypto.java` with negative tamper/wrong-AAD assertions, fixed `TestCrypto.java` HMAC byte-array concatenation, and replaced `assert` with `CryptoSupport.require(...)` so checks execute without `-ea`.
- **Demo Runners**: Updated `demo_langs.sh` and `demo_langs.ps1` to support `python`, `java`, `javascript`, `powershell`, `both`, and `all`.
- **CI Hardening**: Updated `.github/workflows/security-testing.yml` path filters (`python/**`, `java/**`, `javascript/**`, `powershell/**`) and `.github/workflows/adr-gatekeeper.yml` to pass PR/commit context dynamically.
- **Documentation**: Rewrote `README.md` and `CONTRIBUTING.md` to match the repository's actual languages, commands, and PQC adoption workflow.
