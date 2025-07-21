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
    from ..models.cdashig_domain_field import CdashigDomainField
    from ..models.cdashig_domain_links import CdashigDomainLinks


T = TypeVar("T", bound="CdashigDomain")


@_attrs_define
class CdashigDomain:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 31.
        name (Union[Unset, str]):  Example: VS.
        label (Union[Unset, str]):  Example: Vital Signs.
        field_links (Union[Unset, CdashigDomainLinks]):
        fields (Union[Unset, list['CdashigDomainField']]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashigDomainLinks"] = UNSET
    fields: Union[Unset, list["CdashigDomainField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

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
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_domain_field import CdashigDomainField
        from ..models.cdashig_domain_links import CdashigDomainLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashigDomainLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashigDomainLinks.from_dict(_field_links)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CdashigDomainField.from_dict(fields_item_data)

            fields.append(fields_item)

        cdashig_domain = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            field_links=field_links,
            fields=fields,
        )

        cdashig_domain.additional_properties = d
        return cdashig_domain

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
