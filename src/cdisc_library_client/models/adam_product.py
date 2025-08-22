from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adam_datastructure import AdamDatastructure
    from ..models.adam_product_links import AdamProductLinks


T = TypeVar("T", bound="AdamProduct")


@_attrs_define
class AdamProduct:
    """
    Attributes:
        name (Union[Unset, str]):  Example: ADaMIG v1.1.
        label (Union[Unset, str]):  Example: Analysis Data Model Implementation Guide Version 1.1.
        description (Union[Unset, str]):  Example: This document comprises the Clinical Data Interchange Standards
            Consortium (CDISC) Version 1.1 of the Analysis Data Model Implementation Guide (ADaMIG), which has been prepared
            by the Analysis Data Model (ADaM) Team of CDISC. The ADaMIG specifies ADaM standard dataset structures and
            variables, including naming conventions. It also specifies standard solutions to implementation issues.

            The ADaMIG must be used in close concert with the current version of the document titled "Analysis Data Model
            (ADaM)" which is available for download at http://www.cdisc.org/adam. That document explains the purpose of the
            Analysis Data Model. It describes fundamental principles that apply to all analysis datasets, with the driving
            principle being that the design of ADaM datasets and associated metadata facilitate explicit communication of
            the content of, input to, and purpose of submitted ADaM datasets. The Analysis Data Model supports efficient
            generation, replication, and review of analysis results..
        source (Union[Unset, str]):  Example: Prepared by the CDISC Analysis Data Model Team.
        effective_date (Union[Unset, str]):  Example: 2016-02-12.
        registration_status (Union[Unset, str]):  Example: Final.
        version (Union[Unset, str]):  Example: 1.1.
        field_links (Union[Unset, AdamProductLinks]):
        data_structures (Union[Unset, list['AdamDatastructure']]):
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    effective_date: Union[Unset, str] = UNSET
    registration_status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    field_links: Union[Unset, "AdamProductLinks"] = UNSET
    data_structures: Union[Unset, list["AdamDatastructure"]] = UNSET
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

        data_structures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_structures, Unset):
            data_structures = []
            for data_structures_item_data in self.data_structures:
                data_structures_item = data_structures_item_data.to_dict()
                data_structures.append(data_structures_item)

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
        if data_structures is not UNSET:
            field_dict["dataStructures"] = data_structures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adam_datastructure import AdamDatastructure
        from ..models.adam_product_links import AdamProductLinks

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        source = d.pop("source", UNSET)

        effective_date = d.pop("effectiveDate", UNSET)

        registration_status = d.pop("registrationStatus", UNSET)

        version = d.pop("version", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, AdamProductLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AdamProductLinks.from_dict(_field_links)

        data_structures = []
        _data_structures = d.pop("dataStructures", UNSET)
        for data_structures_item_data in _data_structures or []:
            data_structures_item = AdamDatastructure.from_dict(data_structures_item_data)

            data_structures.append(data_structures_item)

        adam_product = cls(
            name=name,
            label=label,
            description=description,
            source=source,
            effective_date=effective_date,
            registration_status=registration_status,
            version=version,
            field_links=field_links,
            data_structures=data_structures,
        )

        adam_product.additional_properties = d
        return adam_product

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
