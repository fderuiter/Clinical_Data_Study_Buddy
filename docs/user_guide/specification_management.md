# Specification Management

This project provides tools to generate and validate dataset specifications.

## Generating an Excel Specification

You can generate an Excel-based specification template for a given CDISC product and version.

```bash
poetry run cdsb generate specification-templates --product sdtmig --version 3-3 --domains DM --domains AE --domains VS
```

This will create a file named `sdtmig_3-3_spec.xlsx` with sheets for the DM, AE, and VS domains.

## Generating a Dataset from a Specification

Once you have a specification file, you can generate a synthetic dataset from it.

```bash
poetry run cdsb spec generate-dataset --spec-file sdtmig_3-3_spec.xlsx
```

This will generate CSV files for each domain (sheet) in the specification file.

## Validating a Dataset Against a Specification

You can also validate an existing dataset against a specification file.

```bash
poetry run cdsb spec validate --spec-file sdtmig_3-3_spec.xlsx --dataset-file sdtm_dm_20250822_215518.csv
```

This will check for missing/extra columns and data type mismatches.
