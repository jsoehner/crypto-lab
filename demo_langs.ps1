param(
    [string]$Choice = ""
)

$GREEN = "`e[0;32m"
$BLUE = "`e[0;34m"
$NC = "`e[0m"

Write-Host "${BLUE}==========================================${NC}"
Write-Host "      Language Demonstration Script"
Write-Host "${BLUE}==========================================${NC}"

if ([string]::IsNullOrWhiteSpace($Choice)) {
    $Choice = Read-Host "Which language(s) would you like to demonstrate? (python, java, javascript, powershell, all)"
}

function Invoke-PythonDemo {
    Write-Host "`n${GREEN}[Python] Running classical cryptography examples...${NC}"
    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        python3 python/run_all.py
    } elseif (Get-Command python -ErrorAction SilentlyContinue) {
        python python/run_all.py
    } else {
        Write-Host "Python is not installed."
    }
}

function Invoke-JavaDemo {
    Write-Host "`n${GREEN}[Java] Running classical and PQC (ML-KEM-768, ML-DSA-65) examples...${NC}"
    if ((Get-Command java -ErrorAction SilentlyContinue) -and (Get-Command bash -ErrorAction SilentlyContinue)) {
        bash java/run_all.sh
    } else {
        Write-Host "Java or Bash is not installed."
    }
}

function Invoke-JavaScriptDemo {
    Write-Host "`n${GREEN}[JavaScript] Running classical and PQC (ML-KEM-768, ML-DSA-65) examples...${NC}"
    if (Get-Command node -ErrorAction SilentlyContinue) {
        node "$PSScriptRoot/javascript/src/run_all.js"
    } else {
        Write-Host "Node.js is not installed."
    }
}

function Invoke-PowerShellDemo {
    Write-Host "`n${GREEN}[PowerShell] Running AES-256-GCM example...${NC}"
    & "$PSScriptRoot/powershell/AesGcmExample.ps1"
}

switch ($Choice.ToLower()) {
    "python"     { Invoke-PythonDemo }
    "java"       { Invoke-JavaDemo }
    "javascript" { Invoke-JavaScriptDemo }
    "js"         { Invoke-JavaScriptDemo }
    "powershell" { Invoke-PowerShellDemo }
    "both"       { Invoke-PythonDemo; Invoke-JavaDemo }
    "all"        { Invoke-PythonDemo; Invoke-JavaDemo; Invoke-JavaScriptDemo; Invoke-PowerShellDemo }
    Default {
        Write-Host "Invalid choice. Choose python, java, javascript, powershell, both, or all."
        exit 1
    }
}

Write-Host "`n${BLUE}==========================================${NC}"
Write-Host "            Demonstration Complete"
Write-Host "${BLUE}==========================================${NC}"
