# Three-Stage Sovereign EKM & PQC Workflow Architecture

This document visualizes the complete multi-stage cryptographic architecture across **`crypto-lab`** and **`ctm-ekm-lab`**, from standalone Cloud HSM BYOK/CMK (Stage 1) to Sovereign External KMS & OIDC/Vault Proxy (Stage 2) and Multi-Cloud Root-of-Trust Cascade Orchestration (Stage 3).

---

## 1. End-to-End Multi-Stage Architecture (`flowchart TB`)

```mermaid
flowchart TB
    %% Styling
    classDef stage1 fill:#1E293B,stroke:#38BDF8,stroke-width:2px,color:#F8FAFC
    classDef stage2 fill:#1E293B,stroke:#10B981,stroke-width:2px,color:#F8FAFC
    classDef stage3 fill:#1E293B,stroke:#F59E0B,stroke-width:2px,color:#F8FAFC
    classDef pqc fill:#31102F,stroke:#E879F9,stroke-width:2px,color:#F8FAFC
    classDef gate fill:#450A0A,stroke:#EF4444,stroke-width:2px,color:#FEF2F2

    subgraph S1["Stage 1: Cloud HSM BYOK & CMK (No External EKM)"]
        ONPREM["On-Premises Key Material (256-bit)"]
        BYOKWRAP["BYOK Wrapper (RSA-OAEP + AES-256-KWP)"]
        AZHSM["Azure Managed HSM / Key Vault"]
        GCPKMS["GCP Cloud KMS / Cloud HSM"]
        S1DEK["Local AES-256-GCM DEK + AAD"]
        ONPREM --> BYOKWRAP
        BYOKWRAP -->|"ImportKey"| AZHSM
        BYOKWRAP -->|"ImportJob"| GCPKMS
        AZHSM -->|"Wrap/Unwrap DEK"| S1DEK
        GCPKMS -->|"Encrypt/Decrypt DEK"| S1DEK
    end

    subgraph S2["Stage 2: Sovereign eKMS & Vault+OIDC Proxy (ctm-ekm-lab)"]
        direction TB
        KC["Keycloak OIDC (Layer 7 JWKS)"]
        PROXY["EKM-Proxy (Rate Limit 429, Headers, Log Masking)"]
        VAULT["HashiCorp Vault Transit (Layer 4 mTLS)"]
        CTM["CipherTrust Manager CE / Lab Server (X.509 v3 mTLS + JWT)"]
        CTMOPS["Lifecycle: Rotate v1->v2 | Multi-Tenant | Kill-Switch 403"]

        KC -->|"1. Validate Bearer JWT"| PROXY
        PROXY -->|"2. mTLS Client Cert Auth"| VAULT
        CTM --- CTMOPS
    end

    subgraph S3["Stage 3: Multi-Cloud Root-of-Trust Cascade (crypto-lab)"]
        ROOTKEK["Sovereign Root KEK (Never Leaves CTM)"]
        SVC_V["Service KEK: vault-transit"]
        SVC_A["Service KEK: azure-keyvault"]
        SVC_G["Service KEK: gcp-cloud-kms / SaaS"]
        APPDEK["Application AES-256-GCM DEK"]

        ROOTKEK -->|"Wraps Service KEK"| SVC_V
        ROOTKEK -->|"Wraps Service KEK"| SVC_A
        ROOTKEK -->|"Wraps Service KEK"| SVC_G
        SVC_V -->|"Wraps DEK"| APPDEK
        SVC_A -->|"Wraps DEK"| APPDEK
        SVC_G -->|"Wraps DEK"| APPDEK
    end

    subgraph PQC["PQC & Governance Layer (crypto-lab)"]
        PQCMODS["ML-KEM-768 (FIPS 203) | Hybrid X25519+ML-KEM | ML-DSA-65 | SLH-DSA"]
        CBOM["AST Crypto Scanner + CBOM Scorecard (23 Python + Java 25 + JS Tests)"]
        EDU["Telemetry: [CTM STATUS] + [PROBLEM] / [WHAT] / [WHY]"]
    end

    KILL["Kill-Switch: Deactivate Root KEK -> HTTP 403 Cascade"]

    CTM -->|"Anchors Root of Trust"| ROOTKEK
    ROOTKEK -.->|"Instant Revocation"| KILL
    KILL -.->|"Blocks Unwrap Across All Clouds"| S3
    PQCMODS --- CBOM
    CBOM --- EDU

    class ONPREM,BYOKWRAP,AZHSM,GCPKMS,S1DEK stage1
    class KC,PROXY,VAULT,CTM,CTMOPS stage2
    class ROOTKEK,SVC_V,SVC_A,SVC_G,APPDEK stage3
    class PQCMODS,CBOM,EDU pqc
    class KILL gate
```

---

## 2. Runtime Cryptographic & Policy Sequence (`sequenceDiagram`)

```mermaid
sequenceDiagram
    autonumber
    participant App as Application (crypto-lab)
    participant IdP as Keycloak OIDC (Layer 7)
    participant Proxy as EKM-Proxy (Rate Limit + mTLS)
    participant Vault as Vault Transit (Layer 4)
    participant CTM as Sovereign CTM (ctm-ekm-lab)
    participant Cloud as Azure / GCP / SaaS Vault

    Note over App,Cloud: Happy Path: Stage 2 + Stage 3 Multi-Cloud Encryption
    App->>IdP: Request OIDC Access Token (client/user)
    IdP-->>App: Signed RS256 Bearer JWT
    App->>CTM: POST /api/v1/vault/keys2 (X.509 v3 mTLS + JWT)
    CTM-->>App: 201 Created (sovereign-root-kek, version=1)

    App->>CTM: Wrap Service KEKs (aad="vault-transit" / "azure-keyvault" / "gcp-cloud-kms")
    CTM-->>App: Wrapped Service KEKs (v1)

    App->>Proxy: POST /unwrap-key (Bearer JWT + wrapped DEK)
    Proxy->>IdP: Verify JWT signature via JWKS
    Proxy->>Proxy: Enforce 429 Rate Limit & Mask Logs
    Proxy->>Vault: POST /v1/transit/decrypt (mTLS Client Cert)
    Vault-->>Proxy: Plaintext DEK
    Proxy-->>App: 200 OK (Plaintext DEK)
    App->>App: Encrypt/Decrypt Payload Locally (AES-256-GCM + AAD)

    Note over App,Cloud: Incident Response: Stage 3 Sovereign Kill-Switch
    CTM->>CTM: POST /api/v1/vault/keys2/sovereign-root-kek/deactivate
    App->>CTM: Attempt Unwrap for Vault / Azure / GCP Service KEK
    CTM-->>App: 403 Forbidden (Key Deactivated — Cascade Blocks All Clouds)

    Note over App,Cloud: Recovery & Rotation
    CTM->>CTM: POST .../reactivate & POST .../rotate (version=2)
    App->>CTM: Unwrap v1 envelope OR Wrap new data under v2
    CTM-->>App: 200 OK (Zero-Downtime Continuity)
```

---

## 3. Sovereign KEK State Lifecycle (`stateDiagram-v2`)

```mermaid
stateDiagram-v2
    [*] --> Active_v1: POST /api/v1/vault/keys2 (AES-256)
    Active_v1 --> Rotated_v2: POST .../rotate (New wraps use v2; v1 decrypts)
    Active_v1 --> Deactivated: POST .../deactivate (Kill-Switch -> HTTP 403)
    Rotated_v2 --> Deactivated: POST .../deactivate (Kill-Switch -> HTTP 403)
    Deactivated --> Active_v1: POST .../reactivate (Restores access)
    Deactivated --> Destroyed: destroy_key() (Zeroized — Permanent)
    Destroyed --> [*]
```
