# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added
- **Interactive `ctm-ekm-lab` Auto-Activation (`demo_langs.sh`):** Automatically detects a sibling `../ctm-ekm-lab` (or `$CTM_EKM_LAB_DIR`) checkout when `CIPHERTRUST_URL` is unset, prompts to start the local HTTPS + X.509 v3 mTLS mock server (`CM_REQUIRE_MTLS=true`), bootstraps `.env.ciphertrust` if needed, executes live EKM demos, and tears down the background process cleanly via `trap EXIT`.

## [2.0.0] - 2026-11-20

### Architecture & Major Changes
- **Major Version Bump (`v2.0.0`):** Reflects the unified **Three-Stage Sovereign EKM & Multi-Language PQC Architecture** spanning local CipherTrust eKMS (Stage 1), OIDC + mTLS Vault Transit EKM Proxy (Stage 2), Multi-Cloud EKM Cascade (Stage 3), and NIST FIPS 203/204/205 PQC across Python 3.15, Java 25, and Node.js 22.
- **Updated Architecture Infographic:** Replaced `docs/assets/ekms-control-plane-infographic.jpg` with the `v2.0.0` Three-Stage Sovereign EKM & PQC blueprint infographic.

### Governance, Decisions & Verification
- **ADR-014 & Master ADR Index:** Added [ADRs/014-three-stage-sovereign-ekm-and-unified-governance.md](ADRs/014-three-stage-sovereign-ekm-and-unified-governance.md) (superseding inline CI workflow details in ADR-009 with SHA-pinned `jsoehner/jsi-bom-actions@v1.1.1`) and [ADRs/README.md](ADRs/README.md).
- **CI & Runtime Upgrades:** Standardized on `jsoehner/jsi-bom-actions@v1.1.1`, `actions/setup-node@v7`, `actions/setup-python@v7`, and `actions/setup-java@v6` via Dependabot.
- **Functional Verification:** Verified end-to-end across Python 3.15 (15 offline + 8 live `ctm-ekm-lab` mTLS tests = 23/23), Java 25 (11 examples + `TestCrypto`), and Node.js 22 (8/8 tests + demo) by **Jeffs' Automated build and deploy agent** ([docs/BUILD_VERIFICATION.md](docs/BUILD_VERIFICATION.md)).

## [1.6.0] - 2026-11-18

### Added
- **OIDC + mTLS Vault Transit EKM Proxy (`python/vault_ekm_proxy_example.py`)**: Absorbed the Layer-7 OIDC JWT + Layer-4 mTLS + Layer-1 Vault Transit pattern from the retired `ekm-demo` project, with offline simulator and unit tests in `python/test_cloud_kms.py`.
- **ADR-013**: Documented the absorption of `ekm-demo` across `crypto-lab` and `ctm-ekm-lab` in `ADRs/013-oidc-mtls-ekm-proxy-and-vault-transit-absorption.md`.

## [1.5.0] - 2026-11-18

### Added
- **Live `ctm-ekm-lab` Integration Suite (`python/test_ctm_integration.py`)**: Added 8 live mTLS integration tests (key provisioning/metadata, live envelope round-trip, AAD/tamper rejection, kill-switch deactivate/reactivate, versioned key rotation `v1 -> v2`, multi-tenant isolation, auth rejection, and missing mTLS client cert rejection).
- **Educational `[PROBLEM]` / `[WHAT]` / `[WHY]` Telemetry**: Added `python/edu_output.py` and color-coded threat narration + `[CTM STATUS]` availability banners to `demo_langs.sh`, `demo_langs.ps1`, and all Python test suites.
- **ADR-012 & Milestone Infographic**: Added `ADRs/012-sovereign-ekm-integration-and-educational-observability.md` and updated the Sovereign eKMS infographic across `crypto-lab` and `ctm-ekm-lab`.

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
