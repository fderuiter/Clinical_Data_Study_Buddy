# Contributing

We welcome contributions to the CDISC Generators project. This guide will help you get your development environment set up.

## Development Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management. Setup scripts are provided for different operating systems.

### Linux and macOS

Run the setup script from your shell:

```bash
./setup.sh
```

The script will:
1.  Check for `python3` (3.11+) and `poetry`.
2.  If they are not found, it will attempt to install them using the system's package manager (`apt`, `yum`, or `brew`).
3.  Install all project dependencies.
4.  Set up pre-commit hooks.

### Windows

Run the PowerShell setup script from a PowerShell terminal. You may need to adjust your execution policy first:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
./setup.ps1
```

The script will:
1.  Check for Python 3.11+ and Poetry.
2.  If they are not found, it will download and install them. This may require administrator privileges.
3.  Install all project dependencies.
4.  Set up pre-commit hooks.
> **Note:** If Python or Poetry are installed by the script, you will need to restart your terminal and run the script again for the changes to take effect.

### Docker-based Environment (Recommended)

For the most consistent and reliable setup, you can use the provided development container. This avoids any "works on my machine" issues.

**Prerequisites:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**To get started:**
1.  Open the project folder in VS Code.
2.  A notification will appear asking if you want to "Reopen in Container". Click it.
3.  VS Code will build the Docker image and start the development container. This may take a few minutes on the first run.

Once inside the dev container, you'll have a fully configured environment with all tools and dependencies ready to go. You can use the integrated terminal in VS Code to run tests, scripts, etc.

## Updating the CDISC Library API Client

This project includes a generated Python client for the CDISC Library API located in `src/cdisc_library_client`. This client is generated from the official CDISC Library OpenAPI specification.

To update the client to the latest version, you can use the following command:

```bash
make update-sdk
```

This command will:
1.  Download the latest OpenAPI specification from the official CDISC website.
2.  Regenerate the Python client in `src/cdisc_library_client`.

It is recommended to run this command periodically to ensure the client is up-to-date with any changes to the CDISC Library API.
