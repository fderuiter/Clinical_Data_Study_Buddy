from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportQrsResponses")


@_attrs_define
class ExportQrsResponses:
    """
    Attributes:
        response_group (Union[Unset, str]):
        sequence (Union[Unset, str]):
        responses_original_result_codelist_c_code (Union[Unset, str]):
        responses_original_result_term_c_code (Union[Unset, str]):
        responses_original_result_unit_codelist_c_code (Union[Unset, str]):
        responses_original_result_unit_term_c_code (Union[Unset, str]):
        responses_standardized_result_codelist_c_code (Union[Unset, str]):
        responses_standardized_result_term_c_code (Union[Unset, str]):
        responses_standardized_result_unit_codelist_c_code (Union[Unset, str]):
        responses_standardized_result_unit_term_c_code (Union[Unset, str]):
    """

    response_group: Union[Unset, str] = UNSET
    sequence: Union[Unset, str] = UNSET
    responses_original_result_codelist_c_code: Union[Unset, str] = UNSET
    responses_original_result_term_c_code: Union[Unset, str] = UNSET
    responses_original_result_unit_codelist_c_code: Union[Unset, str] = UNSET
    responses_original_result_unit_term_c_code: Union[Unset, str] = UNSET
    responses_standardized_result_codelist_c_code: Union[Unset, str] = UNSET
    responses_standardized_result_term_c_code: Union[Unset, str] = UNSET
    responses_standardized_result_unit_codelist_c_code: Union[Unset, str] = UNSET
    responses_standardized_result_unit_term_c_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_group = self.response_group

        sequence = self.sequence

        responses_original_result_codelist_c_code = self.responses_original_result_codelist_c_code

        responses_original_result_term_c_code = self.responses_original_result_term_c_code

        responses_original_result_unit_codelist_c_code = self.responses_original_result_unit_codelist_c_code

        responses_original_result_unit_term_c_code = self.responses_original_result_unit_term_c_code

        responses_standardized_result_codelist_c_code = self.responses_standardized_result_codelist_c_code

        responses_standardized_result_term_c_code = self.responses_standardized_result_term_c_code

        responses_standardized_result_unit_codelist_c_code = self.responses_standardized_result_unit_codelist_c_code

        responses_standardized_result_unit_term_c_code = self.responses_standardized_result_unit_term_c_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response_group is not UNSET:
            field_dict["Response Group"] = response_group
        if sequence is not UNSET:
            field_dict["Sequence"] = sequence
        if responses_original_result_codelist_c_code is not UNSET:
            field_dict["Response's Original Result Codelist C-Code"] = responses_original_result_codelist_c_code
        if responses_original_result_term_c_code is not UNSET:
            field_dict["Response's Original Result Term C-Code"] = responses_original_result_term_c_code
        if responses_original_result_unit_codelist_c_code is not UNSET:
            field_dict["Response's Original Result Unit Codelist C-Code"] = (
                responses_original_result_unit_codelist_c_code
            )
        if responses_original_result_unit_term_c_code is not UNSET:
            field_dict["Response's Original Result Unit Term C-Code"] = responses_original_result_unit_term_c_code
        if responses_standardized_result_codelist_c_code is not UNSET:
            field_dict["Response's Standardized Result Codelist C-Code"] = responses_standardized_result_codelist_c_code
        if responses_standardized_result_term_c_code is not UNSET:
            field_dict["Response's Standardized Result Term C-Code"] = responses_standardized_result_term_c_code
        if responses_standardized_result_unit_codelist_c_code is not UNSET:
            field_dict["Response's Standardized Result Unit Codelist C-Code"] = (
                responses_standardized_result_unit_codelist_c_code
            )
        if responses_standardized_result_unit_term_c_code is not UNSET:
            field_dict["Response's Standardized Result Unit Term C-Code"] = (
                responses_standardized_result_unit_term_c_code
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_group = d.pop("Response Group", UNSET)

        sequence = d.pop("Sequence", UNSET)

        responses_original_result_codelist_c_code = d.pop("Response's Original Result Codelist C-Code", UNSET)

        responses_original_result_term_c_code = d.pop("Response's Original Result Term C-Code", UNSET)

        responses_original_result_unit_codelist_c_code = d.pop("Response's Original Result Unit Codelist C-Code", UNSET)

        responses_original_result_unit_term_c_code = d.pop("Response's Original Result Unit Term C-Code", UNSET)

        responses_standardized_result_codelist_c_code = d.pop("Response's Standardized Result Codelist C-Code", UNSET)

        responses_standardized_result_term_c_code = d.pop("Response's Standardized Result Term C-Code", UNSET)

        responses_standardized_result_unit_codelist_c_code = d.pop(
            "Response's Standardized Result Unit Codelist C-Code", UNSET
        )

        responses_standardized_result_unit_term_c_code = d.pop("Response's Standardized Result Unit Term C-Code", UNSET)

        export_qrs_responses = cls(
            response_group=response_group,
            sequence=sequence,
            responses_original_result_codelist_c_code=responses_original_result_codelist_c_code,
            responses_original_result_term_c_code=responses_original_result_term_c_code,
            responses_original_result_unit_codelist_c_code=responses_original_result_unit_codelist_c_code,
            responses_original_result_unit_term_c_code=responses_original_result_unit_term_c_code,
            responses_standardized_result_codelist_c_code=responses_standardized_result_codelist_c_code,
            responses_standardized_result_term_c_code=responses_standardized_result_term_c_code,
            responses_standardized_result_unit_codelist_c_code=responses_standardized_result_unit_codelist_c_code,
            responses_standardized_result_unit_term_c_code=responses_standardized_result_unit_term_c_code,
        )

        export_qrs_responses.additional_properties = d
        return export_qrs_responses

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
