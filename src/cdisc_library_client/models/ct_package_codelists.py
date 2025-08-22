from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct_package_codelists_links import CtPackageCodelistsLinks


T = TypeVar("T", bound="CtPackageCodelists")


@_attrs_define
class CtPackageCodelists:
    """
    Attributes:
        name (Union[Unset, str]):  Example: SDTM CT 2019-12-20.
        label (Union[Unset, str]):  Example: SDTM Controlled Terminology Package 40 Effective 2019-12-20.
        description (Union[Unset, str]):  Example: CDISC Controlled Terminology for SDTM is the set of CDISC-developed
            or CDISC-adopted standard expressions (values) used with data items within CDISC-defined SDTM datasets..
        source (Union[Unset, str]):  Example: SDTM Controlled Terminology developed by the CDISC Terminology Team in
            collaboration with the National Cancer Institute's Enterprise Vocabulary Services (EVS).
        effective_date (Union[Unset, str]):  Example: 2019-12-20.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: TODO.
        field_links (Union[Unset, CtPackageCodelistsLinks]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CtPackageCodelistsLinks"] = UNSET
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
        from ..models.ct_package_codelists_links import CtPackageCodelistsLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CtPackageCodelistsLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CtPackageCodelistsLinks.from_dict(_field_links)

        ct_package_codelists = cls(
            name=name,
            label=label,
            description=description,
            source=source,
            effective_date=effective_date,
            registration_status=registration_status,
            version=version,
            field_links=field_links,
        )

        ct_package_codelists.additional_properties = d
        return ct_package_codelists

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
