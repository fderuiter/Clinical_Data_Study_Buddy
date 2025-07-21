from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeValues")


@_attrs_define
class ScopeValues:
    """
    Attributes:
        total (Union[Unset, float]):  Example: 1.
        has_more (Union[Unset, bool]):
        values (Union[Unset, list[str]]):  Example: ['Terminology'].
    """

    total: Union[Unset, float] = UNSET
    has_more: Union[Unset, bool] = UNSET
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        has_more = self.has_more

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        has_more = d.pop("hasMore", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        scope_values = cls(
            total=total,
            has_more=has_more,
            values=values,
        )

        scope_values.additional_properties = d
        return scope_values

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
