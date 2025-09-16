# Generating Datasets

This project provides two main ways to generate datasets: synthetic datasets for a single domain, and a complete package of raw datasets for an EDC system.

## Generating Synthetic Datasets

In addition to generating CRFs from the CDISC Library, this project can also generate synthetic CDISC-compliant datasets.

### Quickstart

To generate a synthetic dataset, use the `generate synthetic-data` command. For example, to generate an SDTMIG dataset for the DM domain, run the following command:

```bash
poetry run cdsb generate synthetic-data \
    --standard sdtmig \
    --version 3-3 \
    --domain DM \
    --num-subjects 100 \
    --output-dir ./synthetic_data
```

This will generate a CSV file in the `synthetic_data` directory.

## Generating EDC Raw Dataset Package

This project includes a command to generate a complete package of raw EDC datasets for a clinical study. The command, `generate edc-raw-dataset-package`, generates a ZIP file containing multiple datasets with consistent subjects across all domains. It also includes a draft `define.xml` file (currently with limited metadata).

### Quickstart

To generate a raw dataset package, use the `generate edc-raw-dataset-package` command. For example, to generate a package with DM, VS, and LB domains for 10 subjects in the Oncology therapeutic area, run the following command:

```bash
poetry run cdsb generate edc-raw-dataset-package \
    --num-subjects 10 \
    --domains DM --domains VS --domains LB \
    --therapeutic-area Oncology \
    --output-dir ./raw_dataset_package
```

This will generate a `edc_raw_datasets.zip` file in the `raw_dataset_package` directory.
