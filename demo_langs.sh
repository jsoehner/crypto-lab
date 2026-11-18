#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}==========================================${NC}"
echo -e "      Language Demonstration Script"
echo -e "${BLUE}==========================================${NC}"

choice="${1:-}"
if [ -z "$choice" ]; then
    echo "Which language(s) would you like to demonstrate? (python, java, javascript, powershell, all)"
    read -r -p "Choice: " choice
fi

run_python() {
    echo -e "\n${GREEN}[Python] Running classical cryptography examples...${NC}"
    if command -v python3 &> /dev/null; then
        python3 python/run_all.py
        if [ -n "${CIPHERTRUST_URL:-}" ]; then
            echo -e "${GREEN}[Python + CTM] Live CipherTrust detected at ${CIPHERTRUST_URL}; running EKM integration...${NC}"
            python3 python/ciphertrust_ekm_example.py
        fi
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
