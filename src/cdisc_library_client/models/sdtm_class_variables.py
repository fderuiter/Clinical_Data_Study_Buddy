from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sdtm_class_variables_links import SdtmClassVariablesLinks


T = TypeVar("T", bound="SdtmClassVariables")


@_attrs_define
class SdtmClassVariables:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 1.
        name (Union[Unset, str]):  Example: General Observations.
        label (Union[Unset, str]):  Example: General Observation Class.
        description (Union[Unset, str]):  Example: The majority of observations collected during a study can be divided
            among three general classes: Interventions, Events, or Findings.  Datasets based on any of the general
            observation classes share a set of common Identifier and Timing variables. As a general rule, any valid
            Identifier or Timing variable is permissible for use in any submission dataset based on a general observation
            class. (Source: SDTM v1.8, Section 2.2).
        field_links (Union[Unset, SdtmClassVariablesLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SdtmClassVariablesLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_class_variables_links import SdtmClassVariablesLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SdtmClassVariablesLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SdtmClassVariablesLinks.from_dict(_field_links)

        sdtm_class_variables = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
        )

        sdtm_class_variables.additional_properties = d
        return sdtm_class_variables

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
