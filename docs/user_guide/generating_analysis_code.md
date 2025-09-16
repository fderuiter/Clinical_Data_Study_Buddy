# Generating Analysis Code

This project can also generate analysis code in SAS and R for various outputs.

## Quickstart

To generate an analysis script, use the `generate analysis-code` command. For example, to generate a SAS script for a demographics table from the ADSL dataset, run the following command:

```bash
poetry run cdsb generate analysis-code \
    --language sas \
    --dataset ADSL \
    --output-type Demographics \
    --treatment-var TRT01A \
    --output-file demog_table.sas
```

This will generate a SAS file named `demog_table.sas` in the current directory.
