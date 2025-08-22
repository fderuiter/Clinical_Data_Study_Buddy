#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import exporters to register them
import src.crfgen.exporter.csv  # noqa
import src.crfgen.exporter.docx  # noqa
import src.crfgen.exporter.latex  # noqa
import src.crfgen.exporter.pdf  # noqa
import src.crfgen.exporter.rtf  # noqa
import src.crfgen.exporter.markdown  # noqa
import src.crfgen.exporter.odm  # noqa
import src.crfgen.exporter.xlsx  # noqa


from src.crfgen.tfl.tfl_generator import TFLGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate Tables, Figures, and Listings (TFLs).")
    parser.add_argument(
        "config_path",
        type=Path,
        help="Path to the TFL configuration file (JSON).",
    )
    args = parser.parse_args()

    if not args.config_path.is_file():
        print(f"Error: Configuration file not found at '{args.config_path}'")
        return

    with open(args.config_path, "r") as f:
        config = json.load(f)

    generator = TFLGenerator(config)
    generator.generate()


if __name__ == "__main__":
    main()
