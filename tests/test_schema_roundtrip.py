from crfgen.schema import Form, FieldDef, dump_forms, load_forms
import tempfile, pathlib


def test_roundtrip():
    f = Form(
        title="VS",
        domain="VS",
        fields=[FieldDef(oid="VSORRES", prompt="Res", datatype="text", cdash_var="VSORRES")]
    )
    tmp = pathlib.Path(tempfile.mkdtemp()) / "tmp.json"
    dump_forms([f], tmp)
    out = load_forms(tmp)
    assert out[0].title == "VS"
