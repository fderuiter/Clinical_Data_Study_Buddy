# Generating CDASH CRFs

The repository includes a command to convert the official CDASH workbooks into Word documents—one per domain.  The command now adds extra metadata from the IG such as variable type, controlled terminology and completion instructions.  Generated CRFs use a consistent landscape layout with protocol information in the header and versioned footers with page numbers.

```bash
poetry run cdisc generate-cdash-crf --ig-version v2.3 --out ./crfs

# To build only specific domains
poetry run cdisc generate-cdash-crf --ig-version v2.3 --domains AE CM --out ./crfs
```
