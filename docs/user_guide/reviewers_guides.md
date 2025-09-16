# Generating Reviewer's Guides

This project includes commands to generate an Analysis Data Reviewer's Guide (ADRG) and a Study Data Reviewer's Guide (SDRG). These guides are based on the PHUSE templates and are intended for FDA submissions.

## Prerequisites

Before generating the reviewer's guides, you need to have a `study_config.json` file.

The `study_config.json` file should be created manually and should contain study-specific information. See the example below:

```json
{
  "study_id": "ABC-123",
  "protocol_id": "XYZ-001",
  "protocol_title": "A Study to Evaluate the Efficacy and Safety of a New Drug"
}
```

## Generating the ADRG

To generate the ADRG, use the `adrg generate` command:

```bash
poetry run cdsb adrg generate \
    --config study_config.json \
    --out adrg.docx
```

## Generating the SDRG

To generate the SDRG, use the `sdrg generate` command:

```bash
poetry run cdsb sdrg generate \
    --config study_config.json \
    --out sdrg.docx
```
