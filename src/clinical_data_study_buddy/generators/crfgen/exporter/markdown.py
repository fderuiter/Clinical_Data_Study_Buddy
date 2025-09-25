"""
This module provides the functionality to export CRF (Case Report Form) data
to Markdown (.md) files using Jinja2 templates.
"""

from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader, select_autoescape

from clinical_data_study_buddy.core.models.schema import Form

from .registry import register

env = Environment(
    loader=FileSystemLoader("templates/crfgen"),
    autoescape=select_autoescape(),
)


@register("md")
def render_md(forms: Sequence[Form], out_dir: Path):
    """
    Renders a sequence of Form objects to .md files.

    This function uses a Jinja2 template to generate a Markdown file for each
    form in the sequence.

    Args:
        forms (Sequence[Form]): A sequence of Form objects to be rendered.
        out_dir (Path): The output directory where the .md files will be saved.
    """
    tpl = env.get_template("markdown.j2")
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in forms:
        (out_dir / f"{f.domain}.md").write_text(tpl.render(form=f))
