import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Sequence

from crfgen.schema import Form

from .registry import register


@register("odm")
def export_odm(forms: Sequence[Form], outdir: Path) -> None:
    root = ET.Element("ODM")
    for form in forms:
        form_el = ET.SubElement(root, "FormDef", OID=form.domain, Name=form.title)
        for fld in form.fields:
            ET.SubElement(form_el, "ItemRef", OID=fld.oid)
    tree = ET.ElementTree(root)
    tree.write(outdir / "forms.xml", encoding="utf-8", xml_declaration=True)
