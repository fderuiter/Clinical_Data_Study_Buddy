from pathlib import Path
from typing import List
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ..schema import Form
from .registry import register

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent.parent / "templates"),
    autoescape=select_autoescape()
)

@register("md")
def render_md(forms: List[Form], out_dir: Path):
    tpl = env.get_template("markdown.j2")
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in forms:
        (out_dir / f"{f.domain}.md").write_text(tpl.render(form=f))
