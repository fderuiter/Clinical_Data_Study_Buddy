from cdisc_generators_api.cdisc_generators.data_generator import DataGenerator
from cdisc_generators_api.cdisc_generators.crfgen.schema import Form, FieldDef, Codelist

def test_generate():
    """
    Tests that the DataGenerator creates a dataset with the correct shape.
    """
    fields = [
        FieldDef(oid="USUBJID", prompt="Subject ID", datatype="text", cdash_var="USUBJID"),
        FieldDef(oid="AGE", prompt="Age", datatype="integer", cdash_var="AGE"),
    ]
    form_data = Form(title="DM", domain="DM", fields=fields)
    generator = DataGenerator(form_data)
    dataset = generator.generate(num_subjects=10)

    assert len(dataset) == 10
    assert len(dataset[0]) == 2
    assert "USUBJID" in dataset[0]
    assert "AGE" in dataset[0]

def test_generate_from_codelist():
    """
    Tests that the DataGenerator uses the codelist for generation.
    """
    codelist = Codelist(nci_code="C123", href="/codelists/C123")
    fields = [
        FieldDef(oid="SEX", prompt="Sex", datatype="text", cdash_var="SEX", codelist=codelist),
    ]
    form_data = Form(title="DM", domain="DM", fields=fields)
    generator = DataGenerator(form_data)
    dataset = generator.generate(num_subjects=1)

    assert dataset[0]["SEX"] == "C123"
