from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_datastructure_varsets_ref import AdamDatastructureVarsetsRef
    from ..models.adam_product_ref import AdamProductRef
    from ..models.adam_varset_ref_element import AdamVarsetRefElement


T = TypeVar("T", bound="AdamDatastructureVarsetsLinks")


@_attrs_define
class AdamDatastructureVarsetsLinks:
    """
    Attributes:
        self_ (Union[Unset, AdamDatastructureVarsetsRef]):
        parent_product (Union[Unset, AdamProductRef]):
        prior_version (Union[Unset, AdamDatastructureVarsetsRef]):
        analysis_variable_sets (Union[Unset, list['AdamVarsetRefElement']]):
    """

    self_: Union[Unset, "AdamDatastructureVarsetsRef"] = UNSET
    parent_product: Union[Unset, "AdamProductRef"] = UNSET
    prior_version: Union[Unset, "AdamDatastructureVarsetsRef"] = UNSET
    analysis_variable_sets: Union[Unset, list["AdamVarsetRefElement"]] = UNSET
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

        analysis_variable_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analysis_variable_sets, Unset):
            analysis_variable_sets = []
            for analysis_variable_sets_item_data in self.analysis_variable_sets:
                analysis_variable_sets_item = analysis_variable_sets_item_data.to_dict()
                analysis_variable_sets.append(analysis_variable_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if analysis_variable_sets is not UNSET:
            field_dict["analysisVariableSets"] = analysis_variable_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure_varsets_ref import AdamDatastructureVarsetsRef
        from ..models.adam_product_ref import AdamProductRef
        from ..models.adam_varset_ref_element import AdamVarsetRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, AdamDatastructureVarsetsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = AdamDatastructureVarsetsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, AdamProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = AdamProductRef.from_dict(_parent_product)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, AdamDatastructureVarsetsRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = AdamDatastructureVarsetsRef.from_dict(_prior_version)

        analysis_variable_sets = []
        _analysis_variable_sets = d.pop("analysisVariableSets", UNSET)
        for analysis_variable_sets_item_data in _analysis_variable_sets or []:
            analysis_variable_sets_item = AdamVarsetRefElement.from_dict(analysis_variable_sets_item_data)

            analysis_variable_sets.append(analysis_variable_sets_item)

        adam_datastructure_varsets_links = cls(
            self_=self_,
            parent_product=parent_product,
            prior_version=prior_version,
            analysis_variable_sets=analysis_variable_sets,
        )

        adam_datastructure_varsets_links.additional_properties = d
        return adam_datastructure_varsets_links

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
