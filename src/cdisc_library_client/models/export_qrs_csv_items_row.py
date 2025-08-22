from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportQrsCsvItemsRow")


@_attrs_define
class ExportQrsCsvItemsRow:
    """
    Attributes:
        qrs_measure_name (Union[Unset, str]):
        qrs_measure_label (Union[Unset, str]):
        qrs_measure_type (Union[Unset, str]):
        item_sequence (Union[Unset, str]):
        test_name (Union[Unset, str]):
        item_text (Union[Unset, str]):
        tests_codelist_c_code (Union[Unset, str]):
        tests_term_c_code (Union[Unset, str]):
        test_codes_codelist_c_code (Union[Unset, str]):
        test_codes_term_c_code (Union[Unset, str]):
        subcategorys_codelist_c_code (Union[Unset, str]):
        subcategorys_term_c_code (Union[Unset, str]):
        evaluators_codelist_c_code (Union[Unset, str]):
        evaluators_term_c_code (Union[Unset, str]):
        free_form_responses_datatype (Union[Unset, str]):
        response_group (Union[Unset, str]):
    """

    qrs_measure_name: Union[Unset, str] = UNSET
    qrs_measure_label: Union[Unset, str] = UNSET
    qrs_measure_type: Union[Unset, str] = UNSET
    item_sequence: Union[Unset, str] = UNSET
    test_name: Union[Unset, str] = UNSET
    item_text: Union[Unset, str] = UNSET
    tests_codelist_c_code: Union[Unset, str] = UNSET
    tests_term_c_code: Union[Unset, str] = UNSET
    test_codes_codelist_c_code: Union[Unset, str] = UNSET
    test_codes_term_c_code: Union[Unset, str] = UNSET
    subcategorys_codelist_c_code: Union[Unset, str] = UNSET
    subcategorys_term_c_code: Union[Unset, str] = UNSET
    evaluators_codelist_c_code: Union[Unset, str] = UNSET
    evaluators_term_c_code: Union[Unset, str] = UNSET
    free_form_responses_datatype: Union[Unset, str] = UNSET
    response_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qrs_measure_name = self.qrs_measure_name

        qrs_measure_label = self.qrs_measure_label

        qrs_measure_type = self.qrs_measure_type

        item_sequence = self.item_sequence

        test_name = self.test_name

        item_text = self.item_text

        tests_codelist_c_code = self.tests_codelist_c_code

        tests_term_c_code = self.tests_term_c_code

        test_codes_codelist_c_code = self.test_codes_codelist_c_code

        test_codes_term_c_code = self.test_codes_term_c_code

        subcategorys_codelist_c_code = self.subcategorys_codelist_c_code

        subcategorys_term_c_code = self.subcategorys_term_c_code

        evaluators_codelist_c_code = self.evaluators_codelist_c_code

        evaluators_term_c_code = self.evaluators_term_c_code

        free_form_responses_datatype = self.free_form_responses_datatype

        response_group = self.response_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qrs_measure_name is not UNSET:
            field_dict["QRS Measure Name"] = qrs_measure_name
        if qrs_measure_label is not UNSET:
            field_dict["QRS Measure Label"] = qrs_measure_label
        if qrs_measure_type is not UNSET:
            field_dict["QRS Measure Type"] = qrs_measure_type
        if item_sequence is not UNSET:
            field_dict["Item Sequence"] = item_sequence
        if test_name is not UNSET:
            field_dict["Test Name"] = test_name
        if item_text is not UNSET:
            field_dict["Item Text"] = item_text
        if tests_codelist_c_code is not UNSET:
            field_dict["Test's Codelist C-Code"] = tests_codelist_c_code
        if tests_term_c_code is not UNSET:
            field_dict["Test's Term C-Code"] = tests_term_c_code
        if test_codes_codelist_c_code is not UNSET:
            field_dict["Test Code's Codelist C-Code"] = test_codes_codelist_c_code
        if test_codes_term_c_code is not UNSET:
            field_dict["Test Code's Term C-Code"] = test_codes_term_c_code
        if subcategorys_codelist_c_code is not UNSET:
            field_dict["Subcategory's Codelist C-Code"] = subcategorys_codelist_c_code
        if subcategorys_term_c_code is not UNSET:
            field_dict["Subcategory's Term C-Code"] = subcategorys_term_c_code
        if evaluators_codelist_c_code is not UNSET:
            field_dict["Evaluator's Codelist C-Code"] = evaluators_codelist_c_code
        if evaluators_term_c_code is not UNSET:
            field_dict["Evaluator's Term C-Code"] = evaluators_term_c_code
        if free_form_responses_datatype is not UNSET:
            field_dict["Free-form Response's Datatype"] = free_form_responses_datatype
        if response_group is not UNSET:
            field_dict["Response Group"] = response_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qrs_measure_name = d.pop("QRS Measure Name", UNSET)

        qrs_measure_label = d.pop("QRS Measure Label", UNSET)

        qrs_measure_type = d.pop("QRS Measure Type", UNSET)

        item_sequence = d.pop("Item Sequence", UNSET)

        test_name = d.pop("Test Name", UNSET)

        item_text = d.pop("Item Text", UNSET)

        tests_codelist_c_code = d.pop("Test's Codelist C-Code", UNSET)

        tests_term_c_code = d.pop("Test's Term C-Code", UNSET)

        test_codes_codelist_c_code = d.pop("Test Code's Codelist C-Code", UNSET)

        test_codes_term_c_code = d.pop("Test Code's Term C-Code", UNSET)

        subcategorys_codelist_c_code = d.pop("Subcategory's Codelist C-Code", UNSET)

        subcategorys_term_c_code = d.pop("Subcategory's Term C-Code", UNSET)

        evaluators_codelist_c_code = d.pop("Evaluator's Codelist C-Code", UNSET)

        evaluators_term_c_code = d.pop("Evaluator's Term C-Code", UNSET)

        free_form_responses_datatype = d.pop("Free-form Response's Datatype", UNSET)

        response_group = d.pop("Response Group", UNSET)

        export_qrs_csv_items_row = cls(
            qrs_measure_name=qrs_measure_name,
            qrs_measure_label=qrs_measure_label,
            qrs_measure_type=qrs_measure_type,
            item_sequence=item_sequence,
            test_name=test_name,
            item_text=item_text,
            tests_codelist_c_code=tests_codelist_c_code,
            tests_term_c_code=tests_term_c_code,
            test_codes_codelist_c_code=test_codes_codelist_c_code,
            test_codes_term_c_code=test_codes_term_c_code,
            subcategorys_codelist_c_code=subcategorys_codelist_c_code,
            subcategorys_term_c_code=subcategorys_term_c_code,
            evaluators_codelist_c_code=evaluators_codelist_c_code,
            evaluators_term_c_code=evaluators_term_c_code,
            free_form_responses_datatype=free_form_responses_datatype,
            response_group=response_group,
        )

        export_qrs_csv_items_row.additional_properties = d
        return export_qrs_csv_items_row

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
