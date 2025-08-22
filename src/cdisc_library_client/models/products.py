from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.products_links import ProductsLinks


T = TypeVar("T", bound="Products")


@_attrs_define
class Products:
    """
    Attributes:
        field_links (Union[Unset, ProductsLinks]):
    """

    field_links: Union[Unset, "ProductsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.products_links import ProductsLinks

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, ProductsLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ProductsLinks.from_dict(_field_links)

        products = cls(
            field_links=field_links,
        )

        products.additional_properties = d
        return products

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
