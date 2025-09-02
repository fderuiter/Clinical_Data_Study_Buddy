# CDISC Data Symphony

![Weekly Sync Status](https://github.com/fderuiter/cdisc_generators/actions/workflows/weekly-sync.yml/badge.svg)

CDISC Data Symphony is a set of tools for generating clinical study artifacts, including Case Report Forms (CRFs), synthetic datasets, analysis code, and more. It is designed to streamline the process of creating and managing clinical trial documentation and data, ensuring compliance with CDISC standards.

## Features

*   **CRF Generation**: Generate Case Report Forms (CRFs) in various formats (e.g., PDF, DOCX, CSV) from a specification.
*   **Synthetic Data Generation**: Create synthetic datasets for testing and validation purposes.
*   **Analysis Code Generation**: Generate analysis code (e.g., SAS, R) for statistical analysis.
*   **Study Protocol Generation**: Create study protocols from a template.
*   **OpenFDA Integration**: Integrate with the OpenFDA API to fetch data and generate reports.
*   **CLI and Web UI**: A command-line interface (CLI) for power users and a web-based user interface (UI) for ease of use.

## Installation

To use CDISC Data Symphony, you need to have Python 3.12+ and Poetry installed.

1.  **Install Python 3.12+**: Follow the instructions on the [official Python website](https://www.python.org/downloads/).
2.  **Install Poetry**: Follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Once you have Python and Poetry installed, you can clone the repository and install the dependencies:

```bash
git clone https://github.com/fderuiter/cdisc_generators.git
cd cdisc_generators
poetry install
```

## Development Setup

If you want to contribute to the project, you will need to set up a development environment.

1.  **Fork and Clone the Repository**:
    ```bash
    git clone https://github.com/<your-username>/cdisc_generators.git
    cd cdisc_generators
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

CDISC Data Symphony provides a command-line interface (CLI) for interacting with its features.

The CLI is organized into subcommands for different functionalities. You can get more information about each subcommand by using the `--help` flag.

```bash
poetry run cdisc --help
```

### Examples

Here are some examples of how to use the CLI:

*   **Generate a CRF**:
    ```bash
    poetry run cdisc generate crf --config examples/crf_config.yaml
    ```

*   **Generate synthetic data**:
    ```bash
    poetry run cdisc generate synthetic-data --config examples/study_config.json
    ```

*   **Download a CDISC standard**:
    ```bash
    poetry run cdisc download standard --name SDTMIG --version 3.3
    ```

## Contributing

We welcome contributions to the project! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
