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
    from ..models.sdtmig_classes_links import SdtmigClassesLinks


T = TypeVar("T", bound="SdtmigClasses")


@_attrs_define
class SdtmigClasses:
    """
    Attributes:
        name (Union[Unset, str]):  Example: SDTMIG v3.3.
        label (Union[Unset, str]):  Example: Study Data Tabulation Model Implementation Guide: Human Clinical Trials
            Version 3.3 (Final).
        description (Union[Unset, str]):  Example: CDISC Version 3.3 (v3.3) Study Data Tabulation Model Implementation
            Guide for Human Clinical Trials (SDTMIG) is intended to guide the organization, structure, and format of
            standard clinical trial tabulation datasets submitted to a regulatory authority..
        source (Union[Unset, str]):  Example: Prepared by the CDISC Submission Data Standards Team.
        effective_date (Union[Unset, str]):  Example: 2018-11-20.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: 3.3.
        field_links (Union[Unset, SdtmigClassesLinks]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SdtmigClassesLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        description = self.description

        source = self.source

        effective_date = self.effective_date

        registration_status = self.registration_status

        version = self.version

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if registration_status is not UNSET:
            field_dict["registrationStatus"] = registration_status
        if version is not UNSET:
            field_dict["version"] = version
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sdtmig_classes_links import SdtmigClassesLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SdtmigClassesLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SdtmigClassesLinks.from_dict(_field_links)

        sdtmig_classes = cls(
            name=name,
            label=label,
            description=description,
            source=source,
            effective_date=effective_date,
            registration_status=registration_status,
            version=version,
            field_links=field_links,
        )

        sdtmig_classes.additional_properties = d
        return sdtmig_classes

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
