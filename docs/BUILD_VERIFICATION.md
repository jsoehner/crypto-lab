# Build & Functional Verification Report

- **Date:** `2026-11-20`
- **Verified By:** **Jeffs' Automated build and deploy agent**
- **Repository:** `jsoehner/crypto-lab` (`v1.6.0`)
- **Overall Status:** `VERIFIED` (Python 3.15, Java 25, JavaScript / Node.js 22)

---

## 1. Trusted OSS Split-Horizon Registry Configuration

Configured via `setup_trusted_oss_repo.py` (`--mode virtual`):

| Scope | Setting | Value |
| :--- | :--- | :--- |
| Local LAN | `TRUSTED_OSS_CACHE_URL` (`.env`, git-excluded) | `http://oss.jsigroup.local:8080` (`healthz`: HTTP `200`) |
| GitHub Actions WAN | `TRUSTED_OSS_CACHE_URL` repo variable | `https://jsigroup-oss.duckdns.org` |
| GitHub Actions Mode | `TRUSTED_OSS_MODE` / `TRUSTED_OSS_GPG_EMAIL` | `virtual` / `oss-signing@the-techy.com` |
| GitHub Actions mTLS | `OSS_MTLS_CLIENT_CERT` / `OSS_MTLS_CLIENT_KEY` | Configured as repository secrets |
| Git Hygiene | `.git/info/exclude` | `.env`, `uv.toml`, `.mvn/settings.xml`, `.mvn/maven.config`, `.npmrc` |

**Ecosystem Registry Observations:**
- **PyPI (`http://oss.jsigroup.local:8080/pypi/virtual/simple`)**: HTTP `200` — resolved `cryptography==50.0.2`, `cffi==2.1.1`, and `pycparser==3.12` cleanly on CPython 3.15.2.
- **npm (`http://oss.jsigroup.local:8080/npm/`)**: HTTP `404` (npm proxy not enabled on local cache); installed `@noble/post-quantum` deterministically via `npm ci` (0 vulnerabilities).

---

## 2. Build, Run & Functional Verification Commands

### Python (`CPython 3.15.2`, `uv 0.13.7`)

```bash
uv venv /tmp/crypto-lab-verify-venv
uv pip install --python /tmp/crypto-lab-verify-venv/bin/python \
  --default-index http://oss.jsigroup.local:8080/pypi/virtual/simple \
  -r python/requirements.txt

/tmp/crypto-lab-verify-venv/bin/python -m unittest discover -s python -p 'test_*.py' -v
/tmp/crypto-lab-verify-venv/bin/python python/run_all.py
```

### Java 25 (`OpenJDK 25.0.5`, `javac 25.0.5`)

```bash
mkdir -p /tmp/crypto-lab-java-out
find java/src/main/java -name '*.java' -print0 | xargs -0 javac -d /tmp/crypto-lab-java-out
for source in java/src/main/java/org/example/crypto/*Example.java; do
  java -cp /tmp/crypto-lab-java-out "org.example.crypto.$(basename "$source" .java)"
done
java -ea -cp /tmp/crypto-lab-java-out org.example.crypto.TestCrypto
```

### JavaScript (`Node.js v22.23.2`, `npm 10.9.8`)

```bash
cd javascript
npm ci
npm test
npm run demo
```

---

## 3. Functional Verification Results

| Suite | Runtime | Result | Summary |
| :--- | :--- | :--- | :--- |
| **Python Unit Tests** | CPython 3.15.2 (`cryptography 50.0.2`) | ✅ PASS | **15 passed, 8 skipped** (23 discovered; 8 live `ctm-ekm-lab` integration tests intentionally skipped when `CIPHERTRUST_URL` is unset). Verified AES-GCM, SHA-256, HMAC, PBKDF2, RSA-OAEP/PSS, Ed25519, X25519+HKDF, AES-KW, PKCS#8, Azure/GCP BYOK+CMK, Vault OIDC EKM Proxy, Offline CipherTrust EKM, and Stage 3 Multi-Cloud Cascade. |
| **Python CLI Demo** | CPython 3.15.2 | ✅ PASS | `python/run_all.py` executed all 9 reference examples cleanly. |
| **Java 25 Examples & Tests** | OpenJDK 25.0.5 | ✅ PASS | Compiled all sources with `javac 25.0.5`, executed all 11 `*Example` classes (including native JEP 496 `ML-KEM-768`, `HybridX25519MlKemExample`, and JEP 497 `ML-DSA-65`), and `TestCrypto` (`-ea`) passed (`All Java tests passed!`). |
| **JavaScript Unit Tests** | Node.js v22.23.2 (`@noble/post-quantum`) | ✅ PASS | **8 / 8 tests passed** (`node --test tests/crypto.test.js`): SHA-256, HMAC-SHA-256, AES-256-GCM, ML-KEM-768 (FIPS 203), ML-DSA-65 (FIPS 204), ML-KEM-768 KEM-DEM, Hybrid X25519 + ML-KEM-768, and SLH-DSA (FIPS 205). |
| **JavaScript CLI Demo** | Node.js v22.23.2 | ✅ PASS | `npm run demo` (`src/run_all.js`) executed all 7 classical + PQC examples cleanly. |
| **PowerShell** | Optional (`pwsh` 7+) | ⏭️ N/A | `pwsh` is not installed on the Linux verification host (optional per `README.md`). |
| **Web UI / HTTP API** | N/A | ⏭️ N/A | Multi-language cryptographic CLI/library reference repository (no Web UI or daemon). |
