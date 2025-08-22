from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_datastructure_ref import AdamDatastructureRef
    from ..models.adam_product_ref import AdamProductRef


T = TypeVar("T", bound="AdamDatastructureLinks")


@_attrs_define
class AdamDatastructureLinks:
    """
    Attributes:
        self_ (Union[Unset, AdamDatastructureRef]):
        parent_product (Union[Unset, AdamProductRef]):
        prior_version (Union[Unset, AdamDatastructureRef]):
    """

    self_: Union[Unset, "AdamDatastructureRef"] = UNSET
    parent_product: Union[Unset, "AdamProductRef"] = UNSET
    prior_version: Union[Unset, "AdamDatastructureRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure_ref import AdamDatastructureRef
        from ..models.adam_product_ref import AdamProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, AdamDatastructureRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = AdamDatastructureRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, AdamProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = AdamProductRef.from_dict(_parent_product)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, AdamDatastructureRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = AdamDatastructureRef.from_dict(_prior_version)

        adam_datastructure_links = cls(
            self_=self_,
            parent_product=parent_product,
            prior_version=prior_version,
        )

        adam_datastructure_links.additional_properties = d
        return adam_datastructure_links

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
