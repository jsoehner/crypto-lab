#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[1;32m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
YELLOW='\033[1;33m'
MAGENTA='\033[1;35m'
NC='\033[0m'

echo -e "${BLUE}======================================================================${NC}"
echo -e "            Crypto Lab — Interactive Security & PQC Demo"
echo -e "${BLUE}======================================================================${NC}"
echo -e "${MAGENTA}[PROBLEM]${NC} Threat / Scenario  |  ${CYAN}[WHAT]${NC} Action  |  ${YELLOW}[WHY]${NC} Security Rationale"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CTM_EKM_LAB_DIR="${CTM_EKM_LAB_DIR:-$(cd "${SCRIPT_DIR}/.." && pwd)/ctm-ekm-lab}"
CTM_LAB_PID=""

cleanup_ctm_lab() {
    if [ -n "${CTM_LAB_PID:-}" ]; then
        kill "$CTM_LAB_PID" 2>/dev/null || true
    fi
}
trap cleanup_ctm_lab EXIT

is_ctm_reachable() {
    python3 -c "import urllib.parse, socket; u=urllib.parse.urlparse('${CIPHERTRUST_URL}'); s=socket.create_connection((u.hostname, u.port or 443), timeout=2); s.close()" 2>/dev/null
}

print_ctm_status() {
    if [ -n "${CIPHERTRUST_URL:-}" ]; then
        mtls_state="disabled"
        if [ -n "${CIPHERTRUST_CLIENT_CERT:-}" ]; then
            mtls_state="enabled"
        fi
        if is_ctm_reachable; then
            echo -e "${GREEN}[CTM STATUS] AVAILABLE${NC} — Live CipherTrust EKM at ${CIPHERTRUST_URL} (mTLS: ${mtls_state})"
            return 0
        else
            echo -e "\033[0;33m[CTM STATUS] UNREACHABLE\033[0m — ${CIPHERTRUST_URL} did not respond (live CTM calls will fail)"
            return 1
        fi
    else
        echo -e "\033[0;33m[CTM STATUS] NOT AVAILABLE\033[0m — CIPHERTRUST_URL unset (using offline EKM simulator)"
        return 1
    fi
}

activate_ctm_lab() {
    local lab_dir="$1"
    local env_file="${lab_dir}/.env.ciphertrust"

    if [ -f "$env_file" ]; then
        set -a
        # shellcheck disable=SC1090
        source "$env_file"
        set +a
    else
        export CIPHERTRUST_URL="${CIPHERTRUST_URL:-https://127.0.0.1:8443}"
        export CIPHERTRUST_USER="${CIPHERTRUST_USER:-admin}"
        export CIPHERTRUST_PASSWORD="${CIPHERTRUST_PASSWORD:-lab-bootstrap-pass}"
    fi

    if ! is_ctm_reachable; then
        if [ ! -f "${lab_dir}/certs/lab-ca.crt" ] || [ ! -f "${lab_dir}/certs/cm-server.crt" ] || [ ! -f "${lab_dir}/certs/ekm-client.crt" ]; then
            echo -e "${CYAN}[CTM SETUP]${NC} Generating lab mTLS certificates..."
            bash "${lab_dir}/scripts/generate_mtls_certs.sh"
        fi
        echo -e "${CYAN}[CTM SETUP]${NC} Starting local ctm-ekm-lab mock server..."
        CM_REQUIRE_MTLS=true python3 "${lab_dir}/mock-cm-ce/server.py" >/tmp/ctm-ekm-lab.log 2>&1 &
        CTM_LAB_PID=$!
        for _ in $(seq 1 20); do
            if is_ctm_reachable; then
                break
            fi
            sleep 0.25
        done
    fi

    if [ ! -f "$env_file" ] && is_ctm_reachable; then
        echo -e "${CYAN}[CTM SETUP]${NC} Bootstrapping CipherTrust lab environment..."
        bash "${lab_dir}/scripts/bootstrap_cm_ce.sh"
        set -a
        # shellcheck disable=SC1090
        source "$env_file"
        set +a
    fi

    print_ctm_status || true
}

if ! print_ctm_status; then
    if [ -d "$CTM_EKM_LAB_DIR" ] && [ -z "${CI:-}" ] && { [ -t 0 ] || [ -z "${1:-}" ]; }; then
        read -r -p "Activate optional ctm-ekm-lab dependency before continuing? [y/N]: " activate_ctm || true
        if [[ "${activate_ctm,,}" =~ ^(y|yes)$ ]]; then
            activate_ctm_lab "$CTM_EKM_LAB_DIR"
        fi
    fi
fi

choice="${1:-}"
if [ -z "$choice" ]; then
    echo "Which language(s) would you like to demonstrate? (python, java, javascript, powershell, all)"
    read -r -p "Choice: " choice
fi

run_python() {
    echo -e "\n${GREEN}[Python] Classical Cryptography & Key Protection${NC}"
    echo -e "  ${MAGENTA}[PROBLEM]${NC} Plaintext data, weak hashes, and unauthenticated ciphertexts expose secrets to tampering and brute force."
    echo -e "  ${CYAN}[WHAT]${NC}    Running SHA-256, HMAC, PBKDF2, AES-256-GCM, RSA-3072, Ed25519, X25519+HKDF, AES-KW, and encrypted PKCS#8."
    echo -e "  ${YELLOW}[WHY]${NC}     Uses CSPRNG nonces/salts, constant-time checks, and 256-bit symmetric keys (Grover-resistant)."
    if command -v python3 &> /dev/null; then
        python3 python/run_all.py
        echo -e "\n${GREEN}[External KMS / CTM] Sovereign Key Control Plane${NC}"
        echo -e "  ${MAGENTA}[PROBLEM]${NC} Storing root KEKs inside cloud providers risks unauthorized access and slow incident revocation."
        echo -e "  ${CYAN}[WHAT]${NC}    Running Sovereign EKM control plane and CipherTrust REST client (live mTLS or offline simulator)."
        echo -e "  ${YELLOW}[WHY]${NC}     Root KEKs never leave your external KMS, enabling instant kill-switch revocation and immutable audit logs."
        python3 python/external_kms_ekm_example.py
        python3 python/ciphertrust_ekm_example.py
        python3 python/vault_ekm_proxy_example.py
        python3 python/stage3_multi_cloud_ekm_orchestration.py
    else
        echo "Python 3 is not installed."
    fi
}

run_java() {
    echo -e "\n${GREEN}[Java 25] Classical & Post-Quantum Cryptography (FIPS 203 / 204)${NC}"
    echo -e "  ${MAGENTA}[PROBLEM]${NC} Quantum computers running Shor's algorithm will break RSA, X25519, and Ed25519 ('Harvest Now, Decrypt Later')."
    echo -e "  ${CYAN}[WHAT]${NC}    Compiling and running Java 25 JCA/JCE examples including ML-KEM-768, Hybrid X25519+ML-KEM-768, and ML-DSA-65."
    echo -e "  ${YELLOW}[WHY]${NC}     Native JDK 25 ML-KEM and ML-DSA provide NIST-standardized quantum resistance alongside classical baselines."
    if command -v java &> /dev/null; then
        chmod +x java/run_all.sh
        ./java/run_all.sh
    else
        echo "Java is not installed."
    fi
}

run_javascript() {
    echo -e "\n${GREEN}[JavaScript / Node.js 22] Classical & Post-Quantum (FIPS 203 / 204 / 205)${NC}"
    echo -e "  ${MAGENTA}[PROBLEM]${NC} Web and API services need quantum-resistant key exchange and both lattice & hash-based signatures."
    echo -e "  ${CYAN}[WHAT]${NC}    Running Node.js crypto + @noble/post-quantum (ML-KEM-768, Hybrid KEM, ML-DSA-65, and SLH-DSA FIPS 205)."
    echo -e "  ${YELLOW}[WHY]${NC}     SLH-DSA provides stateless hash-based signatures with zero lattice assumptions for high-assurance roots."
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
