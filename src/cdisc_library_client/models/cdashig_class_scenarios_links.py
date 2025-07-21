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
    from ..models.cdashig_class_scenarios_ref import CdashigClassScenariosRef
    from ..models.cdashig_scenario_ref_element import CdashigScenarioRefElement


T = TypeVar("T", bound="CdashigClassScenariosLinks")


@_attrs_define
class CdashigClassScenariosLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashigClassScenariosRef]):
        scenarios (Union[Unset, list['CdashigScenarioRefElement']]):
    """

    self_: Union[Unset, "CdashigClassScenariosRef"] = UNSET
    scenarios: Union[Unset, list["CdashigScenarioRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

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
        if scenarios is not UNSET:
            field_dict["scenarios"] = scenarios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_class_scenarios_ref import CdashigClassScenariosRef
        from ..models.cdashig_scenario_ref_element import CdashigScenarioRefElement

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashigClassScenariosRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashigClassScenariosRef.from_dict(_self_)

        scenarios = []
        _scenarios = d.pop("scenarios", UNSET)
        for scenarios_item_data in _scenarios or []:
            scenarios_item = CdashigScenarioRefElement.from_dict(scenarios_item_data)

            scenarios.append(scenarios_item)

        cdashig_class_scenarios_links = cls(
            self_=self_,
            scenarios=scenarios,
        )

        cdashig_class_scenarios_links.additional_properties = d
        return cdashig_class_scenarios_links

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
