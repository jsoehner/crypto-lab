# ADR-010: Post-Quantum Cryptography (ML-KEM-768 and ML-DSA-65)

## Status
Accepted

## Context
Classical asymmetric primitives (RSA, X25519, Ed25519) are vulnerable to Shor's algorithm on cryptographically relevant quantum computers, creating "Harvest Now, Decrypt Later" risk for long-lived confidentiality and signature trust. NIST finalized FIPS 203 (ML-KEM) and FIPS 204 (ML-DSA) in August 2024, and our CBOM audit ([CRYPTOGRAPHIC_AUDIT.md](../docs/security/CRYPTOGRAPHIC_AUDIT.md)) previously reported 0% PQC migration.

## Decision
1. **Key Encapsulation (FIPS 203)**: Adopt **ML-KEM-768** (NIST Security Level 3) paired with **HKDF-SHA-256** and **AES-256-GCM** for key establishment and data encryption.
2. **Digital Signatures (FIPS 204)**: Adopt **ML-DSA-65** (NIST Security Level 3) for quantum-resistant signing and verification.
3. **Reference Implementations**:
   - **Java 25+**: Use the built-in JCA/JCE `ML-KEM` (`NamedParameterSpec.ML_KEM_768`) and `ML-DSA` (`NamedParameterSpec.ML_DSA_65`) providers ([MlKemExample.java](../java/src/main/java/org/example/crypto/MlKemExample.java), [MlDsaExample.java](../java/src/main/java/org/example/crypto/MlDsaExample.java)).
   - **JavaScript (Node.js 22+)**: Use `@noble/post-quantum` (`ml_kem768` and `ml_dsa65`) paired with `node:crypto` HKDF-SHA-256 and AES-256-GCM ([ml_kem_example.js](../javascript/src/ml_kem_example.js), [ml_dsa_example.js](../javascript/src/ml_dsa_example.js)).

## Consequences
- Java 24+ (tested on OpenJDK 25) is required to run `MlKemExample` and `MlDsaExample` without external JCA providers.
- Ciphertext and signature sizes increase compared to ECC (ML-KEM-768 ciphertext: 1,088 bytes; ML-DSA-65 signature: 3,309 bytes).
- Classical examples remain in the repository for interoperability and side-by-side migration comparison.
