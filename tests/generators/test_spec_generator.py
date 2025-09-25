from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pandas as pd
import pytest

from clinical_data_study_buddy.generators.spec import (
    generate_dataset,
    generate_template,
    validate,
)


@pytest.fixture
def mock_cdisc_client():
    """Fixture for a mocked AuthenticatedClient."""
    return MagicMock()


# Tests for generate_template
@patch("clinical_data_study_buddy.generators.spec.get_client")
@patch("clinical_data_study_buddy.generators.spec.openpyxl.Workbook")
def test_generate_template_sdtmig(
    mock_workbook_class, mock_get_client, mock_cdisc_client
):
    # Arrange
    mock_get_client.return_value = mock_cdisc_client
    mock_workbook = MagicMock()
    mock_workbook_class.return_value = mock_workbook
    mock_sheet = MagicMock()
    mock_workbook.create_sheet.return_value = mock_sheet

    product = "sdtmig"
    version = "3-3"
    domains = ["DM"]
    output_dir = "output"

    mock_response = MagicMock()
    mock_response.to_dict.return_value = {
        "datasetVariables": [
            {
                "name": "STUDYID",
                "label": "Study Identifier",
                "simpleDatatype": "Char",
                "role": "Identifier",
                "core": "Req",
                "_links": {},
                "description": "Unique identifier for a study.",
            }
        ]
    }

    with patch(
        "clinical_data_study_buddy.generators.spec.get_mdr_sdtmig_version_datasets_dataset.sync",
        return_value=mock_response,
    ) as mock_api_call:
        # Act
        generate_template(product, version, domains, output_dir)

        # Assert
        mock_get_client.assert_called_once()
        mock_workbook.create_sheet.assert_called_once_with(title="DM")
        mock_api_call.assert_called_once_with(
            client=mock_cdisc_client, version=version, dataset="DM"
        )

        header = [
            "Variable Name",
            "Variable Label",
            "Data Type",
            "Role",
            "Core",
            "Codelist",
            "Description",
        ]
        row = [
            "STUDYID",
            "Study Identifier",
            "Char",
            "Identifier",
            "Req",
            "",
            "Unique identifier for a study.",
        ]

        mock_sheet.append.assert_has_calls([call(header), call(row)])
        output_path = Path(output_dir) / f"{product}_{version}_spec.xlsx"
        mock_workbook.save.assert_called_once_with(output_path)


# Tests for generate_dataset
@patch("clinical_data_study_buddy.generators.spec.openpyxl.load_workbook")
@patch("clinical_data_study_buddy.generators.spec.pd.read_excel")
@patch("clinical_data_study_buddy.generators.spec.DataGenerator")
@patch("clinical_data_study_buddy.generators.spec.pd.DataFrame.to_csv")
def test_generate_dataset(
    mock_to_csv, mock_data_generator_class, mock_read_excel, mock_load_workbook
):
    # Arrange
    spec_path = "spec.xlsx"
    output_dir = "output"

    mock_workbook = MagicMock()
    mock_workbook.sheetnames = ["DM", "AE"]
    mock_load_workbook.return_value = mock_workbook

    spec_df = pd.DataFrame(
        {
            "Variable Name": ["STUDYID"],
            "Variable Label": ["Study Identifier"],
            "Data Type": ["Char"],
        }
    )
    mock_read_excel.return_value = spec_df

    mock_data_generator = MagicMock()
    mock_data_generator.generate.return_value = [{"STUDYID": "TEST01"}]
    mock_data_generator_class.return_value = mock_data_generator

    # Act
    generate_dataset(spec_path, output_dir)

    # Assert
    assert mock_read_excel.call_count == 2
    assert mock_data_generator_class.call_count == 2

    # Check that DataGenerator was instantiated correctly for DM
    first_call_args = mock_data_generator_class.call_args_list[0][0][0]
    assert first_call_args.title == "DM"
    assert len(first_call_args.fields) == 1
    field_def = first_call_args.fields[0]
    assert field_def.oid == "STUDYID"
    assert field_def.prompt == "Study Identifier"
    assert field_def.datatype == "text"  # 'Char' should be mapped to 'text'
    assert field_def.cdash_var == "STUDYID"

    assert mock_data_generator.generate.call_count == 2
    mock_data_generator.generate.assert_called_with(num_subjects=50)

    assert mock_to_csv.call_count == 2
    dm_output_path = Path(output_dir) / "DM.csv"
    ae_output_path = Path(output_dir) / "AE.csv"
    mock_to_csv.assert_has_calls(
        [call(dm_output_path, index=False), call(ae_output_path, index=False)],
        any_order=True,
    )


# Tests for validate
@patch("clinical_data_study_buddy.generators.spec.pd.read_csv")
@patch("clinical_data_study_buddy.generators.spec.pd.read_excel")
@patch("builtins.print")
def test_validate_success(mock_print, mock_read_excel, mock_read_csv):
    # Arrange
    spec_path = "spec.xlsx"
    dataset_path = "DM.csv"

    spec_df = pd.DataFrame(
        {"Variable Name": ["STUDYID", "USUBJID"], "Data Type": ["Char", "Char"]}
    )
    dataset_df = pd.DataFrame({"STUDYID": ["TEST01"], "USUBJID": ["SUBJ-01"]})
    mock_read_excel.return_value = spec_df
    mock_read_csv.return_value = dataset_df

    # Act
    validate(spec_path, dataset_path)

    # Assert
    mock_print.assert_any_call(
        "\nValidation Successful: Dataset conforms to the specification."
    )


@patch("clinical_data_study_buddy.generators.spec.pd.read_csv")
@patch("clinical_data_study_buddy.generators.spec.pd.read_excel")
@patch("builtins.print")
def test_validate_missing_columns(mock_print, mock_read_excel, mock_read_csv):
    # Arrange
    spec_path = "spec.xlsx"
    dataset_path = "DM.csv"

    spec_df = pd.DataFrame(
        {"Variable Name": ["STUDYID", "USUBJID"], "Data Type": ["Char", "Char"]}
    )
    dataset_df = pd.DataFrame({"STUDYID": ["TEST01"]})
    mock_read_excel.return_value = spec_df
    mock_read_csv.return_value = dataset_df

    # Act
    validate(spec_path, dataset_path)

    # Assert
    mock_print.assert_any_call("\nValidation Warnings:")
    mock_print.assert_any_call(
        "- Missing columns in dataset that are in the spec: USUBJID"
    )


@patch("clinical_data_study_buddy.generators.spec.pd.read_csv")
@patch("clinical_data_study_buddy.generators.spec.pd.read_excel")
@patch("builtins.print")
def test_validate_extra_columns(mock_print, mock_read_excel, mock_read_csv):
    # Arrange
    spec_path = "spec.xlsx"
    dataset_path = "DM.csv"

    spec_df = pd.DataFrame({"Variable Name": ["STUDYID"], "Data Type": ["Char"]})
    dataset_df = pd.DataFrame({"STUDYID": ["TEST01"], "EXTRACOL": ["extra"]})
    mock_read_excel.return_value = spec_df
    mock_read_csv.return_value = dataset_df

    # Act
    validate(spec_path, dataset_path)

    # Assert
    mock_print.assert_any_call("\nValidation Failed:")
    mock_print.assert_any_call(
        "- Extra columns in dataset that are not in the spec: EXTRACOL"
    )


@patch("clinical_data_study_buddy.generators.spec.pd.read_csv")
@patch("clinical_data_study_buddy.generators.spec.pd.read_excel")
@patch("builtins.print")
def test_validate_dtype_error(mock_print, mock_read_excel, mock_read_csv):
    # Arrange
    spec_path = "spec.xlsx"
    dataset_path = "VS.csv"

    spec_df = pd.DataFrame({"Variable Name": ["VSSTRESN"], "Data Type": ["Num"]})
    dataset_df = pd.DataFrame({"VSSTRESN": ["not-a-number"]})
    mock_read_excel.return_value = spec_df
    mock_read_csv.return_value = dataset_df

    # Act
    validate(spec_path, dataset_path)

    # Assert
    mock_print.assert_any_call("\nValidation Failed:")
    mock_print.assert_any_call(
        "- Data type error in column 'VSSTRESN': Expected a numeric type."
    )


@patch("clinical_data_study_buddy.generators.spec.get_client")
@patch("clinical_data_study_buddy.generators.spec.openpyxl.Workbook")
def test_generate_template_adamig(
    mock_workbook_class, mock_get_client, mock_cdisc_client
):
    # Arrange
    mock_get_client.return_value = mock_cdisc_client
    mock_workbook = MagicMock()
    mock_workbook_class.return_value = mock_workbook
    mock_sheet = MagicMock()
    mock_workbook.create_sheet.return_value = mock_sheet

    product = "adamig"
    version = "1-1"
    domains = ["ADSL"]
    output_dir = "output"

    mock_response = MagicMock()
    mock_response.to_dict.return_value = {
        "analysisVariableSets": [
            {
                "analysisVariables": [
                    {
                        "name": "TRT01P",
                        "label": "Planned Treatment for Period 01",
                        "simpleDatatype": "Char",
                        "role": "Identifier",
                        "core": "Exp",
                        "_links": {},
                        "description": "Planned treatment for Period 01.",
                    }
                ]
            }
        ]
    }

    with patch(
        "clinical_data_study_buddy.generators.spec.get_mdr_adam_product_datastructures_structure.sync",
        return_value=mock_response,
    ) as mock_api_call:
        # Act
        generate_template(product, version, domains, output_dir)

        # Assert
        mock_get_client.assert_called_once()
        mock_workbook.create_sheet.assert_called_once_with(title="ADSL")
        adam_product_id = f"adamig-{version}"
        mock_api_call.assert_called_once_with(
            client=mock_cdisc_client, product=adam_product_id, structure="ADSL"
        )

        header = [
            "Variable Name",
            "Variable Label",
            "Data Type",
            "Role",
            "Core",
            "Codelist",
            "Description",
        ]
        row = [
            "TRT01P",
            "Planned Treatment for Period 01",
            "Char",
            "Identifier",
            "Exp",
            "",
            "Planned treatment for Period 01.",
        ]

        mock_sheet.append.assert_has_calls([call(header), call(row)])
        output_path = Path(output_dir) / f"{product}_{version}_spec.xlsx"
        mock_workbook.save.assert_called_once_with(output_path)


@patch("clinical_data_study_buddy.generators.spec.get_client")
@patch("clinical_data_study_buddy.generators.spec.openpyxl.Workbook")
def test_generate_template_no_variables(
    mock_workbook_class, mock_get_client, mock_cdisc_client
):
    # Arrange
    mock_get_client.return_value = mock_cdisc_client
    mock_workbook = MagicMock()
    mock_workbook_class.return_value = mock_workbook
    mock_sheet = MagicMock()
    mock_workbook.create_sheet.return_value = mock_sheet

    product = "sdtmig"
    version = "3-3"
    domains = ["DM"]
    output_dir = "output"

    mock_response = MagicMock()
    mock_response.to_dict.return_value = {"datasetVariables": []}

    with patch(
        "clinical_data_study_buddy.generators.spec.get_mdr_sdtmig_version_datasets_dataset.sync",
        return_value=mock_response,
    ):
        # Act
        generate_template(product, version, domains, output_dir)

        # Assert
        mock_sheet.append.assert_any_call(["No variables found for domain DM"])


@patch("clinical_data_study_buddy.generators.spec.get_client")
@patch("clinical_data_study_buddy.generators.spec.openpyxl.Workbook")
def test_generate_template_api_error(
    mock_workbook_class, mock_get_client, mock_cdisc_client
):
    # Arrange
    mock_get_client.return_value = mock_cdisc_client
    mock_workbook = MagicMock()
    mock_workbook_class.return_value = mock_workbook
    mock_sheet = MagicMock()
    mock_workbook.create_sheet.return_value = mock_sheet

    product = "sdtmig"
    version = "3-3"
    domains = ["DM"]
    output_dir = "output"

    with patch(
        "clinical_data_study_buddy.generators.spec.get_mdr_sdtmig_version_datasets_dataset.sync",
        side_effect=Exception("API Error"),
    ):
        # Act
        generate_template(product, version, domains, output_dir)

        # Assert
        mock_sheet.append.assert_any_call(["Error fetching data for DM"])


@patch("builtins.print")
def test_validate_invalid_filename(mock_print):
    # Act
    validate("spec.xlsx", "a_b_c_d.csv")

    # Assert
    mock_print.assert_any_call(
        "Invalid dataset filename format: a_b_c_d.csv. Expected '<product>_<domain>_<timestamp>.csv' or '<domain>.csv'."
    )


@patch(
    "clinical_data_study_buddy.generators.spec.pd.read_excel",
    side_effect=ValueError("Sheet not found"),
)
@patch("builtins.print")
def test_validate_sheet_not_found(mock_print, mock_read_excel):
    # Act
    validate("spec.xlsx", "DM.csv")

    # Assert
    mock_print.assert_any_call("Sheet 'DM' not found in the specification file.")
