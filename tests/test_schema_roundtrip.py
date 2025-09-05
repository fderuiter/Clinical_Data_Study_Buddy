import pathlib

from cdisc_data_symphony.builder.crfgen.schema import FieldDef, Form, dump_forms, load_forms


def test_roundtrip(tmp_path: pathlib.Path):
    f = Form(
        title="VS",
        domain="VS",
        fields=[
            FieldDef(oid="VSORRES", prompt="Res", datatype="text", cdash_var="VSORRES")
        ],
    )
    tmp = tmp_path / "tmp.json"
    dump_forms([f], tmp)
    out = load_forms(tmp)
    assert out[0].title == "VS"
