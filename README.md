# Clinical Data Study Buddy

![Weekly Sync Status](https://github.com/fderuiter/Clinical_Data_Study_Buddy/actions/workflows/weekly-sync.yml/badge.svg)

Clinical Data Study Buddy is a comprehensive suite of tools designed to streamline the generation of clinical study artifacts. It helps create and manage clinical trial documentation and data, ensuring compliance with CDISC standards. Artifacts that can be generated include Case Report Forms (CRFs), synthetic datasets, analysis code, study protocols, and more.

## Features

*   **Standards-Based Artifact Generation**:
    *   **CRF Generation**: Generate Case Report Forms (CRFs) in various formats (e.g., PDF, DOCX, CSV, RTF, XML) from CDISC standards.
    *   **Specification Templates**: Create Excel-based specification templates for CDISC datasets.
    *   **Reviewer's Guides**: Generate Study Data Reviewer's Guides (SDRG) and Analysis Data Reviewer's Guides (ADRG).
    *   **Study Protocols**: Create comprehensive study protocols from a template, including Gantt charts for timelines.
*   **Data Generation and Integration**:
    *   **Synthetic Data Generation**: Create synthetic datasets for testing and validation purposes based on CDISC standards or specification files.
    *   **EDC Raw Dataset Packages**: Generate complete packages of synthetic datasets for simulated studies, including `define.xml`.
    *   **OpenFDA Integration**: Integrate with the OpenFDA API to fetch adverse event and drug label data to enrich generated artifacts.
*   **Analysis and Reporting**:
    *   **Analysis Code Generation**: Generate analysis code in SAS or R for common clinical trial analyses like demographic tables, vital signs, and TEAE summaries.
    *   **TFL Shell Generation**: Create shell documents for Tables, Figures, and Listings (TFLs).
*   **User Interfaces**:
    *   **Command-Line Interface (CLI)**: A powerful and scriptable CLI for all functionalities, built with Typer.
    *   **Web User Interface (UI)**: An intuitive web-based UI for key features, built with FastAPI.

## Architecture Overview

The project is architected to be modular and extensible, with a clear separation of concerns. The main components are:

*   `src/clinical_data_study_buddy/`: The main application package.
    *   `core/`: Contains the core business logic and high-level services that orchestrate the generation and download processes.
    *   `generators/`: Houses the specific logic for generating the various artifacts. Each generator is responsible for a specific type of output (e.g., `CRFGenerator`, `DataGenerator`, `TFLShellGenerator`). This is where the main "work" of the application happens.
    *   `services/`: Provides a layer of services that abstract away lower-level details, such as interacting with the CDISC Library API or the local file system.
    *   `cli/`: Implements the command-line interface using Typer. Each command is organized into its own subcommand, making the CLI easy to use and extend.
    *   `web/`: Contains the web-based user interface, built with FastAPI and Jinja2 templates. It provides a user-friendly way to access the application's features.
    *   `api/`: Contains a REST API, also built with FastAPI, which is currently used for the OpenFDA integration.
*   `src/cdisc_library_client/`: A generated Python client for the CDISC Library API. See the section below for more details.
*   `templates/`: Contains Jinja2 templates used for generating documents like CRFs and study protocols.
*   `scripts/`: Includes utility scripts for development tasks, such as regenerating the CDISC Library client.

## Installation

To use Clinical Data Study Buddy, you need to have Python 3.12+ and Poetry installed.

1.  **Install Python 3.12+**: Follow the instructions on the [official Python website](https://www.python.org/downloads/).
2.  **Install Poetry**: Follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Once you have Python and Poetry installed, you can clone the repository and install the dependencies:

```bash
git clone https://github.com/fderuiter/Clinical_Data_Study_Buddy.git
cd Clinical_Data_Study_Buddy
poetry install
```

## Configuration

To use features that interact with the CDISC Library API, you need to set the `CDISC_PRIMARY_KEY` environment variable. You can do this by creating a `.env` file in the root of the project:

```
CDISC_PRIMARY_KEY="your-api-key"
```

## Development Setup

If you want to contribute to the project, you will need to set up a development environment.

1.  **Fork and Clone the Repository**:
    ```bash
    git clone https://github.com/<your-username>/Clinical_Data_Study_Buddy.git
    cd Clinical_Data_Study_Buddy
    ```

2.  **Install Dependencies**:
    The `setup.sh` script will install all the necessary dependencies using Poetry.
    ```bash
    ./setup.sh
    ```

3.  **Run Tests**:
    To ensure that everything is set up correctly, run the test suite:
    ```bash
    poetry run pytest
    ```

## Usage

Clinical Data Study Buddy provides both a command-line interface (CLI) and a web-based user interface (UI).

### Web UI

To run the web UI, use the following command:

```bash
poetry run uvicorn clinical_data_study_buddy.web.main:app --reload
```

Then, open your web browser and navigate to `http://127.0.0.1:8000`.

### Command-Line Interface (CLI)

The CLI is organized into subcommands for different functionalities. You can get more information about each subcommand by using the `--help` flag.

```bash
poetry run cdsb --help
```

#### Examples

Here are some examples of how to use the CLI:

*   **Generate a TFL shell document**:
    ```bash
    poetry run cdsb generate tfl-shell --spec "My TFL Spec" --output-file my_tfl_shell.txt
    ```

*   **Generate a raw dataset package**:
    ```bash
    poetry run cdsb generate edc-raw-dataset-package --domains DM AE VS --num-subjects 20 --output-dir my_package
    ```

*   **Generate synthetic data for the DM domain**:
    ```bash
    poetry run cdsb generate synthetic-data --standard sdtmig --version 3-3 --domain DM --num-subjects 10
    ```

*   **Generate analysis code for a demographics table**:
    ```bash
    poetry run cdsb generate analysis-code --language sas --dataset ADSL --output-type Demographics --treatment-var TRT01A --output-file demo.sas
    ```

*   **Download the SDTMIG 3.3 standard**:
    ```bash
    poetry run cdsb download standard --standard sdtmig --version 3-3 --output-dir standards
    ```

*   **Generate a Study Data Reviewer's Guide (SDRG)**:
    ```bash
    poetry run cdsb sdrg generate --config examples/study_config.json --out sdrg.docx
    ```

## CDISC Library Client

The `src/cdisc_library_client` directory contains a Python client for the CDISC Library API. This client is auto-generated from the OpenAPI specification file located at `docs/openapi/cdisc-library.json` using the `openapi-python-client` tool.

### Regenerating the Client

If you make changes to the OpenAPI specification, you will need to regenerate the client. You can do this by running the following script from the root of the repository:

```bash
poetry run python scripts/generate_client.py
```

This script will update the client code in `src/cdisc_library_client` to reflect the changes in the OpenAPI specification.

## Contributing

We welcome contributions to the project! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
