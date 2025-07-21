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
    from ..models.adam_datastructure_ref_element import AdamDatastructureRefElement
    from ..models.adam_product_datastructures_ref import AdamProductDatastructuresRef


T = TypeVar("T", bound="AdamProductDatastructuresLinks")


@_attrs_define
class AdamProductDatastructuresLinks:
    """
    Attributes:
        self_ (Union[Unset, AdamProductDatastructuresRef]):
        prior_version (Union[Unset, AdamProductDatastructuresRef]):
        data_structures (Union[Unset, list['AdamDatastructureRefElement']]):
    """

    self_: Union[Unset, "AdamProductDatastructuresRef"] = UNSET
    prior_version: Union[Unset, "AdamProductDatastructuresRef"] = UNSET
    data_structures: Union[Unset, list["AdamDatastructureRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        data_structures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_structures, Unset):
            data_structures = []
            for data_structures_item_data in self.data_structures:
                data_structures_item = data_structures_item_data.to_dict()
                data_structures.append(data_structures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if data_structures is not UNSET:
            field_dict["dataStructures"] = data_structures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure_ref_element import AdamDatastructureRefElement
        from ..models.adam_product_datastructures_ref import (
            AdamProductDatastructuresRef,
        )

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, AdamProductDatastructuresRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = AdamProductDatastructuresRef.from_dict(_self_)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, AdamProductDatastructuresRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = AdamProductDatastructuresRef.from_dict(_prior_version)

        data_structures = []
        _data_structures = d.pop("dataStructures", UNSET)
        for data_structures_item_data in _data_structures or []:
            data_structures_item = AdamDatastructureRefElement.from_dict(
                data_structures_item_data
            )

            data_structures.append(data_structures_item)

        adam_product_datastructures_links = cls(
            self_=self_,
            prior_version=prior_version,
            data_structures=data_structures,
        )

        adam_product_datastructures_links.additional_properties = d
        return adam_product_datastructures_links

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
