from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_variable_links import AdamVariableLinks


T = TypeVar("T", bound="AdamVariable")


@_attrs_define
class AdamVariable:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 5.
        name (Union[Unset, str]):  Example: SITEGRy.
        label (Union[Unset, str]):  Example: Pooled Site Group y.
        description (Union[Unset, str]):  Example: Character description of a grouping or pooling of clinical sites for
            analysis purposes. For example, SITEGR3 is the name of a variable containing site group (pooled site) names,
            where the grouping has been done according to the third site grouping algorithm, defined in variable metadata;
            SITEGR3 does not mean the third group of sites..
        core (Union[Unset, str]):  Example: Perm.
        simple_datatype (Union[Unset, str]):  Example: Char.
        described_value_domain (Union[Unset, str]):  Example: Some codelist.
        value_list (Union[Unset, list[str]]):  Example: TODO.
        field_links (Union[Unset, AdamVariableLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    core: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    described_value_domain: Union[Unset, str] = UNSET
    value_list: Union[Unset, list[str]] = UNSET
    field_links: Union[Unset, "AdamVariableLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        core = self.core

        simple_datatype = self.simple_datatype

        described_value_domain = self.described_value_domain

        value_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = self.value_list

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
        if core is not UNSET:
            field_dict["core"] = core
        if simple_datatype is not UNSET:
            field_dict["simpleDatatype"] = simple_datatype
        if described_value_domain is not UNSET:
            field_dict["describedValueDomain"] = described_value_domain
        if value_list is not UNSET:
            field_dict["valueList"] = value_list
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_variable_links import AdamVariableLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        core = d.pop("core", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        described_value_domain = d.pop("describedValueDomain", UNSET)

        value_list = cast(list[str], d.pop("valueList", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, AdamVariableLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AdamVariableLinks.from_dict(_field_links)

        adam_variable = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            core=core,
            simple_datatype=simple_datatype,
            described_value_domain=described_value_domain,
            value_list=value_list,
            field_links=field_links,
        )

        adam_variable.additional_properties = d
        return adam_variable

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
