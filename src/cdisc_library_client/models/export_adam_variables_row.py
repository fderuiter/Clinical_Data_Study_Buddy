from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportAdamVariablesRow")


@_attrs_define
class ExportAdamVariablesRow:
    """
    Attributes:
        version (Union[Unset, str]):
        data_structure_name (Union[Unset, str]):
        dataset_name (Union[Unset, str]):
        variable_group (Union[Unset, str]):
        variable_name (Union[Unset, str]):
        variable_label (Union[Unset, str]):
        type_ (Union[Unset, str]):
        codelist_controlled_terms (Union[Unset, str]):
        core (Union[Unset, str]):
        cdisc_notes (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    data_structure_name: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    variable_group: Union[Unset, str] = UNSET
    variable_name: Union[Unset, str] = UNSET
    variable_label: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    codelist_controlled_terms: Union[Unset, str] = UNSET
    core: Union[Unset, str] = UNSET
    cdisc_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        data_structure_name = self.data_structure_name

        dataset_name = self.dataset_name

        variable_group = self.variable_group

        variable_name = self.variable_name

        variable_label = self.variable_label

        type_ = self.type_

        codelist_controlled_terms = self.codelist_controlled_terms

        core = self.core

        cdisc_notes = self.cdisc_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if data_structure_name is not UNSET:
            field_dict["Data Structure Name"] = data_structure_name
        if dataset_name is not UNSET:
            field_dict["Dataset Name"] = dataset_name
        if variable_group is not UNSET:
            field_dict["Variable Group"] = variable_group
        if variable_name is not UNSET:
            field_dict["Variable Name"] = variable_name
        if variable_label is not UNSET:
            field_dict["Variable Label"] = variable_label
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if codelist_controlled_terms is not UNSET:
            field_dict["Codelist/Controlled Terms"] = codelist_controlled_terms
        if core is not UNSET:
            field_dict["Core"] = core
        if cdisc_notes is not UNSET:
            field_dict["CDISC Notes"] = cdisc_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("Version", UNSET)

        data_structure_name = d.pop("Data Structure Name", UNSET)

        dataset_name = d.pop("Dataset Name", UNSET)

        variable_group = d.pop("Variable Group", UNSET)

        variable_name = d.pop("Variable Name", UNSET)

        variable_label = d.pop("Variable Label", UNSET)

        type_ = d.pop("Type", UNSET)

        codelist_controlled_terms = d.pop("Codelist/Controlled Terms", UNSET)

        core = d.pop("Core", UNSET)

        cdisc_notes = d.pop("CDISC Notes", UNSET)

        export_adam_variables_row = cls(
            version=version,
            data_structure_name=data_structure_name,
            dataset_name=dataset_name,
            variable_group=variable_group,
            variable_name=variable_name,
            variable_label=variable_label,
            type_=type_,
            codelist_controlled_terms=codelist_controlled_terms,
            core=core,
            cdisc_notes=cdisc_notes,
        )

        export_adam_variables_row.additional_properties = d
        return export_adam_variables_row

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
