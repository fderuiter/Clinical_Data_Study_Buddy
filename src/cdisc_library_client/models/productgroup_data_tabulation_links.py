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
    from ..models.productgroup_ref import ProductgroupRef
    from ..models.sdtm_product_ref_element import SdtmProductRefElement
    from ..models.sdtmig_product_ref_element import SdtmigProductRefElement
    from ..models.sendig_product_ref_element import SendigProductRefElement


T = TypeVar("T", bound="ProductgroupDataTabulationLinks")


@_attrs_define
class ProductgroupDataTabulationLinks:
    """
    Attributes:
        self_ (Union[Unset, ProductgroupRef]):
        sdtm (Union[Unset, list['SdtmProductRefElement']]):
        sdtmig (Union[Unset, list['SdtmigProductRefElement']]):
        sendig (Union[Unset, list['SendigProductRefElement']]):
    """

    self_: Union[Unset, "ProductgroupRef"] = UNSET
    sdtm: Union[Unset, list["SdtmProductRefElement"]] = UNSET
    sdtmig: Union[Unset, list["SdtmigProductRefElement"]] = UNSET
    sendig: Union[Unset, list["SendigProductRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        sdtm: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sdtm, Unset):
            sdtm = []
            for sdtm_item_data in self.sdtm:
                sdtm_item = sdtm_item_data.to_dict()
                sdtm.append(sdtm_item)

        sdtmig: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sdtmig, Unset):
            sdtmig = []
            for sdtmig_item_data in self.sdtmig:
                sdtmig_item = sdtmig_item_data.to_dict()
                sdtmig.append(sdtmig_item)

        sendig: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sendig, Unset):
            sendig = []
            for sendig_item_data in self.sendig:
                sendig_item = sendig_item_data.to_dict()
                sendig.append(sendig_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if sdtm is not UNSET:
            field_dict["sdtm"] = sdtm
        if sdtmig is not UNSET:
            field_dict["sdtmig"] = sdtmig
        if sendig is not UNSET:
            field_dict["sendig"] = sendig

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.productgroup_ref import ProductgroupRef
        from ..models.sdtm_product_ref_element import SdtmProductRefElement
        from ..models.sdtmig_product_ref_element import SdtmigProductRefElement
        from ..models.sendig_product_ref_element import SendigProductRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ProductgroupRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ProductgroupRef.from_dict(_self_)

        sdtm = []
        _sdtm = d.pop("sdtm", UNSET)
        for sdtm_item_data in _sdtm or []:
            sdtm_item = SdtmProductRefElement.from_dict(sdtm_item_data)

            sdtm.append(sdtm_item)

        sdtmig = []
        _sdtmig = d.pop("sdtmig", UNSET)
        for sdtmig_item_data in _sdtmig or []:
            sdtmig_item = SdtmigProductRefElement.from_dict(sdtmig_item_data)

            sdtmig.append(sdtmig_item)

        sendig = []
        _sendig = d.pop("sendig", UNSET)
        for sendig_item_data in _sendig or []:
            sendig_item = SendigProductRefElement.from_dict(sendig_item_data)

            sendig.append(sendig_item)

        productgroup_data_tabulation_links = cls(
            self_=self_,
            sdtm=sdtm,
            sdtmig=sdtmig,
            sendig=sendig,
        )

        productgroup_data_tabulation_links.additional_properties = d
        return productgroup_data_tabulation_links

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
