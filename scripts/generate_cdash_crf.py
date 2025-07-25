#!/usr/bin/env python
"""Generate MS Word CRFs from CDASH metadata workbooks."""

import argparse
import pathlib

import pandas as pd
from docx import Document


def load_ig(ig_path: str) -> pd.DataFrame:
    """Load and normalise the *Variables* worksheet."""
    ig_df = pd.read_excel(ig_path, sheet_name="Variables", engine="openpyxl")
    ig_df = ig_df[~ig_df["Domain"].isna()].copy()
    ig_df["Display Label"] = ig_df["Question Text"].fillna(
        ig_df["CDASHIG Variable Label"]
    )
    ig_df.rename(
        columns={"CDASHIG Variable": "Variable", "Variable Order": "Order"},
        inplace=True,
    )
    return ig_df


def build_domain_crf(domain_df: pd.DataFrame, domain: str, out_dir: pathlib.Path) -> None:
    """Create a Word document for a single CDASH domain."""

    document = Document()
    document.add_heading(f"{domain} Domain CRF", level=1)

    table = document.add_table(rows=1, cols=3)
    hdr = table.rows[0].cells
    hdr[0].text = "Variable"
    hdr[1].text = "Label / Question"
    hdr[2].text = "Data Entry"

    for _, row in domain_df.sort_values("Order").iterrows():
        cells = table.add_row().cells
        cells[0].text = row["Variable"]
        cells[1].text = str(row["Display Label"])
        cells[2].text = "_______________________________"

    out_path = out_dir / f"{domain}_CRF.docx"
    document.save(out_path)
    print(f"\u2713 Saved {out_path.relative_to(out_dir.parent)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Word CRFs from CDASH metadata spreadsheets."
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Path to CDASH_Model_v1.3.xlsx (reserved for future use)",
    )
    parser.add_argument("--ig", required=True, help="Path to CDASHIG_v2.3.xlsx")
    parser.add_argument(
        "--out",
        default="crfs",
        help="Directory to save the generated Word documents",
    )
    parser.add_argument(
        "--domains",
        nargs="*",
        metavar="DOMAIN",
        help="Optional list of domains to generate (e.g. AE CM)",
    )
    args = parser.parse_args()

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    ig_df = load_ig(args.ig)

    target_domains = args.domains or ig_df["Domain"].unique()
    for dom in target_domains:
        dom_df = ig_df[ig_df["Domain"] == dom]
        if dom_df.empty:
            print(f"\u26a0 Domain {dom} not found in IG \u2013 skipped")
            continue
        build_domain_crf(dom_df, dom, out_dir)


if __name__ == "__main__":
    main()
