# Quickstart

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
