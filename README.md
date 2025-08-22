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

