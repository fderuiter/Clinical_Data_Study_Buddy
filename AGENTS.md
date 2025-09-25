# Agent Instructions

This document provides instructions for AI agents working with this repository.

## Development

- This project uses `poetry` for dependency management.
- The `Makefile` contains targets for common tasks:
    - `make install`: Install dependencies.
    - `make test`: Run tests.
    - `make format`: Format code with `black` and `isort`.
    - `make lint`: Lint code with `ruff`.
    - `make type-check`: Run `mypy` for type checking.
    - `make health-check`: Run all checks.
    - `make generate-client`: Regenerate the `cdisc_library_client`.

## Generated Code

The `src/cdisc_library_client` directory is auto-generated. Do not edit the files in this directory directly. To update the client, run `make generate-client`.
