from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdashig_class import CdashigClass
    from ..models.cdashig_product_links import CdashigProductLinks


T = TypeVar("T", bound="CdashigProduct")


@_attrs_define
class CdashigProduct:
    """
    Attributes:
        name (Union[Unset, str]):  Example: CDASHIG v2.1.
        label (Union[Unset, str]):  Example: Clinical Data Acquisition Standards Harmonization Implementation Guide for
            Human Clinical Trials Version 2.1.
        description (Union[Unset, str]):  Example: The Clinical Data Acquisition Standards Harmonization (CDASH) Model,
            the CDASH Implementation Guide (CDASHIG), and the CDASHIG Metadata Table define basic standards for the
            collection of clinical trial data and how to implement the standard for specific case report forms (CRFs)..
        source (Union[Unset, str]):  Example: Prepared by the CDISC CDASH Team.
        effective_date (Union[Unset, str]):  Example: 2019-11-01.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: 2.1.
        field_links (Union[Unset, CdashigProductLinks]):
        classes (Union[Unset, list['CdashigClass']]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashigProductLinks"] = UNSET
    classes: Union[Unset, list["CdashigClass"]] = UNSET
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

        classes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = []
            for classes_item_data in self.classes:
                classes_item = classes_item_data.to_dict()
                classes.append(classes_item)

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
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdashig_class import CdashigClass
        from ..models.cdashig_product_links import CdashigProductLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashigProductLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashigProductLinks.from_dict(_field_links)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = CdashigClass.from_dict(classes_item_data)

            classes.append(classes_item)

        cdashig_product = cls(
            name=name,
            label=label,
            description=description,
            source=source,
            effective_date=effective_date,
            registration_status=registration_status,
            version=version,
            field_links=field_links,
            classes=classes,
        )

        cdashig_product.additional_properties = d
        return cdashig_product

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
