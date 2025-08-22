from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_variable import AdamVariable
    from ..models.adam_varset_links import AdamVarsetLinks


T = TypeVar("T", bound="AdamVarset")


@_attrs_define
class AdamVarset:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 1.
        name (Union[Unset, str]):  Example: ADSL.
        label (Union[Unset, str]):  Example: Subject-Level Analysis Dataset Structure.
        description (Union[Unset, str]):  Example: One record per subject..
        field_links (Union[Unset, AdamVarsetLinks]):
        analysis_variables (Union[Unset, list['AdamVariable']]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "AdamVarsetLinks"] = UNSET
    analysis_variables: Union[Unset, list["AdamVariable"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        analysis_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analysis_variables, Unset):
            analysis_variables = []
            for analysis_variables_item_data in self.analysis_variables:
                analysis_variables_item = analysis_variables_item_data.to_dict()
                analysis_variables.append(analysis_variables_item)

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
        if analysis_variables is not UNSET:
            field_dict["analysisVariables"] = analysis_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_variable import AdamVariable
        from ..models.adam_varset_links import AdamVarsetLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, AdamVarsetLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AdamVarsetLinks.from_dict(_field_links)

        analysis_variables = []
        _analysis_variables = d.pop("analysisVariables", UNSET)
        for analysis_variables_item_data in _analysis_variables or []:
            analysis_variables_item = AdamVariable.from_dict(analysis_variables_item_data)

            analysis_variables.append(analysis_variables_item)

        adam_varset = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
            analysis_variables=analysis_variables,
        )

        adam_varset.additional_properties = d
        return adam_varset

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
