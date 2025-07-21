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
    from ..models.cdashig_scenario_ref_element import CdashigScenarioRefElement


T = TypeVar("T", bound="CdashigDomainLinks")


@_attrs_define
class CdashigDomainLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashigDomainRef]):
        parent_product (Union[Unset, CdashigProductRef]):
        parent_class (Union[Unset, CdashigClassRef]):
        prior_version (Union[Unset, CdashigDomainRef]):
        scenarios (Union[Unset, list['CdashigScenarioRefElement']]):
    """

    self_: Union[Unset, "CdashigDomainRef"] = UNSET
    parent_product: Union[Unset, "CdashigProductRef"] = UNSET
    parent_class: Union[Unset, "CdashigClassRef"] = UNSET
    prior_version: Union[Unset, "CdashigDomainRef"] = UNSET
    scenarios: Union[Unset, list["CdashigScenarioRefElement"]] = UNSET
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

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        scenarios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scenarios, Unset):
            scenarios = []
            for scenarios_item_data in self.scenarios:
                scenarios_item = scenarios_item_data.to_dict()
                scenarios.append(scenarios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_class_ref import CdashigClassRef
        from ..models.cdashig_domain_ref import CdashigDomainRef
        from ..models.cdashig_product_ref import CdashigProductRef
        from ..models.cdashig_scenario_ref_element import CdashigScenarioRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashigDomainRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashigDomainRef.from_dict(_self_)

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

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CdashigDomainRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CdashigDomainRef.from_dict(_prior_version)

        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = CdashigScenarioRefElement.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        cdashig_domain_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_class=parent_class,
            prior_version=prior_version,
            scenarios=scenarios,
        )

        cdashig_domain_links.additional_properties = d
        return cdashig_domain_links

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
