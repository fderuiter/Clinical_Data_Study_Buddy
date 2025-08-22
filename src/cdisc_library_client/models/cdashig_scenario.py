from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdashig_scenario_field import CdashigScenarioField
    from ..models.cdashig_scenario_links import CdashigScenarioLinks


T = TypeVar("T", bound="CdashigScenario")


@_attrs_define
class CdashigScenario:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 19.
        domain (Union[Unset, str]):  Example: Vital Signs.
        scenario (Union[Unset, str]):  Example: VS - Implementation Options: HorizontalGeneric.
        field_links (Union[Unset, CdashigScenarioLinks]):
        fields (Union[Unset, list['CdashigScenarioField']]):
    """

    ordinal: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    scenario: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashigScenarioLinks"] = UNSET
    fields: Union[Unset, list["CdashigScenarioField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        domain = self.domain

        scenario = self.scenario

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if domain is not UNSET:
            field_dict["domain"] = domain
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_scenario_field import CdashigScenarioField
        from ..models.cdashig_scenario_links import CdashigScenarioLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        domain = d.pop("domain", UNSET)

        scenario = d.pop("scenario", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashigScenarioLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashigScenarioLinks.from_dict(_field_links)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CdashigScenarioField.from_dict(fields_item_data)

            fields.append(fields_item)

        cdashig_scenario = cls(
            ordinal=ordinal,
            domain=domain,
            scenario=scenario,
            field_links=field_links,
            fields=fields,
        )

        cdashig_scenario.additional_properties = d
        return cdashig_scenario

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
