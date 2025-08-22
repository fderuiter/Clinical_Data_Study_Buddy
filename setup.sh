#!/bin/bash
#
# Setup script for the cdisc-crf-generator development environment.
#
# This script ensures that the necessary prerequisites are met and installs
# all the required dependencies for development.
#

set -e

# Function to check for a command
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# OS detection
OS="$(uname -s)"
case "${OS}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    *)          machine="UNKNOWN:${OS}"
esac

echo "Detected OS: ${machine}"

# --- Prerequisite Installation ---

# Function to install Python
install_python() {
    echo "Attempting to install Python 3.12+..."
    if [ "$machine" == "Linux" ]; then
        if command_exists apt-get; then
            sudo apt-get update
            sudo apt-get install -y python3.12 python3.12-venv
        elif command_exists yum; then
            # RHEL/CentOS often have older package names
            sudo yum install -y python3
        else
            echo "Error: Neither apt-get nor yum found. Please install Python 3.12+ manually." >&2
            exit 1
        fi
    elif [ "$machine" == "Mac" ]; then
        if ! command_exists brew; then
            echo "Error: Homebrew not found. Please install Homebrew first, then run this script again." >&2
            exit 1
        fi
        brew install python@3.12
    else
        echo "Error: Unsupported OS. Please install Python 3.12+ manually." >&2
        exit 1
    fi
    echo "Python installation complete."
}

# Function to install Poetry
install_poetry() {
    echo "Attempting to install Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    # Add poetry to PATH for the current session
    export PATH="$HOME/.local/bin:$PATH"
    echo "Poetry installation complete."
}


# Check for Python 3.12+
echo "Checking for Python 3.12+..."
if ! command_exists python3; then
    install_python
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
MIN_VERSION="3.12"
if [ "$(printf '%s\n' "$MIN_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$MIN_VERSION" ]; then
    install_python
fi
echo "Python version check passed."


# Check for Poetry
echo "Checking for Poetry..."
if ! command_exists poetry; then
    install_poetry
fi
echo "Poetry check passed."

echo "Starting development environment setup..."

echo "Installing dependencies with Poetry..."
poetry install

echo "Dependencies installed successfully."

echo "Installing pre-commit hooks..."
if [ -z "$CI" ]; then
    # Unset core.hooksPath to allow pre-commit to install hooks
    git config --global --unset-all core.hooksPath
    poetry run pre-commit install
    echo "Pre-commit hooks installed successfully."
else
    echo "Skipping pre-commit hook installation in CI environment."
fi

echo "Setup complete. The development environment is ready."
