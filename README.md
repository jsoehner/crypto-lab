# Secure Crypto Reference Examples

Vetted classical and post-quantum (PQC) cryptographic reference implementations in **Python**, **Java 25**, **JavaScript (Node.js 22)**, and **PowerShell**, paired with Architectural Decision Records (ADRs) and an automated SBOM/CBOM supply-chain pipeline.

**Version:** `1.1.0` (see [CHANGELOG.md](CHANGELOG.md))

## Why This Project Exists

Teams migrating to modern cryptography face two recurring problems:
1. **Misconfigured classical primitives** (reused nonces, missing AAD, non-constant-time tag checks, or weak KDFs).
2. **Quantum migration blind spots** ("Harvest Now, Decrypt Later" exposure on RSA, X25519, and Ed25519 without visibility into where those primitives live).

This repository serves as a hands-on reference exercise. It shows how to implement each primitive safely, test both happy paths and tamper rejection, and audit the resulting codebase with automated Software and Cryptographic Bills of Materials (SBOM & CBOM).

## Supported Primitives & PQC Readiness

| Category | Primitive / Standard | Quantum Status | Python | Java 25 | JavaScript (Node.js) | PowerShell |
|---|---|---|---|---|---|---|
| **PQC Key Encapsulation** | **ML-KEM-768** (NIST FIPS 203) | Post-Quantum Ready | — | [MlKemExample.java](java/src/main/java/org/example/crypto/MlKemExample.java) | [ml_kem_example.js](javascript/src/ml_kem_example.js) | — |
| **PQC Digital Signatures** | **ML-DSA-65** (NIST FIPS 204) | Post-Quantum Ready | — | [MlDsaExample.java](java/src/main/java/org/example/crypto/MlDsaExample.java) | [ml_dsa_example.js](javascript/src/ml_dsa_example.js) | — |
| **Authenticated Encryption** | **AES-256-GCM** (96-bit CSPRNG nonce + AAD) | Grover-Resistant (256-bit) | [aes_gcm_example.py](python/aes_gcm_example.py) | [AesGcmExample.java](java/src/main/java/org/example/crypto/AesGcmExample.java) | [aes_gcm_example.js](javascript/src/aes_gcm_example.js) | [AesGcmExample.ps1](powershell/AesGcmExample.ps1) |
| **Hashing & MAC** | **SHA-256**, **HMAC-SHA-256** | Grover-Resistant | [hashing_example.py](python/hashing_example.py), [hmac_example.py](python/hmac_example.py) | [HashingExample.java](java/src/main/java/org/example/crypto/HashingExample.java), [HmacExample.java](java/src/main/java/org/example/crypto/HmacExample.java) | [hashing.js](javascript/src/hashing.js), [hmac_example.js](javascript/src/hmac_example.js) | — |
| **Password KDF** | **PBKDF2-HMAC-SHA-256** | Grover-Resistant | [pbkdf2_example.py](python/pbkdf2_example.py) | [Pbkdf2Example.java](java/src/main/java/org/example/crypto/Pbkdf2Example.java) | — | — |
| **Key Wrapping & Storage** | **AES Key Wrap (RFC 3394)**, Encrypted PKCS#8 PEM | Grover-Resistant | [aes_key_wrap_example.py](python/aes_key_wrap_example.py), [private_key_serialisation_example.py](python/private_key_serialisation_example.py) | [AesKeyWrapExample.java](java/src/main/java/org/example/crypto/AesKeyWrapExample.java) | — | — |
| **Classical Asymmetric** | **X25519+HKDF**, **Ed25519**, **RSA-3072 OAEP/PSS** | Quantum-Vulnerable (Migration Target) | [x25519_hkdf_example.py](python/x25519_hkdf_example.py), [ed25519_example.py](python/ed25519_example.py), [rsa_oaep_pss_example.py](python/rsa_oaep_pss_example.py) | [X25519HkdfExample.java](java/src/main/java/org/example/crypto/X25519HkdfExample.java), [Ed25519Example.java](java/src/main/java/org/example/crypto/Ed25519Example.java), [RsaOaepPssExample.java](java/src/main/java/org/example/crypto/RsaOaepPssExample.java) | — | — |

## Quickstart

### Prerequisites
- **Python 3.10+**: `pip install -r python/requirements.txt`
- **Java 25+** (OpenJDK 24+ required for built-in `ML-KEM` and `ML-DSA` JCA providers)
- **Node.js 22+**: `cd javascript && npm install`
- **PowerShell 7+** (`pwsh`, optional for `powershell/AesGcmExample.ps1`)

### Run Interactive Demos

```bash
# Bash (prompts for python, java, javascript, powershell, both, or all — or pass as an argument)
./demo_langs.sh all
```

```powershell
# PowerShell
.\demo_langs.ps1 -Choice all
```

### Run Test Suites

```bash
# Python unit tests (positive + tamper/wrong-AAD/wrong-password checks)
python3 -m unittest discover -s python -p 'test_*.py' -v

# Java examples + assertions (CryptoSupport.require + -ea)
./java/run_all.sh
java -ea -cp java/out org.example.crypto.TestCrypto

# JavaScript unit tests (AES-GCM, SHA-256, HMAC, ML-KEM-768, ML-DSA-65)
npm --prefix javascript test
```

## How to Adopt These Patterns

1. **Start from the ADR**: Read the decision record in [ADRs/](ADRs/) for the primitive you need before copying code. Each ADR explains key sizes, nonces, padding, and tradeoffs.
2. **Use 256-bit symmetric keys and SHA-256+**: AES-256-GCM and SHA-256 retain 128-bit security against Grover's algorithm. Generate a fresh 96-bit CSPRNG nonce per encryption and bind context via Additional Authenticated Data (AAD).
3. **Plan PQC migration with FIPS 203 & 204**:
   - Replace or hybridize `X25519` / `RSA-OAEP` key exchange with **ML-KEM-768** + **HKDF-SHA-256** ([MlKemExample.java](java/src/main/java/org/example/crypto/MlKemExample.java), [ml_kem_example.js](javascript/src/ml_kem_example.js)).
   - Replace `Ed25519` / `RSA-PSS` signatures with **ML-DSA-65** ([MlDsaExample.java](java/src/main/java/org/example/crypto/MlDsaExample.java), [ml_dsa_example.js](javascript/src/ml_dsa_example.js)).
4. **Verify failure modes**: Every wrapper should reject tampered ciphertexts, mismatched AAD, and invalid signatures in constant time.

## Automated SBOM, CBOM & PQC Audit Pipeline

This repository tracks component and cryptographic inventory in CI ([.github/workflows/sbom-cbom.yml](.github/workflows/sbom-cbom.yml)) and publishes the latest assessment to [docs/security/CRYPTOGRAPHIC_AUDIT.md](docs/security/CRYPTOGRAPHIC_AUDIT.md).

### Run the Audit Locally

```bash
# Generate SBOM, CBOM, and AST cryptographic scan results into oss/
bash scripts/generate_boms.sh -t dir -o oss .

# Validate generated BOM schemas and coverage
bash scripts/test_boms.sh oss

# Generate the PQC readiness markdown summary
python3 scripts/analyze_cbom.py oss/cbom.json --sbom oss/sbom.cyclonedx.json --markdown oss/crypto-summary.md
```

### Architectural Decision Records

- [ADR-001: Cryptographic Standards](ADRs/001-cryptographic-standards.md)
- [ADR-002: Authenticated Encryption (AES-GCM)](ADRs/002-authenticated-encryption-aes-gcm.md)
- [ADR-003: Password Hashing (PBKDF2)](ADRs/003-password-hashing-pbkdf2.md)
- [ADR-004: Key Agreement (X25519 + HKDF)](ADRs/004-key-agreement-x25519-hkdf.md)
- [ADR-005: Asymmetric Cryptography (RSA-OAEP / PSS)](ADRs/005-asymmetric-cryptography-rsa-oaep-pss.md)
- [ADR-006: Digital Signatures (Ed25519)](ADRs/006-digital-signatures-ed25519.md)
- [ADR-007: Message Authentication (HMAC)](ADRs/007-message-authentication-hmac.md)
- [ADR-008: Key Wrapping & Serialization](ADRs/008-key-wrapping-and-serialization.md)
- [ADR-009: Automated SBOM & CBOM Governance](ADRs/009-automated-sbom-cbom-supply-chain-governance.md)
- [ADR-010: Post-Quantum Cryptography (ML-KEM-768 & ML-DSA-65)](ADRs/010-post-quantum-cryptography-ml-kem-ml-dsa.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, security rules, and PR requirements.
