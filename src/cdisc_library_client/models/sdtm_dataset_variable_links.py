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
    from ..models.root_sdtm_dataset_variable_ref import RootSdtmDatasetVariableRef
    from ..models.sdtm_dataset_ref import SdtmDatasetRef
    from ..models.sdtm_dataset_variable_ref import SdtmDatasetVariableRef
    from ..models.sdtm_product_ref import SdtmProductRef


T = TypeVar("T", bound="SdtmDatasetVariableLinks")


@_attrs_define
class SdtmDatasetVariableLinks:
    """
    Attributes:
        self_ (Union[Unset, SdtmDatasetVariableRef]):
        parent_product (Union[Unset, SdtmProductRef]):
        parent_dataset (Union[Unset, SdtmDatasetRef]):
        root_item (Union[Unset, RootSdtmDatasetVariableRef]):
        prior_version (Union[Unset, SdtmDatasetVariableRef]):
    """

    self_: Union[Unset, "SdtmDatasetVariableRef"] = UNSET
    parent_product: Union[Unset, "SdtmProductRef"] = UNSET
    parent_dataset: Union[Unset, "SdtmDatasetRef"] = UNSET
    root_item: Union[Unset, "RootSdtmDatasetVariableRef"] = UNSET
    prior_version: Union[Unset, "SdtmDatasetVariableRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_dataset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_dataset, Unset):
            parent_dataset = self.parent_dataset.to_dict()

        root_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.root_item, Unset):
            root_item = self.root_item.to_dict()

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
        if parent_dataset is not UNSET:
            field_dict["parentDataset"] = parent_dataset
        if root_item is not UNSET:
            field_dict["rootItem"] = root_item
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_sdtm_dataset_variable_ref import RootSdtmDatasetVariableRef
        from ..models.sdtm_dataset_ref import SdtmDatasetRef
        from ..models.sdtm_dataset_variable_ref import SdtmDatasetVariableRef
        from ..models.sdtm_product_ref import SdtmProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SdtmDatasetVariableRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SdtmDatasetVariableRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SdtmProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SdtmProductRef.from_dict(_parent_product)

        _parent_dataset = d.pop("parentDataset", UNSET)
        parent_dataset: Union[Unset, SdtmDatasetRef]
        if isinstance(_parent_dataset, Unset):
            parent_dataset = UNSET
        else:
            parent_dataset = SdtmDatasetRef.from_dict(_parent_dataset)

        _root_item = d.pop("rootItem", UNSET)
        root_item: Union[Unset, RootSdtmDatasetVariableRef]
        if isinstance(_root_item, Unset):
            root_item = UNSET
        else:
            root_item = RootSdtmDatasetVariableRef.from_dict(_root_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SdtmDatasetVariableRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SdtmDatasetVariableRef.from_dict(_prior_version)

        sdtm_dataset_variable_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_dataset=parent_dataset,
            root_item=root_item,
            prior_version=prior_version,
        )

        sdtm_dataset_variable_links.additional_properties = d
        return sdtm_dataset_variable_links

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
