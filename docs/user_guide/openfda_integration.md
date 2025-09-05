# OpenFDA Integration

This project includes features to integrate data from [open.fda.gov](https://open.fda.gov/) to enrich the generated CRFs.

## Populating CRFs with Adverse Event Data

You can automatically populate the Adverse Events (AE) CRF with suggested terms for a specific drug. The `generate-cdash-crf` command has a new option to support this:

```bash
poetry run cdisc generate-cdash-crf \
    --ig-version v2.3 \
    --domains AE \
    --openfda-drug-name "Aspirin" \
    --openfda-max-results 50
```

This will fetch the top 50 most frequently reported adverse events for Aspirin from OpenFDA and add them to a separate table in the generated `AE_Adverse_Events_CRF.docx` document, providing a useful reference for common adverse events.

## Standalone OpenFDA Command

For more advanced queries, you can use the `openfda populate-crf` command. This command allows you to fetch adverse events or drug labeling information and output it in various formats.

### Examples

Fetch adverse events for a drug and save as JSON:
```bash
poetry run cdisc openfda populate-crf \
    --drug-name "Ibuprofen" \
    --domain AE \
    --max-results 100 \
    --output-format json > ibuprofen_aes.json
```

Fetch drug label information for a drug:
```bash
poetry run cdisc openfda populate-crf \
    --drug-name "Tylenol" \
    --domain LABEL
```
