import re
from cdisc_data_symphony.builder.data_generator import DataGenerator
from cdisc_data_symphony.builder.crfgen.schema import Form, FieldDef, Codelist

def test_generate():
    """
    Tests that the DataGenerator creates a dataset with the correct shape
    and uses the cdash_var as the column name.
    """
    fields = [
        FieldDef(oid="SUBJECT_ID", prompt="Subject ID", datatype="text", cdash_var="USUBJID"),
        FieldDef(oid="AGE_IN_YEARS", prompt="Age", datatype="integer", cdash_var="AGE"),
    ]
    form_data = Form(title="DM", domain="DM", fields=fields)
    generator = DataGenerator(form_data)
    dataset = generator.generate(num_subjects=10)

    assert len(dataset) == 10
    assert len(dataset[0]) == 2
    assert "USUBJID" in dataset[0]
    assert "AGE" in dataset[0]
    assert "SUBJECT_ID" not in dataset[0]
    assert "AGE_IN_YEARS" not in dataset[0]

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


def test_generate_date_format():
    """
    Tests that the DataGenerator generates a date in the correct format.
    """
    fields = [
        FieldDef(oid="BRTHDTC", prompt="Birth Date", datatype="date", cdash_var="BRTHDTC"),
    ]
    form_data = Form(title="DM", domain="DM", fields=fields)
    generator = DataGenerator(form_data)
    dataset = generator.generate(num_subjects=1)
    generated_date = dataset[0]["BRTHDTC"]

    assert "T" not in generated_date
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", generated_date)


def test_generate_text_with_length():
    """
    Tests that the DataGenerator generates text with a specific length.
    """
    fields = [
        FieldDef(oid="TEXT_FIELD", prompt="Text Field", datatype="text", cdash_var="TEXTVAR", length=20),
    ]
    form_data = Form(title="TEST", domain="TS", fields=fields)
    generator = DataGenerator(form_data)
    dataset = generator.generate(num_subjects=1)
    generated_text = dataset[0]["TEXTVAR"]

    assert len(generated_text) == 20
