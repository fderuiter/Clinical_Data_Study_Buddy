from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CtPackageRefElement")


@_attrs_define
class CtPackageRefElement:
    """
    Attributes:
        href (Union[Unset, str]):  Example: /mdr/ct/packages/sdtmct-2019-12-20.
        title (Union[Unset, str]):  Example: SDTM Controlled Terminology Package 40 Effective 2019-12-20.
        type_ (Union[Unset, str]):  Example: Terminology.
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

        ct_package_ref_element = cls(
            href=href,
            title=title,
            type_=type_,
        )

        ct_package_ref_element.additional_properties = d
        return ct_package_ref_element

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
