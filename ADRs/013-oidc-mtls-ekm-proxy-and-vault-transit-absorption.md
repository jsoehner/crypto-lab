# ADR-013: Absorption of OIDC + mTLS Vault Transit EKM Proxy (`ekm-demo`)

## Status
Accepted

## Context
The standalone `ekm-demo` repository demonstrated a three-layer External Key Manager (EKM) proxy combining Keycloak OIDC JWT validation (Layer 7), mTLS transport to HashiCorp Vault (Layer 4), and Vault Transit KEK operations (Layer 1). Maintaining it as a third separate repository fragmented EKM documentation and duplicated SBOM/CBOM tooling.

## Decision
Absorb `ekm-demo` into the two-repository staged architecture:
1. **`ctm-ekm-lab` (Infrastructure & Control Plane)**: Houses `vault-oidc-proxy/proxy.py`, `config/vault.hcl`, `scripts/generate_vault_oidc_certs.sh`, `docker-compose.vault-oidc.yml`, and `docs/vault-oidc-ekm-guide.md`.
2. **`crypto-lab` (Client Patterns & Tests)**: Houses [vault_ekm_proxy_example.py](../python/vault_ekm_proxy_example.py) and `test_vault_oidc_ekm_proxy_and_rate_limit` in [test_cloud_kms.py](../python/test_cloud_kms.py).
3. Retire and remove the standalone `jsoehner/ekm-demo` repository.

## Consequences
- All cryptographic client patterns and tests live in `crypto-lab`; all deployable EKM control-plane stacks (CipherTrust CE and Vault+OIDC) live in `ctm-ekm-lab`.
