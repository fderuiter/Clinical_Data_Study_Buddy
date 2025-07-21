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
    from ..models.sdtm_dataset_ref import SdtmDatasetRef
    from ..models.sdtmig_class_ref import SdtmigClassRef
    from ..models.sdtmig_dataset_ref import SdtmigDatasetRef
    from ..models.sdtmig_product_ref import SdtmigProductRef


T = TypeVar("T", bound="SdtmigDatasetLinks")


@_attrs_define
class SdtmigDatasetLinks:
    """
    Attributes:
        self_ (Union[Unset, SdtmigDatasetRef]):
        model_dataset (Union[Unset, SdtmDatasetRef]):
        parent_product (Union[Unset, SdtmigProductRef]):
        parent_class (Union[Unset, SdtmigClassRef]):
        prior_version (Union[Unset, SdtmigDatasetRef]):
    """

    self_: Union[Unset, "SdtmigDatasetRef"] = UNSET
    model_dataset: Union[Unset, "SdtmDatasetRef"] = UNSET
    parent_product: Union[Unset, "SdtmigProductRef"] = UNSET
    parent_class: Union[Unset, "SdtmigClassRef"] = UNSET
    prior_version: Union[Unset, "SdtmigDatasetRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        model_dataset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_dataset, Unset):
            model_dataset = self.model_dataset.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if model_dataset is not UNSET:
            field_dict["modelDataset"] = model_dataset
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_dataset_ref import SdtmDatasetRef
        from ..models.sdtmig_class_ref import SdtmigClassRef
        from ..models.sdtmig_dataset_ref import SdtmigDatasetRef
        from ..models.sdtmig_product_ref import SdtmigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SdtmigDatasetRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SdtmigDatasetRef.from_dict(_self_)

        _model_dataset = d.pop("modelDataset", UNSET)
        model_dataset: Union[Unset, SdtmDatasetRef]
        if isinstance(_model_dataset, Unset):
            model_dataset = UNSET
        else:
            model_dataset = SdtmDatasetRef.from_dict(_model_dataset)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SdtmigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SdtmigProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, SdtmigClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = SdtmigClassRef.from_dict(_parent_class)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SdtmigDatasetRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SdtmigDatasetRef.from_dict(_prior_version)

        sdtmig_dataset_links = cls(
            self_=self_,
            model_dataset=model_dataset,
            parent_product=parent_product,
            parent_class=parent_class,
            prior_version=prior_version,
        )

        sdtmig_dataset_links.additional_properties = d
        return sdtmig_dataset_links

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
