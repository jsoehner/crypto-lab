# ADR-012: Sovereign eKMS Integration and Educational Observability

## Status
Accepted

## Context
Running `crypto-lab` standalone validates cryptographic primitives and cloud BYOK/CMK patterns using in-memory simulators, but teams adopting External Key Management (eKMS) also need live protocol verification (X.509 v3 mTLS, Bearer JWT, versioned key rotation, and instant kill-switch revocation) and clear, accessible output explaining *why* each control treats a real threat.

## Decision
1. **Optional Live Dependency (`ctm-ekm-lab`)**: Keep `crypto-lab` runnable offline by default, while automatically detecting `CIPHERTRUST_URL` at runtime in `demo_langs.sh`, `demo_langs.ps1`, and `python/test_ctm_integration.py` to unlock 8 live mTLS integration tests (21 Python tests total).
2. **Explicit CTM Availability Reporting**: Print a prominent `[CTM STATUS] AVAILABLE / UNREACHABLE / NOT AVAILABLE` banner so operators and learners immediately know whether tests executed against a live control plane or the offline simulator.
3. **Educational `[PROBLEM]` / `[WHAT]` / `[WHY]` Output**: Standardize color-coded threat narration (`python/edu_output.py`, `demo_langs.sh`) across all demos and Python tests (respecting `NO_COLOR`).

## Consequences
- Offline CI remains fast and credential-free (`13` passed, `8` skipped).
- Live `ctm-ekm-lab` runs verify end-to-end mTLS, JWT auth, key rotation (`v1 -> v2`), multi-tenant isolation, and instant deactivation/reactivation (`21/21` passed).
