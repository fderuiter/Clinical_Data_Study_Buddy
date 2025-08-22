from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportSdtmClassVariablesRow")


@_attrs_define
class ExportSdtmClassVariablesRow:
    """
    Attributes:
        version (Union[Unset, str]):
        variable_order (Union[Unset, str]):
        class_ (Union[Unset, str]):
        dataset_name (Union[Unset, str]):
        variable_name (Union[Unset, str]):
        variable_label (Union[Unset, str]):
        type_ (Union[Unset, str]):
        controlled_terms_codelist_or_format (Union[Unset, str]):
        role (Union[Unset, str]):
        role_description (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    variable_order: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    variable_name: Union[Unset, str] = UNSET
    variable_label: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    controlled_terms_codelist_or_format: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    role_description: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        variable_order = self.variable_order

        class_ = self.class_

        dataset_name = self.dataset_name

        variable_name = self.variable_name

        variable_label = self.variable_label

        type_ = self.type_

        controlled_terms_codelist_or_format = self.controlled_terms_codelist_or_format

        role = self.role

        role_description = self.role_description

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if variable_order is not UNSET:
            field_dict["Variable Order"] = variable_order
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if dataset_name is not UNSET:
            field_dict["Dataset Name"] = dataset_name
        if variable_name is not UNSET:
            field_dict["Variable Name"] = variable_name
        if variable_label is not UNSET:
            field_dict["Variable Label"] = variable_label
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if controlled_terms_codelist_or_format is not UNSET:
            field_dict["Controlled Terms, Codelist or Format"] = controlled_terms_codelist_or_format
        if role is not UNSET:
            field_dict["Role"] = role
        if role_description is not UNSET:
            field_dict["Role Description"] = role_description
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("Version", UNSET)

        variable_order = d.pop("Variable Order", UNSET)

        class_ = d.pop("Class", UNSET)

        dataset_name = d.pop("Dataset Name", UNSET)

        variable_name = d.pop("Variable Name", UNSET)

        variable_label = d.pop("Variable Label", UNSET)

        type_ = d.pop("Type", UNSET)

        controlled_terms_codelist_or_format = d.pop("Controlled Terms, Codelist or Format", UNSET)

        role = d.pop("Role", UNSET)

        role_description = d.pop("Role Description", UNSET)

        description = d.pop("Description", UNSET)

        export_sdtm_class_variables_row = cls(
            version=version,
            variable_order=variable_order,
            class_=class_,
            dataset_name=dataset_name,
            variable_name=variable_name,
            variable_label=variable_label,
            type_=type_,
            controlled_terms_codelist_or_format=controlled_terms_codelist_or_format,
            role=role,
            role_description=role_description,
            description=description,
        )

        export_sdtm_class_variables_row.additional_properties = d
        return export_sdtm_class_variables_row

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
