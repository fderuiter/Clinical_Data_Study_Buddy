#!/usr/bin/env python
"""Generate artefacts in various formats from a CRF JSON file."""
import argparse
import importlib
from pathlib import Path

from crfgen.schema import load_forms
from crfgen.exporter import EXPORTERS

MODULE_MAP = {
    "md": "markdown",
}


def main() -> None:
    p = argparse.ArgumentParser(description="Build CRF artefacts")
    p.add_argument("--source", required=True, help="Path to forms JSON")
    p.add_argument("--outdir", required=True, help="Directory for output files")
    p.add_argument("--formats", nargs="+", required=True, help="Output formats")
    args = p.parse_args()

    forms = load_forms(args.source)
    out_dir = Path(args.outdir)

    for fmt in args.formats:
        # attempt to import exporter module dynamically
        mod_name = MODULE_MAP.get(fmt, fmt)
        try:
            importlib.import_module(f"crfgen.exporter.{mod_name}")
        except ModuleNotFoundError:
            pass
        exporter = EXPORTERS.get(fmt)
        if not exporter:
            raise SystemExit(f"Unknown format: {fmt}")
        exporter(forms, out_dir)


if __name__ == "__main__":
    main()
