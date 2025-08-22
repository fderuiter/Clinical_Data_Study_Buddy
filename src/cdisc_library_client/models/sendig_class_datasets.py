from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sendig_class_datasets_links import SendigClassDatasetsLinks


T = TypeVar("T", bound="SendigClassDatasets")


@_attrs_define
class SendigClassDatasets:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 5.
        name (Union[Unset, str]):  Example: Findings.
        label (Union[Unset, str]):  Example: Findings Observation Class.
        description (Union[Unset, str]):  Example: This SDTM class captures the observations resulting from planned
            evaluations to address specific tests or questions such as laboratory tests, ECG testing, and questions listed
            on questionnaires. (Source: CDISC Controlled Terminology, GNRLOBSC, C103373, 2018-06-29).
        field_links (Union[Unset, SendigClassDatasetsLinks]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SendigClassDatasetsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sendig_class_datasets_links import SendigClassDatasetsLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SendigClassDatasetsLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SendigClassDatasetsLinks.from_dict(_field_links)

        sendig_class_datasets = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
        )

        sendig_class_datasets.additional_properties = d
        return sendig_class_datasets

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
