# CDISC CRF Generator

This project provides tools for generating Case Report Forms (CRFs) using metadata from the CDISC Library.

Additional documentation is available in the [docs](docs/) directory, including an [FAQ](docs/FAQ.md) about accessing and using the CDISC Library.

Utility helpers such as `cdisc_library_client.normalize_headers()` are provided
to sanitize HTTP headers before requests are made. This avoids issues when
secrets are supplied as bytes.

