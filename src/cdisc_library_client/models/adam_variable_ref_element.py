from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdamVariableRefElement")


@_attrs_define
class AdamVariableRefElement:
    """
    Attributes:
        href (Union[Unset, str]):  Example: /mdr/adam/adamig-1-1/datastructures/ADSL/variables/SITEGRy.
        title (Union[Unset, str]):  Example: Pooled Site Group y.
        type_ (Union[Unset, str]):  Example: Analysis Variable.
    """

    href: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        adam_variable_ref_element = cls(
            href=href,
            title=title,
            type_=type_,
        )

        adam_variable_ref_element.additional_properties = d
        return adam_variable_ref_element

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
