# ADR-011: Cloud HSM BYOK/CMK and External Key Management (EKM/HYOK) Control

## Status
Accepted

## Context
Cloud workloads require clear reference patterns for Customer-Managed Keys (CMK) and Bring Your Own Key (BYOK) in Azure Key Vault / Managed HSM and GCP Cloud KMS / Cloud HSM without an External Key Management (EKM) platform, as well as the most mature sovereign control pattern using an external KMS (EKM / Hold Your Own Key).

## Decision
1. **Azure Key Vault / Managed HSM (BYOK + CMK, no EKM)**:
   - Wrap on-premises key material with the HSM RSA-OAEP-256 KEK + AES-256-KWP (`CKM_RSA_AES_KEY_WRAP`) before import.
   - Use envelope encryption: generate a local AES-256-GCM DEK and wrap/unwrap it via `CryptographyClient.wrap_key("RSA-OAEP-256", ...)`.
   - Reference: [azure_keyvault_byok_cmk_example.py](../python/azure_keyvault_byok_cmk_example.py).
2. **GCP Cloud KMS / Cloud HSM (BYOK + CMK, no EKM)**:
   - Wrap on-premises key material with the ImportJob public key (`RSA-OAEP-3072-SHA256` + AES-256-KWP).
   - Wrap/unwrap local AES-256-GCM DEKs via `KeyManagementServiceClient.encrypt/decrypt` with Additional Authenticated Data (AAD).
   - Reference: [gcp_kms_byok_cmk_example.py](../python/gcp_kms_byok_cmk_example.py).
3. **External Key Management (EKM / HYOK — Mature Sovereign Control)**:
   - Keep root KEKs exclusively inside the external KMS/HSM (`ekm://...`).
   - Enforce caller allowlists, mandatory access justification (bound as AAD), immutable audit logs, and an instant cryptographic kill-switch (`disable_key` / `destroy_key`).
   - Reference: [external_kms_ekm_example.py](../python/external_kms_ekm_example.py).

## Consequences
- Offline unit tests use faithful in-memory HSM/KMS simulators (`SimulatedAzureManagedHsm`, `SimulatedGcpCloudHsm`, `ExternalKmsControlPlane`) so CI runs without cloud credentials while preserving exact cryptographic wrapping formats and protocol boundaries.
