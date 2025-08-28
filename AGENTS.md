# Proposed Repository Structure

This document outlines a proposed new structure for the repository. The goal is to improve the organization of the codebase, making it more modular, maintainable, and easier for new contributors to understand.

## Proposed Structure

```
.
├── .github/
├── docs/
├── examples/
├── scripts/
├── src/
│   ├── cdisc_data_symphony/
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── cli/
│   │   ├── core/
│   │   ├── generators/
│   │   └── web/
│   └── cdisc_library_client/
├── templates/
├── tests/
├── .gitignore
├── AGENTS.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── poetry.lock
└── pyproject.toml
```

## Explanation of Changes

### 1. `src` Directory

The `src` directory is the main container for all Python source code. This is a standard practice in Python projects and helps to keep the codebase organized.

- **`cdisc_data_symphony/`**: The main application package has been renamed from `cdisc_generators_api` to `cdisc_data_symphony`. This new name is more descriptive and aligns with the project's name, "CDISC Data Symphony," as mentioned in the `README.md` file.

- **Internal Structure of `cdisc_data_symphony/`**: The package has been reorganized into the following sub-modules:
    - `api/`: Contains the FastAPI application for the REST API.
    - `cli/`: Contains the Typer application for the command-line interface.
    - `core/`: Contains the core services and business logic.
    - `generators/`: Contains the core logic for generating artifacts.
    - `web/`: Contains the FastAPI application for the web UI.

- **`cdisc_library_client/`**: This directory contains the generated client for the CDISC Library API. As this is generated code, it should not be manually edited. The process for regenerating this client should be documented, and the client itself could be excluded from version control in the future.

### 2. `scripts/` Directory

The `build_scripts` directory has been renamed to `scripts`. This directory should contain utility scripts for development, build, and deployment tasks. Moving them out of the main source code makes the project cleaner and more intuitive.

### 3. `examples/` Directory

A new `examples/` directory has been created to store example data, configuration files, and usage examples. The contents of the `data/` directory should be moved here to make it clear that they are not required for the application to run.

### 4. `issues/` Directory

The `issues/` directory has been removed. It is recommended to use a dedicated issue tracker like GitHub Issues to manage tasks, bugs, and feature requests. This provides a better workflow for collaboration and tracking progress.

## Next Steps

The proposed changes will be implemented in the following order:

1.  **Restructure the repository** according to the new layout.
2.  **Refactor the CLI** to align with the new structure.
3.  **Update the CI/CD pipeline** to reflect the changes.
4.  **Improve module documentation** to ensure all changes are well-documented.

By following this plan, we can improve the overall quality of the codebase and set a solid foundation for future development.
