from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.default_search_scopes import DefaultSearchScopes
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMdrSearchScopesResponse200")


@_attrs_define
class GetMdrSearchScopesResponse200:
    """
    Attributes:
        scopes (Union[Unset, list[DefaultSearchScopes]]):
    """

    scopes: Union[Unset, list[DefaultSearchScopes]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scopes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = DefaultSearchScopes(scopes_item_data)

            scopes.append(scopes_item)

        get_mdr_search_scopes_response_200 = cls(
            scopes=scopes,
        )

        get_mdr_search_scopes_response_200.additional_properties = d
        return get_mdr_search_scopes_response_200

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
