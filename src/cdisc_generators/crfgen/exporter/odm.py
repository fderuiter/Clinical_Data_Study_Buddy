from pathlib import Path
from typing import Sequence

import odmlib.odm_1_3_2.model as ODM

from cdisc_generators.crfgen.schema import Form
from .registry import register


@register("odm")
def render_odm(forms: Sequence[Form], out_dir: Path):
    """Render a list of forms to ODM-XML."""
    root = ODM.ODM(
        FileOID="cdisc-crf-gen.v0.1",
        Granularity="Metadata",
        FileType="Snapshot",
        CreationDateTime="2025-08-21T00:00:00",  # Placeholder
    )
    study = ODM.Study(OID="ST.CRFGEN")
    root.Study.append(study)

    mdv = ODM.MetaDataVersion(OID="MDV.1", Name="CRF Generation MetaDataVersion")
    study.MetaDataVersion.append(mdv)

    for f in forms:
        # TODO: The "Repeating" attribute is required by odmlib.
        # The information is not available in the Form model, so it's hardcoded to "No".
        # This should be revisited if the crawler can fetch this information.
        formdef = ODM.FormDef(OID=f"F.{f.domain}", Name=f.title, Repeating="No")
        mdv.FormDef.append(formdef)

    out_dir.mkdir(exist_ok=True, parents=True)
    output_path = out_dir / "forms.odm.xml"
    root.write_xml(str(output_path))
