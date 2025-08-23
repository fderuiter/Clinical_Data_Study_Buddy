---
title: "Repository Restructuring and Cleanup"
state: "closed"
labels:
  - "enhancement"
  - "refactoring"
assignees:
  - "Jules"
---

### Description

The root directory of the repository was cluttered with a mix of configuration files, generated artifacts, scripts, and source code. This made it difficult to navigate and understand the project structure. The goal of this task was to create a more logical and maintainable directory structure.

### Work Done

1.  **Created New Directories:**
    *   Created a `data/` directory to hold input data, specifications, and configuration files.
    *   Created an `output/` directory to hold all generated artifacts.

2.  **Moved Files and Directories:**
    *   Moved the following files to `data/`:
        *   `crf_config.yaml`
        *   `sdtmig_3-3_spec.xlsx`
        *   `study_config.json`
    *   Moved the following files and directories to `output/`:
        *   `adrg.docx`
        *   `sdrg.docx`
        *   `crf.json`
        *   `crfs/`
        *   `cli_output/`
        *   All `sdtm_*.csv` files

3.  **Updated `.gitignore`:**
    *   Cleaned up and simplified the `.gitignore` file.
    *   Removed redundant entries for specific output directories and file types.
    *   Ensured the entire `output/` directory is ignored to prevent generated files from being committed to version control.

### Status

This task is **complete**. The repository structure is now much cleaner and more organized.
