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
    from ..models.qrs_item_ref_element import QrsItemRefElement
    from ..models.qrs_items_ref import QrsItemsRef
    from ..models.qrs_product_ref import QrsProductRef


T = TypeVar("T", bound="QrsItemsLinks")


@_attrs_define
class QrsItemsLinks:
    """
    Attributes:
        self_ (Union[Unset, QrsItemsRef]):
        parent_product (Union[Unset, QrsProductRef]):
        items (Union[Unset, list['QrsItemRefElement']]):
    """

    self_: Union[Unset, "QrsItemsRef"] = UNSET
    parent_product: Union[Unset, "QrsProductRef"] = UNSET
    items: Union[Unset, list["QrsItemRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_item_ref_element import QrsItemRefElement
        from ..models.qrs_items_ref import QrsItemsRef
        from ..models.qrs_product_ref import QrsProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, QrsItemsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = QrsItemsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, QrsProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = QrsProductRef.from_dict(_parent_product)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = QrsItemRefElement.from_dict(items_item_data)

            items.append(items_item)

        qrs_items_links = cls(
            self_=self_,
            parent_product=parent_product,
            items=items,
        )

        qrs_items_links.additional_properties = d
        return qrs_items_links

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
