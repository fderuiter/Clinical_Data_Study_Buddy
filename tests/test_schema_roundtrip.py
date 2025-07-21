from crfgen.schema import Form, FieldDef, dump_forms, load_forms
import pathlib
import tempfile


def test_roundtrip(tmp_path: pathlib.Path):
    f = Form(
        title="VS",
        domain="VS",
        fields=[FieldDef(oid="VSORRES", prompt="Res", datatype="text", cdash_var="VSORRES")]
    )
    tmp = tmp_path / "tmp.json"
    dump_forms([f], tmp)
    out = load_forms(tmp)
    assert out[0].title == "VS"
