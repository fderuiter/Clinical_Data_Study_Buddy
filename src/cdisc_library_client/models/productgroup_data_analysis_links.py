from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_product_ref_element import AdamProductRefElement
    from ..models.productgroup_ref import ProductgroupRef


T = TypeVar("T", bound="ProductgroupDataAnalysisLinks")


@_attrs_define
class ProductgroupDataAnalysisLinks:
    """
    Attributes:
        self_ (Union[Unset, ProductgroupRef]):
        adam (Union[Unset, list['AdamProductRefElement']]):
    """

    self_: Union[Unset, "ProductgroupRef"] = UNSET
    adam: Union[Unset, list["AdamProductRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        adam: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.adam, Unset):
            adam = []
            for adam_item_data in self.adam:
                adam_item = adam_item_data.to_dict()
                adam.append(adam_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if adam is not UNSET:
            field_dict["adam"] = adam

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_product_ref_element import AdamProductRefElement
        from ..models.productgroup_ref import ProductgroupRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ProductgroupRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ProductgroupRef.from_dict(_self_)

        adam = []
        _adam = d.pop("adam", UNSET)
        for adam_item_data in _adam or []:
            adam_item = AdamProductRefElement.from_dict(adam_item_data)

            adam.append(adam_item)

        productgroup_data_analysis_links = cls(
            self_=self_,
            adam=adam,
        )

        productgroup_data_analysis_links.additional_properties = d
        return productgroup_data_analysis_links

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
