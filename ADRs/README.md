# Architectural Decision Records (ADRs)

Master decision log for `crypto-lab` (`v2.0.0`).

| ADR | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| [ADR-001](001-cryptographic-standards.md) | Cryptographic Standards | Accepted | Baseline symmetric/asymmetric/KDF standards |
| [ADR-002](002-authenticated-encryption-aes-gcm.md) | Authenticated Encryption (AES-GCM) | Accepted | AES-256-GCM, 96-bit CSPRNG nonce + AAD |
| [ADR-003](003-password-hashing-pbkdf2.md) | Password Hashing (PBKDF2) | Accepted | PBKDF2-HMAC-SHA-256 |
| [ADR-004](004-key-agreement-x25519-hkdf.md) | Key Agreement (X25519 + HKDF) | Accepted | Classical ECDH + HKDF-SHA-256 |
| [ADR-005](005-asymmetric-cryptography-rsa-oaep-pss.md) | Asymmetric Cryptography (RSA-OAEP / PSS) | Accepted | RSA-3072 OAEP-SHA256 / PSS |
| [ADR-006](006-digital-signatures-ed25519.md) | Digital Signatures (Ed25519) | Accepted | Classical EdDSA signatures |
| [ADR-007](007-message-authentication-hmac.md) | Message Authentication (HMAC) | Accepted | HMAC-SHA-256 constant-time verification |
| [ADR-008](008-key-wrapping-and-serialization.md) | Key Wrapping & Serialization | Accepted | RFC 3394 AES Key Wrap & encrypted PKCS#8 |
| [ADR-009](009-automated-sbom-cbom-supply-chain-governance.md) | Automated SBOM & CBOM Supply Chain Governance | Partially Superseded | Inline CI steps superseded by [ADR-014](014-three-stage-sovereign-ekm-and-unified-governance.md) |
| [ADR-010](010-post-quantum-cryptography-ml-kem-ml-dsa.md) | Post-Quantum Cryptography (ML-KEM-768 & ML-DSA-65) | Accepted | NIST FIPS 203, 204 & 205 adoption |
| [ADR-011](011-cloud-hsm-byok-cmk-and-ekm-control.md) | Cloud HSM BYOK/CMK & External KMS (EKM/HYOK) Control | Accepted | Azure Managed HSM, GCP Cloud KMS & Sovereign EKM |
| [ADR-012](012-sovereign-ekm-integration-and-educational-observability.md) | Sovereign eKMS Integration & Educational Observability | Accepted | Live `ctm-ekm-lab` integration & `[PROBLEM]/[WHAT]/[WHY]` telemetry |
| [ADR-013](013-oidc-mtls-ekm-proxy-and-vault-transit-absorption.md) | Absorption of OIDC + mTLS Vault Transit EKM Proxy (`ekm-demo`) | Accepted | Stage 2 OIDC + mTLS + Vault Transit pattern |
| [ADR-014](014-three-stage-sovereign-ekm-and-unified-governance.md) | Three-Stage Sovereign EKM Architecture, Unified `jsi-bom-actions` Governance & Automated Verification | Accepted | `v2.0.0` milestone; supersedes inline CI in [ADR-009](009-automated-sbom-cbom-supply-chain-governance.md) |
