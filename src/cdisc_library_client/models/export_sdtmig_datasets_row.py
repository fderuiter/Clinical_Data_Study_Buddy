from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportSdtmigDatasetsRow")


@_attrs_define
class ExportSdtmigDatasetsRow:
    """
    Attributes:
        version (Union[Unset, str]):
        class_ (Union[Unset, str]):
        dataset_name (Union[Unset, str]):
        dataset_label (Union[Unset, str]):
        structure (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    dataset_label: Union[Unset, str] = UNSET
    structure: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        class_ = self.class_

        dataset_name = self.dataset_name

        dataset_label = self.dataset_label

        structure = self.structure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if dataset_name is not UNSET:
            field_dict["Dataset Name"] = dataset_name
        if dataset_label is not UNSET:
            field_dict["Dataset Label"] = dataset_label
        if structure is not UNSET:
            field_dict["Structure"] = structure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("Version", UNSET)

        class_ = d.pop("Class", UNSET)

        dataset_name = d.pop("Dataset Name", UNSET)

        dataset_label = d.pop("Dataset Label", UNSET)

        structure = d.pop("Structure", UNSET)

        export_sdtmig_datasets_row = cls(
            version=version,
            class_=class_,
            dataset_name=dataset_name,
            dataset_label=dataset_label,
            structure=structure,
        )

        export_sdtmig_datasets_row.additional_properties = d
        return export_sdtmig_datasets_row

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
