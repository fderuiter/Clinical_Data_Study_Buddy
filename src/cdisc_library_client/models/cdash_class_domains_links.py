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
    from ..models.cdash_class_domains_ref import CdashClassDomainsRef
    from ..models.cdash_domain_ref_element import CdashDomainRefElement


T = TypeVar("T", bound="CdashClassDomainsLinks")


@_attrs_define
class CdashClassDomainsLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashClassDomainsRef]):
        domains (Union[Unset, list['CdashDomainRefElement']]):
    """

    self_: Union[Unset, "CdashClassDomainsRef"] = UNSET
    domains: Union[Unset, list["CdashDomainRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

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
        if domains is not UNSET:
            field_dict["domains"] = domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_domains_ref import CdashClassDomainsRef
        from ..models.cdash_domain_ref_element import CdashDomainRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashClassDomainsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashClassDomainsRef.from_dict(_self_)

        domains = []
        _domains = d.pop("domains", UNSET)
        for domains_item_data in _domains or []:
            domains_item = CdashDomainRefElement.from_dict(domains_item_data)

            domains.append(domains_item)

        cdash_class_domains_links = cls(
            self_=self_,
            domains=domains,
        )

        cdash_class_domains_links.additional_properties = d
        return cdash_class_domains_links

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
