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
    from ..models.cdashig_class_ref import CdashigClassRef
    from ..models.cdashig_domain_ref import CdashigDomainRef
    from ..models.cdashig_product_ref import CdashigProductRef
    from ..models.cdashig_scenario_ref import CdashigScenarioRef


T = TypeVar("T", bound="CdashigScenarioLinks")


@_attrs_define
class CdashigScenarioLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashigScenarioRef]):
        parent_product (Union[Unset, CdashigProductRef]):
        parent_class (Union[Unset, CdashigClassRef]):
        parent_domain (Union[Unset, CdashigDomainRef]):
        prior_version (Union[Unset, CdashigScenarioRef]):
    """

    self_: Union[Unset, "CdashigScenarioRef"] = UNSET
    parent_product: Union[Unset, "CdashigProductRef"] = UNSET
    parent_class: Union[Unset, "CdashigClassRef"] = UNSET
    parent_domain: Union[Unset, "CdashigDomainRef"] = UNSET
    prior_version: Union[Unset, "CdashigScenarioRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        parent_domain: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_domain, Unset):
            parent_domain = self.parent_domain.to_dict()

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
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if parent_domain is not UNSET:
            field_dict["parentDomain"] = parent_domain
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_class_ref import CdashigClassRef
        from ..models.cdashig_domain_ref import CdashigDomainRef
        from ..models.cdashig_product_ref import CdashigProductRef
        from ..models.cdashig_scenario_ref import CdashigScenarioRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashigScenarioRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashigScenarioRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, CdashigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = CdashigProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, CdashigClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = CdashigClassRef.from_dict(_parent_class)

        _parent_domain = d.pop("parentDomain", UNSET)
        parent_domain: Union[Unset, CdashigDomainRef]
        if isinstance(_parent_domain, Unset):
            parent_domain = UNSET
        else:
            parent_domain = CdashigDomainRef.from_dict(_parent_domain)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CdashigScenarioRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CdashigScenarioRef.from_dict(_prior_version)

        cdashig_scenario_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_class=parent_class,
            parent_domain=parent_domain,
            prior_version=prior_version,
        )

        cdashig_scenario_links.additional_properties = d
        return cdashig_scenario_links

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
