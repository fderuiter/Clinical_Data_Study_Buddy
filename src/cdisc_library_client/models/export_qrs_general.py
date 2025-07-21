from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportQrsGeneral")


@_attrs_define
class ExportQrsGeneral:
    """
    Attributes:
        name (Union[Unset, str]):
        label (Union[Unset, str]):
        effective_date (Union[Unset, str]):
        description (Union[Unset, str]):
        type_ (Union[Unset, str]):
        categorys_codelist_c_code (Union[Unset, str]):
        categorys_term_c_code (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    categorys_codelist_c_code: Union[Unset, str] = UNSET
    categorys_term_c_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        effective_date = self.effective_date

        description = self.description

        type_ = self.type_

        categorys_codelist_c_code = self.categorys_codelist_c_code

        categorys_term_c_code = self.categorys_term_c_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if label is not UNSET:
            field_dict["Label"] = label
        if effective_date is not UNSET:
            field_dict["Effective Date"] = effective_date
        if description is not UNSET:
            field_dict["Description"] = description
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if categorys_codelist_c_code is not UNSET:
            field_dict["Category's Codelist C-Code"] = categorys_codelist_c_code
        if categorys_term_c_code is not UNSET:
            field_dict["Category's Term C-Code"] = categorys_term_c_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        label = d.pop("Label", UNSET)

        effective_date = d.pop("Effective Date", UNSET)

        description = d.pop("Description", UNSET)

        type_ = d.pop("Type", UNSET)

        categorys_codelist_c_code = d.pop("Category's Codelist C-Code", UNSET)

        categorys_term_c_code = d.pop("Category's Term C-Code", UNSET)

        export_qrs_general = cls(
            name=name,
            label=label,
            effective_date=effective_date,
            description=description,
            type_=type_,
            categorys_codelist_c_code=categorys_codelist_c_code,
            categorys_term_c_code=categorys_term_c_code,
        )

        export_qrs_general.additional_properties = d
        return export_qrs_general

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
