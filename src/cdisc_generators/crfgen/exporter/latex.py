from pathlib import Path
from typing import Sequence

from jinja2 import Environment, FileSystemLoader

from cdisc_generators.crfgen.schema import Form
from .registry import register

env = Environment(loader=FileSystemLoader("src/cdisc_generators/crfgen/templates"))


@register("tex")
def render_tex(forms: Sequence[Form], out_dir: Path):
    out_dir.mkdir(exist_ok=True, parents=True)
    tpl = env.get_template("latex.j2")
    for f in forms:
        (out_dir / f"{f.domain}.tex").write_text(tpl.render(form=f))
