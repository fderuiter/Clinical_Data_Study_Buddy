#!/usr/bin/env python
"""Generate MS Word CRFs from CDASH metadata workbooks."""

import argparse
import pathlib

import pandas as pd
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Inches


def _add_page_field(paragraph):
    """Insert a Word page number field into *paragraph*."""
    run = paragraph.add_run()
    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")
    run._r.append(fld_char_begin)

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    run._r.append(instr)

    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_char_end)


def load_ig(ig_path: str) -> pd.DataFrame:
    """Load and normalise the *Variables* worksheet."""
    ig_df = pd.read_excel(ig_path, sheet_name="Variables", engine="openpyxl")
    ig_df = ig_df[~ig_df["Domain"].isna()].copy()
    ig_df["Display Label"] = ig_df["Question Text"].fillna(
        ig_df["CDASHIG Variable Label"]
    )
    ig_df.rename(
        columns={
            "CDASHIG Variable": "Variable",
            "Variable Order": "Order",
            "Case Report Form Completion Instructions": "CRF Instructions",
            "CDISC CT Codelist Submission Values(s), Subset Submission Value(s)": "CT Values",
            "CDISC CT Codelist Code(s), Subset Codes(s)": "CT Codes",
        },
        inplace=True,
    )
    return ig_df


def build_domain_crf(
    domain_df: pd.DataFrame, domain: str, out_dir: pathlib.Path
) -> None:
    """Create a Word document for a single CDASH domain."""

    document = Document()
    # Fixed column widths (inches) to keep tables aligned across pages
    col_widths = [
        Inches(1.0),
        Inches(3.0),
        Inches(0.9),
        Inches(2.0),
        Inches(1.3),
        Inches(2.2),
        Inches(0.5),  # reserved/unused
    ]

    # Use landscape orientation for readability
    section = document.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width, section.page_height = section.page_height, section.page_width

    # Standardise font
    style = document.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(10)

    # Header placeholders for protocol metadata
    hdr_width = section.page_width - section.left_margin - section.right_margin
    hdr_tbl = section.header.add_table(rows=1, cols=3, width=hdr_width)
    hdr_tbl.style = "Table Grid"
    hdr_cells = hdr_tbl.rows[0].cells
    hdr_cells[0].text = "Protocol ID: __________"
    hdr_cells[1].text = "Site Code: __________"
    hdr_cells[2].text = "Subject ID: __________"

    # Footer with version and automatic page numbering
    f_p = section.footer.add_paragraph("CRF Version 1.0 ")
    _add_page_field(f_p)
    f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    document.add_heading(f"{domain} Domain CRF", level=1)

    # Add a table with extra metadata columns to provide more context
    table = document.add_table(rows=1, cols=6, style="Table Grid")
    table.autofit = False
    hdr = table.rows[0].cells
    hdr[0].text = "Variable"
    hdr[1].text = "Label / Question"
    hdr[2].text = "Type"
    hdr[3].text = "Controlled Terminology"
    hdr[4].text = "Data Entry"
    hdr[5].text = "Instructions"
    for i, width in enumerate(col_widths[: len(hdr)]):
        hdr[i].width = width

    for _, row in domain_df.sort_values("Order").iterrows():
        cells = table.add_row().cells
        for i, width in enumerate(col_widths[: len(cells)]):
            cells[i].width = width
        cells[0].text = row["Variable"]
        cells[1].text = str(row["Display Label"])
        cells[2].text = str(row.get("Type", ""))

        ct_val = row.get("CT Values")
        ct_code = row.get("CT Codes")
        if pd.notna(ct_val):
            ct = str(ct_val)
        elif pd.notna(ct_code):
            ct = str(ct_code)
        else:
            ct = ""
        cells[3].text = ct

        # Placeholder where data should be recorded
        cells[4].text = "_______________"

        instructions = []
        if pd.notna(row.get("CRF Instructions")):
            instructions.append(str(row.get("CRF Instructions")))
        if pd.notna(row.get("Implementation Notes")):
            instructions.append(str(row.get("Implementation Notes")))
        label_lower = str(row.get("Display Label", "")).lower()
        var_upper = row["Variable"].upper()
        if (
            "date" in label_lower
            or var_upper.endswith("DT")
            or var_upper.endswith("DAT")
        ):
            instructions.append("Format: dd/mm/yyyy")

        instr_para = cells[5].paragraphs[0]
        for idx, item in enumerate(instructions):
            run = instr_para.add_run(item)
            run.italic = True
            if idx < len(instructions) - 1:
                instr_para.add_run("\n")

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
