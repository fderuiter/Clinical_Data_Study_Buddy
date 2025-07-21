from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.default_search_response_hits_item import DefaultSearchResponseHitsItem


T = TypeVar("T", bound="DefaultSearchResponse")


@_attrs_define
class DefaultSearchResponse:
    """
    Attributes:
        hits (Union[Unset, list['DefaultSearchResponseHitsItem']]):
        total_hits (Union[Unset, float]):  Example: 1.
    """

    hits: Union[Unset, list["DefaultSearchResponseHitsItem"]] = UNSET
    total_hits: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hits, Unset):
            hits = []
            for hits_item_data in self.hits:
                hits_item = hits_item_data.to_dict()
                hits.append(hits_item)

        total_hits = self.total_hits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hits is not UNSET:
            field_dict["hits"] = hits
        if total_hits is not UNSET:
            field_dict["totalHits"] = total_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.default_search_response_hits_item import (
            DefaultSearchResponseHitsItem,
        )

        d = dict(src_dict)
        hits = []
        _hits = d.pop("hits", UNSET)
        for hits_item_data in _hits or []:
            hits_item = DefaultSearchResponseHitsItem.from_dict(hits_item_data)

            hits.append(hits_item)

        total_hits = d.pop("totalHits", UNSET)

        default_search_response = cls(
            hits=hits,
            total_hits=total_hits,
        )

        default_search_response.additional_properties = d
        return default_search_response

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
