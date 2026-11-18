#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}==========================================${NC}"
echo -e "      Language Demonstration Script"
echo -e "${BLUE}==========================================${NC}"

if [ -n "${CIPHERTRUST_URL:-}" ]; then
    mtls_state="disabled"
    if [ -n "${CIPHERTRUST_CLIENT_CERT:-}" ]; then
        mtls_state="enabled"
    fi
    if python3 -c "import urllib.parse, socket; u=urllib.parse.urlparse('${CIPHERTRUST_URL}'); s=socket.create_connection((u.hostname, u.port or 443), timeout=2); s.close()" 2>/dev/null; then
        echo -e "${GREEN}[CTM STATUS] AVAILABLE${NC} — Live CipherTrust EKM at ${CIPHERTRUST_URL} (mTLS: ${mtls_state})"
    else
        echo -e "\033[0;33m[CTM STATUS] UNREACHABLE\033[0m — ${CIPHERTRUST_URL} did not respond (live CTM calls will fail)"
    fi
else
    echo -e "\033[0;33m[CTM STATUS] NOT AVAILABLE\033[0m — CIPHERTRUST_URL unset (using offline EKM simulator)"
fi

choice="${1:-}"
if [ -z "$choice" ]; then
    echo "Which language(s) would you like to demonstrate? (python, java, javascript, powershell, all)"
    read -r -p "Choice: " choice
fi

run_python() {
    echo -e "\n${GREEN}[Python] Running classical cryptography examples...${NC}"
    if command -v python3 &> /dev/null; then
        python3 python/run_all.py
        echo -e "\n${GREEN}[External KMS / CTM] Running Sovereign EKM & CipherTrust examples...${NC}"
        python3 python/external_kms_ekm_example.py
        python3 python/ciphertrust_ekm_example.py
    else
        echo "Python 3 is not installed."
    fi
}

run_java() {
    echo -e "\n${GREEN}[Java] Running classical and PQC (ML-KEM-768, ML-DSA-65) examples...${NC}"
    if command -v java &> /dev/null; then
        chmod +x java/run_all.sh
        ./java/run_all.sh
    else
        echo "Java is not installed."
    fi
}

run_javascript() {
    echo -e "\n${GREEN}[JavaScript] Running classical and PQC (ML-KEM-768, ML-DSA-65) examples...${NC}"
    if command -v node &> /dev/null; then
        node javascript/src/run_all.js
    else
        echo "Node.js is not installed."
    fi
}

run_powershell() {
    echo -e "\n${GREEN}[PowerShell] Running AES-256-GCM example...${NC}"
    if command -v pwsh &> /dev/null; then
        pwsh -NoProfile -File powershell/AesGcmExample.ps1
    else
        echo "PowerShell (pwsh) is not installed."
    fi
}

case "${choice,,}" in
    python)
        run_python
        ;;
    java)
        run_java
        ;;
    javascript|js)
        run_javascript
        ;;
    powershell|pwsh)
        run_powershell
        ;;
    both)
        run_python
        run_java
        ;;
    all)
        run_python
        run_java
        run_javascript
        run_powershell
        ;;
    *)
        echo "Invalid choice. Choose python, java, javascript, powershell, both, or all."
        exit 1
        ;;
esac

echo -e "\n${BLUE}==========================================${NC}"
echo -e "            Demonstration Complete"
echo -e "${BLUE}==========================================${NC}"
