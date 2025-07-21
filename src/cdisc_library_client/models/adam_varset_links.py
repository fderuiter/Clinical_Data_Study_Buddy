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
    from ..models.adam_datastructure_ref import AdamDatastructureRef
    from ..models.adam_product_ref import AdamProductRef
    from ..models.adam_varset_ref import AdamVarsetRef


T = TypeVar("T", bound="AdamVarsetLinks")


@_attrs_define
class AdamVarsetLinks:
    """
    Attributes:
        self_ (Union[Unset, AdamVarsetRef]):
        parent_product (Union[Unset, AdamProductRef]):
        parent_datastructure (Union[Unset, AdamDatastructureRef]):
        prior_version (Union[Unset, AdamVarsetRef]):
    """

    self_: Union[Unset, "AdamVarsetRef"] = UNSET
    parent_product: Union[Unset, "AdamProductRef"] = UNSET
    parent_datastructure: Union[Unset, "AdamDatastructureRef"] = UNSET
    prior_version: Union[Unset, "AdamVarsetRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_datastructure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_datastructure, Unset):
            parent_datastructure = self.parent_datastructure.to_dict()

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
        if parent_datastructure is not UNSET:
            field_dict["parentDatastructure"] = parent_datastructure
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure_ref import AdamDatastructureRef
        from ..models.adam_product_ref import AdamProductRef
        from ..models.adam_varset_ref import AdamVarsetRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, AdamVarsetRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = AdamVarsetRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, AdamProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = AdamProductRef.from_dict(_parent_product)

        _parent_datastructure = d.pop("parentDatastructure", UNSET)
        parent_datastructure: Union[Unset, AdamDatastructureRef]
        if isinstance(_parent_datastructure, Unset):
            parent_datastructure = UNSET
        else:
            parent_datastructure = AdamDatastructureRef.from_dict(_parent_datastructure)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, AdamVarsetRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = AdamVarsetRef.from_dict(_prior_version)

        adam_varset_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_datastructure=parent_datastructure,
            prior_version=prior_version,
        )

        adam_varset_links.additional_properties = d
        return adam_varset_links

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
