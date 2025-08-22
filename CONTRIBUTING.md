# Contributing

## Getting Started

Before you begin, please set up your development environment by following the instructions in the [Development Setup section of the README.md file](./README.md#development-setup). The provided setup scripts will ensure you have all the necessary prerequisites and dependencies.

## Workflow

1. Fork the repo & create a feature branch from main.
2. Ensure the code passes `pre-commit` locally before committing. The setup script will have already installed the pre-commit hooks for you.
   ```bash
   # To run all checks manually:
   poetry run pre-commit run --all-files
   ```
3. Write tests and update docs for your changes.
4. Submit a pull request using the PR template.
