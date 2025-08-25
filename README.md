# CDISC Generators

![Weekly Sync Status](https://github.com/fderuiter/cdisc_generators/actions/workflows/weekly-sync.yml/badge.svg)

This project provides tools for generating Case Report Forms (CRFs) using metadata from the CDISC Library.

Additional documentation is available in the [docs](docs/) directory, including an [FAQ](docs/FAQ.md) about accessing and using the CDISC Library.

Utility helpers such as `cdisc_library_client.normalize_headers()` are provided
to sanitize HTTP headers before requests are made. This avoids issues when
secrets are supplied as bytes.


## Quickstart

Follow these steps to set up the project and generate your first set of CRF artifacts.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fderuiter/cdisc_generators.git
    cd cdisc_generators
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
    poetry run cdisc build-canonical -o crf.json
    ```

5.  **Generate all CRF artifacts:**
    This command reads the `crf.json` file and generates the CRF documents in multiple formats (Markdown, DOCX, CSV, etc.) inside the `artefacts/` directory.
    ```bash
    poetry run cdisc build --source crf.json --outdir artefacts
    ```

6.  **View the generated files:**
    The generated artifacts are now in the `artefacts/` directory. You can open them to see the results. For example, on macOS, you could run:
    ```bash
    open artefacts/VS.docx
    ```

## Web UI (New)

This project also includes a web-based user interface for generating datasets.

To run the UI, use the following command:
```bash
poetry run uvicorn src.ui.main:app --reload
```

Then, open your web browser and navigate to `http://127.0.0.1:8000`.
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

The repository includes a command to convert the official CDASH workbooks into Word documents—one per domain.  The command now adds extra metadata from the IG such as variable type, controlled terminology and completion instructions.  Generated CRFs use a consistent landscape layout with protocol information in the header and versioned footers with page numbers.

```bash
poetry run cdisc generate-cdash-crf --ig-version v2.3 --out ./crfs

# To build only specific domains
poetry run cdisc generate-cdash-crf --ig-version v2.3 --domains AE CM --out ./crfs
```

## Generating Analysis Code

This project can also generate analysis code in SAS and R for various outputs.

### Quickstart

To generate an analysis script, use the `generate-analysis` command. For example, to generate a SAS script for a demographics table from the ADSL dataset, run the following command:

```bash
poetry run cdisc generate-analysis \
    --language sas \
    --dataset ADSL \
    --output-type demographics \
    --treatment-var TRT01A \
    --output-file demog_table.sas
```

This will generate a SAS file named `demog_table.sas` in the current directory.

## Generating Synthetic Datasets

In addition to generating CRFs from the CDISC Library, this project can also generate synthetic CDISC-compliant datasets using the cdiscdataset.com API.

### Quickstart

To generate a synthetic dataset, use the `generate-synthetic-data` command. For example, to generate an SDTM dataset for the DM domain, run the following command:

```bash
poetry run cdisc generate-synthetic-data \
    --dataset-type SDTM \
    --domain DM \
    --num-subjects 100 \
    --output-dir ./synthetic_data
```

This will generate a CSV file in the `synthetic_data` directory.


## Generating EDC Raw Dataset Package

This project includes a command to generate a complete package of raw EDC datasets for a clinical study. The command, `generate-raw-dataset-package`, generates a ZIP file containing multiple datasets with consistent subjects across all domains. It also includes a draft `define.xml` file (currently with limited metadata).

### Quickstart

To generate a raw dataset package, use the `generate-raw-dataset-package` command. For example, to generate a package with DM, VS, and LB domains for 10 subjects in the Oncology therapeutic area, run the following command:

```bash
poetry run cdisc generate-raw-dataset-package \
    --num-subjects 10 \
    --domains DM --domains VS --domains LB \
    --therapeutic-area Oncology \
    --output-dir ./raw_dataset_package
```

This will generate a `edc_raw_datasets.zip` file in the `raw_dataset_package` directory.

## Generating Study Protocols

This project can also generate study protocol documents. This feature is useful for creating a quick draft of a protocol based on a few key parameters.

### Quickstart

To generate a study protocol, use the `protocol generate` command:

```bash
poetry run cdisc protocol generate \
    --therapeutic-area "Oncology" \
    --treatment-arm "Drug A + Placebo" \
    --treatment-arm "Drug B + Placebo" \
    --duration-weeks 52 \
    --phase 3 \
    --output-dir "my_protocol"
```

This will generate a `protocol.md` file and a `gantt_chart.png` file in the `my_protocol` directory.

## Specification Management

This project provides tools to generate and validate dataset specifications.

### Generating an Excel Specification

You can generate an Excel-based specification template for a given CDISC product and version.

```bash
poetry run cdisc spec generate-template --product sdtmig --version 3-3 --domains DM --domains AE --domains VS
```

This will create a file named `sdtmig_3-3_spec.xlsx` with sheets for the DM, AE, and VS domains.

### Generating a Dataset from a Specification

Once you have a specification file, you can generate a synthetic dataset from it.

```bash
poetry run cdisc spec generate-dataset --spec-file sdtmig_3-3_spec.xlsx
```

This will generate CSV files for each domain (sheet) in the specification file.

### Validating a Dataset Against a Specification

You can also validate an existing dataset against a specification file.

```bash
poetry run cdisc spec validate --spec-file sdtmig_3-3_spec.xlsx --dataset-file sdtm_dm_20250822_215518.csv
```

This will check for missing/extra columns and data type mismatches.

## Generating Reviewer's Guides

This project includes commands to generate an Analysis Data Reviewer's Guide (ADRG) and a Study Data Reviewer's Guide (SDRG). These guides are based on the PHUSE templates and are intended for FDA submissions.

### Prerequisites

Before generating the reviewer's guides, you need to have a `crf.json` file and a `study_config.json` file.

- The `crf.json` file can be generated by running `poetry run cdisc build-canonical`.
- The `study_config.json` file should be created manually and should contain study-specific information. See the example below:

```json
{
  "study_id": "ABC-123",
  "protocol_id": "XYZ-001",
  "protocol_title": "A Study to Evaluate the Efficacy and Safety of a New Drug"
}
```

### Generating the ADRG

To generate the ADRG, use the `adrg generate` command:

```bash
poetry run cdisc adrg generate \
    --crf crf.json \
    --config study_config.json \
    --out adrg.docx
```

### Generating the SDRG

To generate the SDRG, use the `sdrg generate` command:

```bash
poetry run cdisc sdrg generate \
    --crf crf.json \
    --config study_config.json \
    --out sdrg.docx
```

## OpenFDA Integration

This project includes features to integrate data from [open.fda.gov](https://open.fda.gov/) to enrich the generated CRFs.

### Populating CRFs with Adverse Event Data

You can automatically populate the Adverse Events (AE) CRF with suggested terms for a specific drug. The `generate-cdash-crf` command has a new option to support this:

```bash
poetry run cdisc generate-cdash-crf \
    --ig-version v2.3 \
    --domains AE \
    --openfda-drug-name "Aspirin" \
    --openfda-max-results 50
```

This will fetch the top 50 most frequently reported adverse events for Aspirin from OpenFDA and add them to a separate table in the generated `AE_Adverse_Events_CRF.docx` document, providing a useful reference for common adverse events.

### Standalone OpenFDA Command

For more advanced queries, you can use the `openfda populate-crf` command. This command allows you to fetch adverse events or drug labeling information and output it in various formats.

**Examples:**

Fetch adverse events for a drug and save as JSON:
```bash
poetry run cdisc openfda populate-crf \
    --drug-name "Ibuprofen" \
    --domain AE \
    --max-results 100 \
    --output-format json > ibuprofen_aes.json
```

Fetch drug label information for a drug:
```bash
poetry run cdisc openfda populate-crf \
    --drug-name "Tylenol" \
    --domain LABEL
```
