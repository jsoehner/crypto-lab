# ADR-014: Three-Stage Sovereign EKM Architecture, Unified `jsi-bom-actions` Governance & Automated Verification

## Metadata

| Field | Value |
|---|---|
| ADR ID | ADR-014 |
| Status | Accepted |
| Created Date | 2026-11-20 |
| Decision Date | 2026-11-20 |
| Effective Date | 2026-11-20 |
| Architecture Domain | Cryptography / Sovereign EKM / Supply Chain Governance |
| Scope | `crypto-lab` (`v2.0.0`) & companion `ctm-ekm-lab` (`v2.0.0`) |
| Supersedes | Inline CI workflow mechanics in [ADR-009](009-automated-sbom-cbom-supply-chain-governance.md) |

---

## Context

Between `v1.1.0` and `v1.6.0`, `crypto-lab` expanded from standalone classical cryptographic snippets into a multi-language **Three-Stage Sovereign EKM & Post-Quantum Cryptography (PQC)** platform:
1. **Stage 1 (Sovereign eKMS Control Plane):** CipherTrust Manager CE REST client (`python/ciphertrust_ekm_example.py`) with 8 live X.509 v3 mTLS + JWT integration tests against `ctm-ekm-lab` (`python/test_ctm_integration.py`).
2. **Stage 2 (OIDC + mTLS Vault Transit EKM Proxy):** Absorbed `ekm-demo` Layer-7 OIDC + Layer-4 mTLS + Layer-1 Vault Transit pattern (`python/vault_ekm_proxy_example.py`).
3. **Stage 3 (Multi-Cloud Sovereign EKM Cascade):** Cross-cloud external KEK hierarchy spanning Azure CCKM / Managed HSM and GCP Cloud EKM / Cloud KMS (`python/stage3_multi_cloud_ekm_orchestration.py`, `docs/security/THREE_STAGE_EKM_WORKFLOW.md`).
4. **Multi-Language PQC:** Native Java 25 JEP 496/497 (`ML-KEM-768`, `ML-DSA-65`, Hybrid X25519), Node.js 22 `@noble/post-quantum` (`ML-KEM-768`, `ML-DSA-65`, `SLH-DSA`), and Python 3.15 (`cryptography 50.0.2`).

Simultaneously, maintaining inline Anchore/cbomkit CI steps from ADR-009 across repositories caused SHA-pinning and PQC-scoring drift, and multi-runtime verification needed a standardized split-horizon Trusted OSS + automated build verification gate.

---

## Alternatives Considered

| Option | Pros | Cons | Disposition |
|---|---|---|---|
| **Option 1: Keep `v1.x` minor releases & inline ADR-009 workflow** | No major version bump. | Obscures the major architectural shift to Three-Stage Sovereign EKM; continues inline CI drift. | **Rejected** |
| **Option 2: Major `v2.0.0` Architecture Baseline + Unified `jsi-bom-actions@v1.1.1` + Split-Horizon Trusted OSS Verification (Selected)** | Clearly signals the Three-Stage Sovereign EKM + PQC architecture; consolidates SBOM/CBOM/PQC CI into SHA-pinned `jsoehner/jsi-bom-actions@v1.1.1`; enforces repeatable Python 3.15 / Java 25 / Node.js 22 + live mTLS verification. | Introduces versioned dependency on `jsoehner/jsi-bom-actions` (mitigated via immutable commit SHA pinning & Dependabot). | **Selected** |

---

## Decision

1. **Major Release Baseline (`v2.0.0`):** Bump `crypto-lab` and companion `ctm-ekm-lab` to `v2.0.0` to reflect the unified Three-Stage Sovereign EKM & Multi-Language PQC architecture.
2. **Unified `jsi-bom-actions` CI Governance:** Supersede the inline multi-step SBOM/CBOM workflow in [ADR-009](009-automated-sbom-cbom-supply-chain-governance.md) with SHA-pinned `jsoehner/jsi-bom-actions@v1.1.1` in `.github/workflows/sbom-cbom.yml` plus automated Dependabot updates (`actions/setup-node@v7`, `actions/setup-python@v7`, `actions/setup-java@v6`).
3. **Split-Horizon Trusted OSS & Automated Verification:** Enforce local LAN PyPI caching (`http://oss.jsigroup.local:8080/pypi/virtual/simple`) with `.git/info/exclude` hygiene and record repeatable verification across Python 3.15, Java 25, Node.js 22, and live `ctm-ekm-lab` mTLS integration in `docs/BUILD_VERIFICATION.md` via **Jeffs' Automated build and deploy agent**.

---

## Consequences

- **Positive:** Single source of truth for Three-Stage EKM architecture, PQC readiness, and supply-chain governance across both paired repositories (`crypto-lab` and `ctm-ekm-lab`), with 100% verified offline and live mTLS test evidence.
- **Trade-offs:** Downstream consumers referencing `v1.x` tags should review `CHANGELOG.md` and `docs/security/THREE_STAGE_EKM_WORKFLOW.md` when adopting Stage 2/3 EKM modules.
