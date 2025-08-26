from pathlib import Path
from typing import Sequence

import odmlib.odm_1_3_2.model as ODM

from cdisc_generators_api.cdisc_generators.crfgen.schema import Form
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
        formdef = ODM.FormDef(OID=f"F.{f.domain}", Name=f.title, Repeating="No")
        item_group_def = ODM.ItemGroupDef(OID=f"IG.{f.domain}", Name=f.title, Repeating="No")
        for field in f.fields:
            item_def = ODM.ItemDef(
                OID=f"IT.{field.oid}",
                Name=field.prompt,
                DataType=field.datatype,
            )
            if field.range_check:
                range_check = ODM.RangeCheck(Comparator="EQ")
                for check_value in field.range_check:
                    item = ODM.CheckValue()
                    item.text = check_value
                    range_check.CheckValue.append(item)
                item_def.RangeCheck.append(range_check)
            mdv.ItemDef.append(item_def)
            item_ref = ODM.ItemRef(ItemOID=f"IT.{field.oid}", Mandatory="No")
            item_group_def.ItemRef.append(item_ref)

        mdv.ItemGroupDef.append(item_group_def)
        formdef.ItemGroupRef.append(ODM.ItemGroupRef(ItemGroupOID=f"IG.{f.domain}", Mandatory="No"))
        mdv.FormDef.append(formdef)

    out_dir.mkdir(exist_ok=True, parents=True)
    output_path = out_dir / "forms.odm.xml"
    root.write_xml(str(output_path))
