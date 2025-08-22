#Requires -Version 5.1

<#
.SYNOPSIS
    Sets up the development environment for the cdisc-crf-generator project on Windows.
.DESCRIPTION
    This script performs the following steps:
    1. Checks for prerequisites (Python 3.11+, Poetry).
    2. Installs any missing prerequisites.
    3. Installs project dependencies using Poetry.
    4. Installs pre-commit hooks.
.NOTES
    This script may need to be run with Administrator privileges to install software.
#>

# Stop on first error
$ErrorActionPreference = "Stop"

Write-Host "Starting development environment setup for Windows..."

# --- Helper Functions ---

# Check if a command exists
function Command-Exists {
    param($Command)
    return (Get-Command $Command -ErrorAction SilentlyContinue)
}

# --- Prerequisite Checks and Installation ---

# 1. Check for Python
Write-Host "Checking for Python 3.11+..."
$pythonExists = Command-Exists python
$pythonVersionCorrect = $false

if ($pythonExists) {
    $versionString = (python --version)
    if ($versionString -match "(\d+)\.(\d+)") {
        $major = $matches[1]
        $minor = $matches[2]
        if (($major -gt 3) -or (($major -eq 3) -and ($minor -ge 11))) {
            $pythonVersionCorrect = $true
            Write-Host "Python version $major.$minor found."
        }
    }
}

if (-not $pythonVersionCorrect) {
    Write-Host "Python 3.11+ not found. Attempting to install Python 3.11.8..."
    $installerUrl = "https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe"
    $installerPath = Join-Path $env:TEMP "python-installer.exe"
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath

    Write-Host "Starting Python installer... This may require administrative privileges."
    Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait -Verb RunAs

    Remove-Item $installerPath
    Write-Host "Python installation complete. Please re-run this script in a new terminal to continue."
    exit
}

# 2. Check for Poetry
Write-Host "Checking for Poetry..."
if (-not (Command-Exists poetry)) {
    Write-Host "Poetry not found. Attempting to install..."
    # The official Poetry installer for PowerShell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    Write-Host "Poetry installation complete."
    Write-Host "Please open a new terminal and run this script again to ensure Poetry is in the PATH."
    exit
}

Write-Host "All prerequisites are met."

Write-Host "Installing project dependencies with Poetry..."
poetry install
Write-Host "Dependencies installed successfully."

Write-Host "Installing pre-commit hooks..."
# Unset core.hooksPath to allow pre-commit to install hooks, similar to the bash script
git config --unset-all core.hooksPath
poetry run pre-commit install
Write-Host "Pre-commit hooks installed successfully."

Write-Host ""
Write-Host "Setup complete. The development environment is ready."
