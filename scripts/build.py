#!/usr/bin/env python3
"""
Dispatch to each exporter to generate all formats from crf.json.
"""
import json
import sys
from pathlib import Path

import crfgen.exporter.csv  # noqa
import crfgen.exporter.docx  # noqa
import crfgen.exporter.latex  # noqa

# Import exporters to register them
import crfgen.exporter.markdown  # noqa
import crfgen.exporter.odm  # noqa
import crfgen.exporter.xlsx  # noqa
from crfgen.exporter import registry as reg
from crfgen.schema import Form


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        "-s",
        default="crf.json",
        help="Path to the canonical JSON",
    )
    parser.add_argument(
        "--outdir",
        "-o",
        default="artefacts",
        help="Directory to emit artifacts",
    )
    parser.add_argument(
        "--formats",
        "-f",
        nargs="+",
        default=reg.formats(),
        help="Which formats to generate",
    )
    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        sys.exit(f"ERROR: source file not found: {src}")

    with src.open() as fp:
        data = json.load(fp)
    forms = [Form(**d) for d in data]

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for fmt in args.formats:
        fn = reg.get(fmt)
        print(f"[build] Rendering {fmt} → {outdir}")
        fn(forms, outdir)


if __name__ == "__main__":
    main()
