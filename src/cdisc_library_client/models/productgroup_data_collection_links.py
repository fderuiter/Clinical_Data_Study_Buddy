from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdash_product_ref_element import CdashProductRefElement
    from ..models.cdashig_product_ref_element import CdashigProductRefElement
    from ..models.productgroup_ref import ProductgroupRef


T = TypeVar("T", bound="ProductgroupDataCollectionLinks")


@_attrs_define
class ProductgroupDataCollectionLinks:
    """
    Attributes:
        self_ (Union[Unset, ProductgroupRef]):
        cdash (Union[Unset, list['CdashProductRefElement']]):
        cdashig (Union[Unset, list['CdashigProductRefElement']]):
    """

    self_: Union[Unset, "ProductgroupRef"] = UNSET
    cdash: Union[Unset, list["CdashProductRefElement"]] = UNSET
    cdashig: Union[Unset, list["CdashigProductRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        cdash: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cdash, Unset):
            cdash = []
            for cdash_item_data in self.cdash:
                cdash_item = cdash_item_data.to_dict()
                cdash.append(cdash_item)

        cdashig: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cdashig, Unset):
            cdashig = []
            for cdashig_item_data in self.cdashig:
                cdashig_item = cdashig_item_data.to_dict()
                cdashig.append(cdashig_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if cdash is not UNSET:
            field_dict["cdash"] = cdash
        if cdashig is not UNSET:
            field_dict["cdashig"] = cdashig

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_product_ref_element import CdashProductRefElement
        from ..models.cdashig_product_ref_element import CdashigProductRefElement
        from ..models.productgroup_ref import ProductgroupRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ProductgroupRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ProductgroupRef.from_dict(_self_)

        cdash = []
        _cdash = d.pop("cdash", UNSET)
        for cdash_item_data in _cdash or []:
            cdash_item = CdashProductRefElement.from_dict(cdash_item_data)

            cdash.append(cdash_item)

        cdashig = []
        _cdashig = d.pop("cdashig", UNSET)
        for cdashig_item_data in _cdashig or []:
            cdashig_item = CdashigProductRefElement.from_dict(cdashig_item_data)

            cdashig.append(cdashig_item)

        productgroup_data_collection_links = cls(
            self_=self_,
            cdash=cdash,
            cdashig=cdashig,
        )

        productgroup_data_collection_links.additional_properties = d
        return productgroup_data_collection_links

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
