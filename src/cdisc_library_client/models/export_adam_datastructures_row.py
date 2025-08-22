from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportAdamDatastructuresRow")


@_attrs_define
class ExportAdamDatastructuresRow:
    """
    Attributes:
        version (Union[Unset, str]):
        data_structure_name (Union[Unset, str]):
        dataset_name (Union[Unset, str]):
        dataset_label (Union[Unset, str]):
        dataset_description (Union[Unset, str]):
        class_ (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    data_structure_name: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    dataset_label: Union[Unset, str] = UNSET
    dataset_description: Union[Unset, str] = UNSET
    class_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        data_structure_name = self.data_structure_name

        dataset_name = self.dataset_name

        dataset_label = self.dataset_label

        dataset_description = self.dataset_description

        class_ = self.class_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if data_structure_name is not UNSET:
            field_dict["Data Structure Name"] = data_structure_name
        if dataset_name is not UNSET:
            field_dict["Dataset Name"] = dataset_name
        if dataset_label is not UNSET:
            field_dict["Dataset Label"] = dataset_label
        if dataset_description is not UNSET:
            field_dict["Dataset Description"] = dataset_description
        if class_ is not UNSET:
            field_dict["Class"] = class_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("Version", UNSET)

        data_structure_name = d.pop("Data Structure Name", UNSET)

        dataset_name = d.pop("Dataset Name", UNSET)

        dataset_label = d.pop("Dataset Label", UNSET)

        dataset_description = d.pop("Dataset Description", UNSET)

        class_ = d.pop("Class", UNSET)

        export_adam_datastructures_row = cls(
            version=version,
            data_structure_name=data_structure_name,
            dataset_name=dataset_name,
            dataset_label=dataset_label,
            dataset_description=dataset_description,
            class_=class_,
        )

        export_adam_datastructures_row.additional_properties = d
        return export_adam_datastructures_row

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
