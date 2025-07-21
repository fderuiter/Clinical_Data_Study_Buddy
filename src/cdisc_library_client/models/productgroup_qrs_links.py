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
    from ..models.productgroup_ref import ProductgroupRef
    from ..models.qrs_ref_element import QrsRefElement


T = TypeVar("T", bound="ProductgroupQrsLinks")


@_attrs_define
class ProductgroupQrsLinks:
    """
    Attributes:
        self_ (Union[Unset, ProductgroupRef]):
        qrs (Union[Unset, list['QrsRefElement']]):
    """

    self_: Union[Unset, "ProductgroupRef"] = UNSET
    qrs: Union[Unset, list["QrsRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        qrs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.qrs, Unset):
            qrs = []
            for qrs_item_data in self.qrs:
                qrs_item = qrs_item_data.to_dict()
                qrs.append(qrs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if qrs is not UNSET:
            field_dict["qrs"] = qrs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.productgroup_ref import ProductgroupRef
        from ..models.qrs_ref_element import QrsRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ProductgroupRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ProductgroupRef.from_dict(_self_)

        qrs = []
        _qrs = d.pop("qrs", UNSET)
        for qrs_item_data in _qrs or []:
            qrs_item = QrsRefElement.from_dict(qrs_item_data)

            qrs.append(qrs_item)

        productgroup_qrs_links = cls(
            self_=self_,
            qrs=qrs,
        )

        productgroup_qrs_links.additional_properties = d
        return productgroup_qrs_links

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
