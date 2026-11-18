# PQC Upgrade Path Support & Blockers Report

**Last Verified:** 2026-11-18 | **Version:** `1.2.0`

## Purpose

This report documents what Post-Quantum Cryptography (PQC) upgrades can be achieved **today** in each language runtime in this repository, and **why** certain upgrade paths remain blocked without external C/native dependencies or newer runtime releases.

## Current vs. Future Support Dashboard

| Language / Runtime | Tested Version | Classical Asymmetric | ML-KEM-768 (FIPS 203) | Hybrid X25519 + ML-KEM-768 | ML-DSA-65 (FIPS 204) | SLH-DSA (FIPS 205) | Primary Blocker for Full Native Upgrade |
|---|---|---|---|---|---|---|---|
| **Java** | OpenJDK `25.0.4.1` | `X25519`, `Ed25519`, `RSA-3072` | 🟢 **Native** (JEP 496) | 🟢 **Native** (`X25519` + `ML-KEM-768`) | 🟢 **Native** (JEP 497) | 🔴 **Blocked** (Needs Bouncy Castle / external JCA) | Standard JCA lacks `SLH-DSA`; LTS runtimes `< JDK 24` lack `ML-KEM` and `ML-DSA` |
| **JavaScript (Node.js)** | Node.js `v22.23.2` | `X25519` (`node:crypto`) | 🟡 **Package** (`@noble/post-quantum`) | 🟡 **Package** (`node:crypto` + `@noble`) | 🟡 **Package** (`@noble/post-quantum`) | 🟡 **Package** (`@noble/post-quantum`) | `node:crypto` stdlib does not expose PQC primitives natively without OpenSSL 3.5+ / third-party JS |
| **Python** | Python `3.15.2` / `cryptography 50.0.0` | `X25519`, `Ed25519`, `RSA-3072` | 🔴 **Blocked** (No stdlib / PyCA API) | 🔴 **Blocked** | 🔴 **Blocked** | 🔴 **Blocked** | `cryptography.hazmat.primitives.asymmetric` (`50.0.0`) does not expose `ML-KEM`, `ML-DSA`, or `SLH-DSA` |
| **PowerShell (.NET)** | Not installed on host (`pwsh` missing) | `AesGcm` only in repo | 🔴 **Blocked** (Needs .NET 10+ & OS OpenSSL 3.5+) | 🔴 **Blocked** | 🔴 **Blocked** | 🔴 **Blocked** | Built-in `MLKem`/`MLDsa`/`SlhDsa` require .NET 10+ and underlying OS OpenSSL 3.5+ / CNG support |

## Why Full PQC Migration Cannot Be Achieved Everywhere Today

### 1. Python (`cryptography==50.0.0`)
- **Verified Gap:** Inspecting `cryptography.hazmat.primitives.asymmetric` in `cryptography 50.0.0` shows no `mlkem`, `mldsa`, or `slhdsa` modules.
- **Why It Cannot Be Achieved Natively:** PyCA `cryptography` delegates asymmetric primitives to its linked OpenSSL backend and has not yet exposed FIPS 203/204/205 APIs in the standard wheel.
- **Future Unlock Path:** Upgrade to a PyCA `cryptography` release built on OpenSSL 3.5+ once `mlkem`/`mldsa` bindings ship, or adopt `liboqs-python` in environments that allow native C/liboqs builds.

### 2. Java (OpenJDK 25 vs. LTS 17/21)
- **Verified Gap:** OpenJDK 25 natively supports `ML-KEM-768` and `ML-DSA-65`, but does not include a standard JCA provider for `SLH-DSA` (FIPS 205).
- **Why Older LTS Environments Are Blocked:** Production estates pinned to Java 17 or Java 21 LTS lack JEP 496 (`ML-KEM`) and JEP 497 (`ML-DSA`) entirely.
- **Future Unlock Path:** Upgrade runtimes to JDK 25+ for native `ML-KEM`/`ML-DSA`, and add Bouncy Castle (`BCPQC`) where `SLH-DSA` or JDK 17/21 compatibility is required.

### 3. JavaScript (Node.js 22)
- **Verified Gap:** Node.js `v22.23.2` `node:crypto` supports `X25519`, `HKDF`, and `AES-256-GCM`, but lacks built-in `ML-KEM`, `ML-DSA`, and `SLH-DSA`.
- **Workaround Used Here:** Pure-JS `@noble/post-quantum` provides FIPS 203/204/205 without native C addons, but adds a third-party dependency.
- **Future Unlock Path:** Native `node:crypto` support once Node.js LTS ships with OpenSSL 3.5+ PQC EVP bindings.

### 4. PowerShell (.NET)
- **Verified Gap:** The Linux host lacks `pwsh`, and .NET 8/9 LTS runtimes do not expose `MLKem`, `MLDsa`, or `SlhDsa` in `System.Security.Cryptography`.
- **Future Unlock Path:** .NET 10+ paired with OS-level OpenSSL 3.5+ (Linux) or PQC-enabled Windows CNG.
