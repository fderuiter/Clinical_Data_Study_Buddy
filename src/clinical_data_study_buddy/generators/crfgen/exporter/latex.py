"""
This module provides the functionality to export CRF (Case Report Form) data
to LaTeX (.tex) files using Jinja2 templates.
"""

from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader

from clinical_data_study_buddy.core.models.schema import Form

from .registry import register

env = Environment(loader=FileSystemLoader("templates/crfgen"))


@register("tex")
def render_tex(forms: Sequence[Form], out_dir: Path):
    """
    Renders a sequence of Form objects to .tex files.

    This function uses a Jinja2 template to generate a LaTeX file for each
    form in the sequence.

    Args:
        forms (Sequence[Form]): A sequence of Form objects to be rendered.
        out_dir (Path): The output directory where the .tex files will be saved.
    """
    out_dir.mkdir(exist_ok=True, parents=True)
    tpl = env.get_template("latex.j2")
    for f in forms:
        (out_dir / f"{f.domain}.tex").write_text(tpl.render(form=f))
