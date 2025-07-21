from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DefaultSearchResponseHitsItem")


@_attrs_define
class DefaultSearchResponseHitsItem:
    """
    Example:
        {'name': 'STUDYID', 'product': 'SDTMIG v3.3', 'href': '/mdr/sdtmig/3-3/datasets/QS/variables/STUDYID', 'type':
            'SDTM Dataset Variable'}

    Attributes:
        href (str):
        type_ (str):
    """

    href: str
    type_: str
    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        type_ = d.pop("type")

        default_search_response_hits_item = cls(
            href=href,
            type_=type_,
        )

        default_search_response_hits_item.additional_properties = d
        return default_search_response_hits_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
