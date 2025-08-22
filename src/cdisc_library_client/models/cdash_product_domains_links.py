from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdash_domain_ref_element import CdashDomainRefElement
    from ..models.cdash_product_domains_ref import CdashProductDomainsRef
    from ..models.cdash_product_ref import CdashProductRef


T = TypeVar("T", bound="CdashProductDomainsLinks")


@_attrs_define
class CdashProductDomainsLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashProductDomainsRef]):
        parent_product (Union[Unset, CdashProductRef]):
        domains (Union[Unset, list['CdashDomainRefElement']]):
    """

    self_: Union[Unset, "CdashProductDomainsRef"] = UNSET
    parent_product: Union[Unset, "CdashProductRef"] = UNSET
    domains: Union[Unset, list["CdashDomainRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        domains: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_domain_ref_element import CdashDomainRefElement
        from ..models.cdash_product_domains_ref import CdashProductDomainsRef
        from ..models.cdash_product_ref import CdashProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashProductDomainsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashProductDomainsRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, CdashProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = CdashProductRef.from_dict(_parent_product)

        domains = []
        _domains = d.pop("domains", UNSET)
        for domains_item_data in _domains or []:
            domains_item = CdashDomainRefElement.from_dict(domains_item_data)

            domains.append(domains_item)

        cdash_product_domains_links = cls(
            self_=self_,
            parent_product=parent_product,
            domains=domains,
        )

        cdash_product_domains_links.additional_properties = d
        return cdash_product_domains_links

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
