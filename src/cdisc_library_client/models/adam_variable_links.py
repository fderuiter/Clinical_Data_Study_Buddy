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
    from ..models.adam_variable_ref import AdamVariableRef
    from ..models.adam_varset_ref import AdamVarsetRef
    from ..models.root_ct_codelist_ref import RootCtCodelistRef


T = TypeVar("T", bound="AdamVariableLinks")


@_attrs_define
class AdamVariableLinks:
    """
    Attributes:
        self_ (Union[Unset, AdamVariableRef]):
        codelist (Union[Unset, RootCtCodelistRef]):
        parent_product (Union[Unset, AdamProductRef]):
        parent_datastructure (Union[Unset, AdamDatastructureRef]):
        parent_variable_set (Union[Unset, AdamVarsetRef]):
        prior_version (Union[Unset, AdamVariableRef]):
    """

    self_: Union[Unset, "AdamVariableRef"] = UNSET
    codelist: Union[Unset, "RootCtCodelistRef"] = UNSET
    parent_product: Union[Unset, "AdamProductRef"] = UNSET
    parent_datastructure: Union[Unset, "AdamDatastructureRef"] = UNSET
    parent_variable_set: Union[Unset, "AdamVarsetRef"] = UNSET
    prior_version: Union[Unset, "AdamVariableRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        codelist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.codelist, Unset):
            codelist = self.codelist.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_datastructure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_datastructure, Unset):
            parent_datastructure = self.parent_datastructure.to_dict()

        parent_variable_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_variable_set, Unset):
            parent_variable_set = self.parent_variable_set.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if codelist is not UNSET:
            field_dict["codelist"] = codelist
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_datastructure is not UNSET:
            field_dict["parentDatastructure"] = parent_datastructure
        if parent_variable_set is not UNSET:
            field_dict["parentVariableSet"] = parent_variable_set
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure_ref import AdamDatastructureRef
        from ..models.adam_product_ref import AdamProductRef
        from ..models.adam_variable_ref import AdamVariableRef
        from ..models.adam_varset_ref import AdamVarsetRef
        from ..models.root_ct_codelist_ref import RootCtCodelistRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, AdamVariableRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = AdamVariableRef.from_dict(_self_)

        _codelist = d.pop("codelist", UNSET)
        codelist: Union[Unset, RootCtCodelistRef]
        if isinstance(_codelist, Unset):
            codelist = UNSET
        else:
            codelist = RootCtCodelistRef.from_dict(_codelist)

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

        _parent_variable_set = d.pop("parentVariableSet", UNSET)
        parent_variable_set: Union[Unset, AdamVarsetRef]
        if isinstance(_parent_variable_set, Unset):
            parent_variable_set = UNSET
        else:
            parent_variable_set = AdamVarsetRef.from_dict(_parent_variable_set)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, AdamVariableRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = AdamVariableRef.from_dict(_prior_version)

        adam_variable_links = cls(
            self_=self_,
            codelist=codelist,
            parent_product=parent_product,
            parent_datastructure=parent_datastructure,
            parent_variable_set=parent_variable_set,
            prior_version=prior_version,
        )

        adam_variable_links.additional_properties = d
        return adam_variable_links

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
