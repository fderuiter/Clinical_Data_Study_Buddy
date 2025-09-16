# Quickstart

Follow these steps to set up the project and generate your first set of CRF artifacts.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fderuiter/Clinical_Data_Study_Buddy.git
    cd Clinical_Data_Study_Buddy
    ```

2.  **Set up the environment:**
    This project uses Poetry for dependency management. Make sure you have Python 3.12+ and Poetry installed.
    ```bash
    ./setup.sh
    ```

3.  **Configure your CDISC Library API Key:**
    You will need a primary subscription key from the CDISC Library. Once you have it, create a `.env` file in the root of the project with the following content:
    ```
    CDISC_PRIMARY_KEY="your-api-key-here"
    ```

4.  **Generate CDASH CRF documents:**
    This command generates Word CRF shells from the CDISC Library API for a specified CDASH-IG version.
    ```bash
    poetry run cdsb generate cdash-crf --ig-version "v2.3"
    ```

5.  **View the generated files:**
    The generated artifacts are now in the `crfs/` directory. You can open them to see the results. For example, on macOS, you could run:
    ```bash
    open crfs/AE.docx
    ```
