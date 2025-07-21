from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceBody")


@_attrs_define
class MaintenanceBody:
    """
    Attributes:
        maintenance_mode (Union[Unset, bool]):
        maintenance_message (Union[Unset, str]):
    """

    maintenance_mode: Union[Unset, bool] = UNSET
    maintenance_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_mode = self.maintenance_mode

        maintenance_message = self.maintenance_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if maintenance_message is not UNSET:
            field_dict["maintenanceMessage"] = maintenance_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maintenance_mode = d.pop("maintenanceMode", UNSET)

        maintenance_message = d.pop("maintenanceMessage", UNSET)

        maintenance_body = cls(
            maintenance_mode=maintenance_mode,
            maintenance_message=maintenance_message,
        )

        maintenance_body.additional_properties = d
        return maintenance_body

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
