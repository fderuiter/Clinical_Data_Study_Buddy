from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sdtm_dataset_variable_links import SdtmDatasetVariableLinks


T = TypeVar("T", bound="SdtmDatasetVariable")


@_attrs_define
class SdtmDatasetVariable:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 4.
        name (Union[Unset, str]):  Example: SUBJID.
        label (Union[Unset, str]):  Example: Subject Identifier for the Study.
        description (Union[Unset, str]):  Example: Subject identifier, which must be unique within the study. Often the
            ID of the subject as recorded on a CRF..
        role (Union[Unset, str]):  Example: Topic.
        role_description (Union[Unset, str]):  Example: Topic.
        simple_datatype (Union[Unset, str]):  Example: Char.
        described_value_domain (Union[Unset, str]):  Example: Sponsor-Defined.
        field_links (Union[Unset, SdtmDatasetVariableLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    role_description: Union[Unset, str] = UNSET
    simple_datatype: Union[Unset, str] = UNSET
    described_value_domain: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SdtmDatasetVariableLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        role = self.role

        role_description = self.role_description

        simple_datatype = self.simple_datatype

        described_value_domain = self.described_value_domain

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
        if role_description is not UNSET:
            field_dict["roleDescription"] = role_description
        if simple_datatype is not UNSET:
            field_dict["simpleDatatype"] = simple_datatype
        if described_value_domain is not UNSET:
            field_dict["describedValueDomain"] = described_value_domain
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtm_dataset_variable_links import SdtmDatasetVariableLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        role = d.pop("role", UNSET)

        role_description = d.pop("roleDescription", UNSET)

        simple_datatype = d.pop("simpleDatatype", UNSET)

        described_value_domain = d.pop("describedValueDomain", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SdtmDatasetVariableLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SdtmDatasetVariableLinks.from_dict(_field_links)

        sdtm_dataset_variable = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            role=role,
            role_description=role_description,
            simple_datatype=simple_datatype,
            described_value_domain=described_value_domain,
            field_links=field_links,
        )

        sdtm_dataset_variable.additional_properties = d
        return sdtm_dataset_variable

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
