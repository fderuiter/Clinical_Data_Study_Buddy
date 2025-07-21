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
    from ..models.sendig_dataset_variable_links import SendigDatasetVariableLinks


T = TypeVar("T", bound="SendigDatasetVariable")


@_attrs_define
class SendigDatasetVariable:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 8.
        name (Union[Unset, str]):  Example: VSTEST.
        label (Union[Unset, str]):  Example: Vital Signs Test Name.
        description (Union[Unset, str]):  Example: Long name for VSTESTCD. The value in VSTEST cannot be longer than 40
            characters..
        role (Union[Unset, str]):  Example: Synonym Qualifier.
        simple_datatype (Union[Unset, str]):  Example: Char.
        core (Union[Unset, str]):  Example: Req.
        described_value_domain (Union[Unset, str]):  Example: Value domain example.
        value_list (Union[Unset, list[str]]):  Example: ['Value example 1', 'Value example 2'].
        field_links (Union[Unset, SendigDatasetVariableLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    core: Union[Unset, str] = UNSET
    described_value_domain: Union[Unset, str] = UNSET
    value_list: Union[Unset, list[str]] = UNSET
    field_links: Union[Unset, "SendigDatasetVariableLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        role = self.role

        simple_datatype = self.simple_datatype

        core = self.core

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
        if role is not UNSET:
            field_dict["role"] = role
        if simple_datatype is not UNSET:
            field_dict["simpleDatatype"] = simple_datatype
        if core is not UNSET:
            field_dict["core"] = core
        if described_value_domain is not UNSET:
            field_dict["describedValueDomain"] = described_value_domain
        if value_list is not UNSET:
            field_dict["valueList"] = value_list
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sendig_dataset_variable_links import SendigDatasetVariableLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        role = d.pop("role", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        core = d.pop("core", UNSET)

        described_value_domain = d.pop("describedValueDomain", UNSET)

        value_list = cast(list[str], d.pop("valueList", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SendigDatasetVariableLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SendigDatasetVariableLinks.from_dict(_field_links)

        sendig_dataset_variable = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            role=role,
            simple_datatype=simple_datatype,
            core=core,
            described_value_domain=described_value_domain,
            value_list=value_list,
            field_links=field_links,
        )

        sendig_dataset_variable.additional_properties = d
        return sendig_dataset_variable

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
