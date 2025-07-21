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
    from ..models.sendig_dataset_ref_element import SendigDatasetRefElement
    from ..models.sendig_datasets_ref import SendigDatasetsRef
    from ..models.sendig_product_ref import SendigProductRef


T = TypeVar("T", bound="SendigDatasetsLinks")


@_attrs_define
class SendigDatasetsLinks:
    """
    Attributes:
        self_ (Union[Unset, SendigDatasetsRef]):
        parent_product (Union[Unset, SendigProductRef]):
        datasets (Union[Unset, list['SendigDatasetRefElement']]):
    """

    self_: Union[Unset, "SendigDatasetsRef"] = UNSET
    parent_product: Union[Unset, "SendigProductRef"] = UNSET
    datasets: Union[Unset, list["SendigDatasetRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

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
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sendig_dataset_ref_element import SendigDatasetRefElement
        from ..models.sendig_datasets_ref import SendigDatasetsRef
        from ..models.sendig_product_ref import SendigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SendigDatasetsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SendigDatasetsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SendigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SendigProductRef.from_dict(_parent_product)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = SendigDatasetRefElement.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        sendig_datasets_links = cls(
            self_=self_,
            parent_product=parent_product,
            datasets=datasets,
        )

        sendig_datasets_links.additional_properties = d
        return sendig_datasets_links

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
