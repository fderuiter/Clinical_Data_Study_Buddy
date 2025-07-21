from pathlib import Path
from typing import List
import xml.etree.ElementTree as ET
from xml.dom import minidom

from ..schema import Form
from .registry import register


@register("odm")
def render_odm(forms: List[Form], out_dir: Path):
    odm = ET.Element("ODM", Description="Generated CRFs")
    study = ET.SubElement(odm, "Study", OID="ST.CRFGEN")
    mdv = ET.SubElement(study, "MetaDataVersion", OID="MDV.1")
    for f in forms:
        ET.SubElement(mdv, "FormDef", OID=f"F.{f.domain}", Name=f.title)
    out_dir.mkdir(exist_ok=True, parents=True)
    xml_str = ET.tostring(odm, encoding="utf-8")
    pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")
    (out_dir / "forms.odm.xml").write_text(pretty)
