"""
This module provides the functionality to export CRF (Case Report Form) data
to a CSV file.
"""
import csv
from pathlib import Path
from typing import Sequence

from clinical_data_study_buddy.core.models.schema import Form

from .registry import register


@register("csv")
def export_csv(forms: Sequence[Form], outdir: Path) -> None:
    """
    Exports a sequence of Form objects to a CSV file.

    The resulting CSV file will contain the domain, OID, and prompt for each
    field in each form.

    Args:
        forms (Sequence[Form]): A sequence of Form objects to be exported.
        outdir (Path): The output directory where the CSV file will be saved.
    """
    path = outdir / "forms.csv"
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["domain", "oid", "prompt"])
        for form in forms:
            for fld in form.fields:
                writer.writerow([form.domain, fld.oid, fld.prompt])
