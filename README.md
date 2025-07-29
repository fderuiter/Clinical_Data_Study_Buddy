# CDISC CRF Generator

This project provides tools for generating Case Report Forms (CRFs) using metadata from the CDISC Library.

Additional documentation is available in the [docs](docs/) directory, including an [FAQ](docs/FAQ.md) about accessing and using the CDISC Library.

Utility helpers such as `cdisc_library_client.normalize_headers()` are provided
to sanitize HTTP headers before requests are made. This avoids issues when
secrets are supplied as bytes.

## Generating CDASH CRFs

The repository includes `scripts/generate_cdash_crf.py` which converts the
official CDASH workbooks into Word documents—one per domain.  The script now
includes extra metadata from the IG such as variable type, any controlled
terminology and completion instructions.  It requires `pandas`, `python-docx`
and `openpyxl` which are already listed in the project dependencies.

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
study branding.

