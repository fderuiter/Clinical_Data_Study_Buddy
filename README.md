# CDISC CRF Generator

![Weekly Sync Status](https://github.com/fderuiter/cdisc_crf_generator/actions/workflows/weekly-sync.yml/badge.svg)

This project provides tools for generating Case Report Forms (CRFs) using metadata from the CDISC Library.

Additional documentation is available in the [docs](docs/) directory, including an [FAQ](docs/FAQ.md) about accessing and using the CDISC Library.

Utility helpers such as `cdisc_library_client.normalize_headers()` are provided
to sanitize HTTP headers before requests are made. This avoids issues when
secrets are supplied as bytes.


## Quickstart

Follow these steps to set up the project and generate your first set of CRF artifacts.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fderuiter/cdisc_crf_generator.git
    cd cdisc_crf_generator
    ```

2.  **Set up the environment:**
    This project uses Poetry for dependency management. Make sure you have Python 3.11+ and Poetry installed.
    ```bash
    poetry install
    ```

3.  **Configure your CDISC Library API Key:**
    You will need a primary subscription key from the CDISC Library. Once you have it, export it as an environment variable:
    ```bash
    export CDISC_PRIMARY_KEY="your-api-key-here"
    ```

4.  **Fetch the canonical CRF data:**
    This command crawls the CDISC Library and creates a canonical `crf.json` file.
    ```bash
    poetry run scripts/build_canonical.py -o crf.json
    ```

5.  **Generate all CRF artifacts:**
    This command reads the `crf.json` file and generates the CRF documents in multiple formats (Markdown, DOCX, CSV, etc.) inside the `artefacts/` directory.
    ```bash
    poetry run scripts/build.py --source crf.json --outdir artefacts
    ```

6.  **View the generated files:**
    The generated artifacts are now in the `artefacts/` directory. You can open them to see the results. For example, on macOS, you could run:
    ```bash
    open artefacts/VS.docx
    ```
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

**Prerequisites:**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**To get started:**
1.  Open the project folder in VS Code.
2.  A notification will appear asking if you want to "Reopen in Container". Click it.
3.  VS Code will build the Docker image and start the development container. This may take a few minutes on the first run.

Once inside the dev container, you'll have a fully configured environment with all tools and dependencies ready to go. You can use the integrated terminal in VS Code to run tests, scripts, etc.

## Generating CDASH CRFs

The repository includes `scripts/generate_cdash_crf.py` which converts the
official CDASH workbooks into Word documents—one per domain.  The script now
adds extra metadata from the IG such as variable type, controlled terminology
and completion instructions.  Generated CRFs use a consistent landscape layout
with protocol information in the header and versioned footers with page numbers.
`pandas`, `python-docx` and `openpyxl` are already listed in the project
dependencies.

```bash
python scripts/generate_cdash_crf.py \
    --model CDASH_Model_v1.3.xlsx \
    --ig CDASHIG_v2.3.xlsx \
    --out ./crfs

# To build only specific domains
python scripts/generate_cdash_crf.py --model CDASH_Model_v1.3.xlsx \
    --ig CDASHIG_v2.3.xlsx --domains AE CM
```

Edit `build_domain_crf()` in the script to customise the table layout or add
study branding or adjust fonts and orientation if needed.

## Generating Synthetic Datasets

In addition to generating CRFs from the CDISC Library, this project can also generate synthetic CDISC-compliant datasets using the cdiscdataset.com API.

### Quickstart

To generate a synthetic dataset, run the `scripts/generate_synthetic_data.py` script with the desired parameters. For example, to generate an SDTM dataset for the DM domain, run the following command:

```bash
python scripts/generate_synthetic_data.py \
    --dataset-type SDTM \
    --domain DM \
    --num-subjects 100 \
    --output-dir ./synthetic_data
```

This will generate a CSV file in the `synthetic_data` directory.

### Options

The following options are available for the `generate_synthetic_data.py` script:

| Option             | Description                                  | Default    |
| ------------------ | -------------------------------------------- | ---------- |
| `--dataset-type`   | Type of dataset to generate (SDTM, ADaM, SEND) |            |
| `--domain`         | Domain for the dataset                       |            |
| `--num-subjects`   | Number of subjects                           | 50         |
| `--therapeutic-area` | Therapeutic area                             | "Oncology" |
| `--format`         | Output format (csv, json, xpt)               | "csv"      |
| `--output-dir`     | Directory to save the downloaded file        | "."        |

## Generating Reviewer's Guides

This project includes scripts to generate an Analysis Data Reviewer's Guide (ADRG) and a Study Data Reviewer's Guide (SDRG). These guides are based on the PHUSE templates and are intended for FDA submissions.

### Prerequisites

Before generating the reviewer's guides, you need to have a `crf.json` file and a `study_config.json` file.

- The `crf.json` file can be generated by running `scripts/build_canonical.py`.
- The `study_config.json` file should be created manually and should contain study-specific information. See the example below:

```json
{
  "study_id": "ABC-123",
  "protocol_id": "XYZ-001",
  "protocol_title": "A Study to Evaluate the Efficacy and Safety of a New Drug"
}
```

### Generating the ADRG

To generate the ADRG, run the `scripts/generate_adrg.py` script:

```bash
python scripts/generate_adrg.py \
    --crf crf.json \
    --config study_config.json \
    --out adrg.docx
```

### Generating the SDRG

To generate the SDRG, run the `scripts/generate_sdrg.py` script:

```bash
python scripts/generate_sdrg.py \
    --crf crf.json \
    --config study_config.json \
    --out sdrg.docx
```
