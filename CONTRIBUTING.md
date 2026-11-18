# Contributing to Crypto Lab

Thank you for contributing. Follow these guidelines when adding or updating cryptographic examples, tests, or governance docs.

## Reporting Bugs and Suggesting Features

1. Search existing issues and ADRs in [ADRs/](ADRs/) before opening a new issue.
2. Include your OS, language runtime version (Python, JDK, Node.js, or PowerShell), and exact reproduction steps.

## Development Setup

### Prerequisites
- **Python**: Python 3.10+ (`pip install -r python/requirements.txt`)
- **Java**: OpenJDK 25+ (required for built-in `ML-KEM-768` and `ML-DSA-65`)
- **JavaScript**: Node.js 22+ (`cd javascript && npm install`)
- **PowerShell**: PowerShell 7+ (`pwsh`, optional for `.ps1` examples)

### Running Tests Locally

```bash
# Python
python3 -m unittest discover -s python -p 'test_*.py' -v

# Java
./java/run_all.sh
java -ea -cp java/out org.example.crypto.TestCrypto

# JavaScript (Node.js)
npm --prefix javascript test
```

## Coding & Security Standards

- **Review ADRs first**: Every cryptographic primitive choice must align with [ADRs/](ADRs/). New algorithm choices require a new ADR.
- **No weak primitives**: Do not add MD5, SHA-1, ECB mode, PKCS#1 v1.5 encryption, or static/hardcoded nonces and salts.
- **Constant-time verification**: Use constant-time comparison for MACs and derived secrets (`hmac.compare_digest` in Python, `MessageDigest.isEqual` in Java, `crypto.timingSafeEqual` in Node.js).
- **Negative tests**: Every new primitive must include at least one negative test (tampered ciphertext, wrong AAD, or invalid signature).

## Commit Message Guidelines

Use **Conventional Commits**:
- `feat:` New cryptographic example or capability
- `fix:` Bug fix or test correction
- `docs:` Documentation and ADR updates
- `chore:` CI, dependency, or build updates
- `test:` Test additions or improvements

Example: `feat(rust): add ML-KEM-768 and ML-DSA-65 reference examples`

## Pull Request Process

1. Create a feature branch (`git checkout -b feat/your-feature`).
2. Run all language test suites and the local BOM check (`bash scripts/generate_boms.sh -t dir .` and `bash scripts/test_boms.sh oss`) if you modified cryptographic code.
3. Fill out [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).
