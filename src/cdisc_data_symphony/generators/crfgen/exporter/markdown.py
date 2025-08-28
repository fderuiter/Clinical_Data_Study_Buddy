from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader, select_autoescape

from cdisc_data_symphony.generators.crfgen.schema import Form
from .registry import register

env = Environment(
    loader=FileSystemLoader("templates/crfgen"),
    autoescape=select_autoescape(),
)


@register("md")
def render_md(forms: Sequence[Form], out_dir: Path):
    tpl = env.get_template("markdown.j2")
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in forms:
        (out_dir / f"{f.domain}.md").write_text(tpl.render(form=f))
