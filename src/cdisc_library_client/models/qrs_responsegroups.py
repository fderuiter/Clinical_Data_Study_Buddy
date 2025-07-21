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
    from ..models.qrs_responsegroups_links import QrsResponsegroupsLinks


T = TypeVar("T", bound="QrsResponsegroups")


@_attrs_define
class QrsResponsegroups:
    """
    Attributes:
        name (Union[Unset, str]):  Example: AIMS v1.0.
        label (Union[Unset, str]):  Example: Abnormal Involuntary Movement Scale Version 1.0.
        description (Union[Unset, str]):  Example: Abnormal Involuntary Movement Scale (AIMS) (Guy W. Ed. ECDEU
            Assessment Manual for Psychopharmacology. Rockville MD: US Dept of Health, Education and Welfare. 1976,
            Publication No. (ADM) 76-338)..
        effective_date (Union[Unset, str]):  Example: 2013-05-22.
        until_date (Union[Unset, str]):  Example: 2030-12-31.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: 1.0.
        qrs_type (Union[Unset, str]):  Example: Questionnaire.
        field_links (Union[Unset, QrsResponsegroupsLinks]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    until_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    qrs_type: Union[Unset, str] = UNSET
    field_links: Union[Unset, "QrsResponsegroupsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label = self.label

        description = self.description

        effective_date = self.effective_date

        until_date = self.until_date

        registration_status = self.registration_status

        version = self.version

        qrs_type = self.qrs_type

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
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if until_date is not UNSET:
            field_dict["untilDate"] = until_date
        if registration_status is not UNSET:
            field_dict["registrationStatus"] = registration_status
        if version is not UNSET:
            field_dict["version"] = version
        if qrs_type is not UNSET:
            field_dict["qrsType"] = qrs_type
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_responsegroups_links import QrsResponsegroupsLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        until_date = d.pop("untilDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        qrs_type = d.pop("qrsType", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, QrsResponsegroupsLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = QrsResponsegroupsLinks.from_dict(_field_links)

        qrs_responsegroups = cls(
            name=name,
            label=label,
            description=description,
            effective_date=effective_date,
            until_date=until_date,
            registration_status=registration_status,
            version=version,
            qrs_type=qrs_type,
            field_links=field_links,
        )

        qrs_responsegroups.additional_properties = d
        return qrs_responsegroups

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
