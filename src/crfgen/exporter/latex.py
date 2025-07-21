from pathlib import Path
from typing import List
from jinja2 import Environment, FileSystemLoader
from ..schema import Form
from .registry import register

env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent / "templates"))

@register("tex")
def render_tex(forms: List[Form], out_dir: Path):
    out_dir.mkdir(exist_ok=True, parents=True)
    tpl = env.get_template("latex.j2")
    for f in forms:
        (out_dir / f"{f.domain}.tex").write_text(tpl.render(form=f))
