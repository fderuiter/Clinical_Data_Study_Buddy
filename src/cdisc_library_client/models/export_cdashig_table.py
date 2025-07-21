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
    from ..models.export_cdashig_domain_variables_row import (
        ExportCdashigDomainVariablesRow,
    )
    from ..models.export_cdashig_scenario_variables_row import (
        ExportCdashigScenarioVariablesRow,
    )


T = TypeVar("T", bound="ExportCdashigTable")


@_attrs_define
class ExportCdashigTable:
    """
    Attributes:
        domain_variables (Union[Unset, list['ExportCdashigDomainVariablesRow']]):
        scenario_variables (Union[Unset, list['ExportCdashigScenarioVariablesRow']]):
    """

    domain_variables: Union[Unset, list["ExportCdashigDomainVariablesRow"]] = UNSET
    scenario_variables: Union[Unset, list["ExportCdashigScenarioVariablesRow"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.domain_variables, Unset):
            domain_variables = []
            for domain_variables_item_data in self.domain_variables:
                domain_variables_item = domain_variables_item_data.to_dict()
                domain_variables.append(domain_variables_item)

        scenario_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scenario_variables, Unset):
            scenario_variables = []
            for scenario_variables_item_data in self.scenario_variables:
                scenario_variables_item = scenario_variables_item_data.to_dict()
                scenario_variables.append(scenario_variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_variables is not UNSET:
            field_dict["domain-variables"] = domain_variables
        if scenario_variables is not UNSET:
            field_dict["scenario-variables"] = scenario_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_cdashig_domain_variables_row import (
            ExportCdashigDomainVariablesRow,
        )
        from ..models.export_cdashig_scenario_variables_row import (
            ExportCdashigScenarioVariablesRow,
        )

        d = dict(src_dict)
        domain_variables = []
        _domain_variables = d.pop("domain-variables", UNSET)
        for domain_variables_item_data in _domain_variables or []:
            domain_variables_item = ExportCdashigDomainVariablesRow.from_dict(
                domain_variables_item_data
            )

            domain_variables.append(domain_variables_item)

        scenario_variables = []
        _scenario_variables = d.pop("scenario-variables", UNSET)
        for scenario_variables_item_data in _scenario_variables or []:
            scenario_variables_item = ExportCdashigScenarioVariablesRow.from_dict(
                scenario_variables_item_data
            )

            scenario_variables.append(scenario_variables_item)

        export_cdashig_table = cls(
            domain_variables=domain_variables,
            scenario_variables=scenario_variables,
        )

        export_cdashig_table.additional_properties = d
        return export_cdashig_table

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
