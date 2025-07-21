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
    from ..models.sendig_class import SendigClass
    from ..models.sendig_product_links import SendigProductLinks


T = TypeVar("T", bound="SendigProduct")


@_attrs_define
class SendigProduct:
    """
    Attributes:
        name (Union[Unset, str]):  Example: SENDIG v3.1.
        label (Union[Unset, str]):  Example: Standard for Exchange ofâ€¦ies Version 3.1 (Final).
        description (Union[Unset, str]):  Example: The SENDIG is intended to guide the organization, structure, and
            format of standard nonclinical tabulation datasets for interchange between organizations such as sponsors and
            CROs, and for submission to regulatory authorities such as the U.S. Food and Drug Administration (FDA)..
        source (Union[Unset, str]):  Example: Prepared by the CDISC Stâ€¦f Nonclinical Data Team.
        effective_date (Union[Unset, str]):  Example: 2016-06-27.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: 3.1.
        field_links (Union[Unset, SendigProductLinks]):
        classes (Union[Unset, list['SendigClass']]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SendigProductLinks"] = UNSET
    classes: Union[Unset, list["SendigClass"]] = UNSET
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
        from ..models.sendig_class import SendigClass
        from ..models.sendig_product_links import SendigProductLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SendigProductLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SendigProductLinks.from_dict(_field_links)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = SendigClass.from_dict(classes_item_data)

            classes.append(classes_item)

        sendig_product = cls(
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

        sendig_product.additional_properties = d
        return sendig_product

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
