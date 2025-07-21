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
    from ..models.sdtmig_class_datasets_ref import SdtmigClassDatasetsRef
    from ..models.sdtmig_dataset_ref_element import SdtmigDatasetRefElement
    from ..models.sdtmig_product_ref import SdtmigProductRef


T = TypeVar("T", bound="SdtmigClassDatasetsLinks")


@_attrs_define
class SdtmigClassDatasetsLinks:
    """
    Attributes:
        self_ (Union[Unset, SdtmigClassDatasetsRef]):
        parent_product (Union[Unset, SdtmigProductRef]):
        prior_version (Union[Unset, SdtmigClassDatasetsRef]):
        datasets (Union[Unset, list['SdtmigDatasetRefElement']]):
    """

    self_: Union[Unset, "SdtmigClassDatasetsRef"] = UNSET
    parent_product: Union[Unset, "SdtmigProductRef"] = UNSET
    prior_version: Union[Unset, "SdtmigClassDatasetsRef"] = UNSET
    datasets: Union[Unset, list["SdtmigDatasetRefElement"]] = UNSET
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

        datasets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtmig_class_datasets_ref import SdtmigClassDatasetsRef
        from ..models.sdtmig_dataset_ref_element import SdtmigDatasetRefElement
        from ..models.sdtmig_product_ref import SdtmigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SdtmigClassDatasetsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SdtmigClassDatasetsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SdtmigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SdtmigProductRef.from_dict(_parent_product)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SdtmigClassDatasetsRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SdtmigClassDatasetsRef.from_dict(_prior_version)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = SdtmigDatasetRefElement.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        sdtmig_class_datasets_links = cls(
            self_=self_,
            parent_product=parent_product,
            prior_version=prior_version,
            datasets=datasets,
        )

        sdtmig_class_datasets_links.additional_properties = d
        return sdtmig_class_datasets_links

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
