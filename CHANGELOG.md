# Changelog

All notable changes to this project are documented in this file.

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
