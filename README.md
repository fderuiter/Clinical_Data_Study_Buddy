# CDISC CRF Generator

This project provides tools for generating Case Report Forms (CRFs) using metadata from the CDISC Library.

## Exporting artefacts

Use the `scripts/build.py` helper to generate files in various formats. For example, to create Markdown output:

```bash
python scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats md
```

To create LaTeX output instead, use `tex` as the format:

```bash
python scripts/build.py --source tests/.data/sample_crf.json --outdir artefacts --formats tex
```

The command will create one file per form in the given output directory.

Additional documentation is available in the [docs](docs/) directory, including an [FAQ](docs/FAQ.md) about accessing and using the CDISC Library.

