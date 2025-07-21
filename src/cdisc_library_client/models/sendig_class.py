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
    from ..models.sendig_class_links import SendigClassLinks
    from ..models.sendig_dataset import SendigDataset


T = TypeVar("T", bound="SendigClass")


@_attrs_define
class SendigClass:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 5.
        name (Union[Unset, str]):  Example: Findings.
        label (Union[Unset, str]):  Example: Findings Observation Class.
        description (Union[Unset, str]):  Example: This SDTM class captures the observations resulting from planned
            evaluations to address specific tests or questions such as laboratory tests, ECG testing, and questions listed
            on questionnaires. (Source: CDISC Controlled Terminology, GNRLOBSC, C103373, 2018-06-29).
        field_links (Union[Unset, SendigClassLinks]):
        datasets (Union[Unset, list['SendigDataset']]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "SendigClassLinks"] = UNSET
    datasets: Union[Unset, list["SendigDataset"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        datasets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.datasets, Unset):
            datasets = []
            for datasets_item_data in self.datasets:
                datasets_item = datasets_item_data.to_dict()
                datasets.append(datasets_item)

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
        if datasets is not UNSET:
            field_dict["datasets"] = datasets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sendig_class_links import SendigClassLinks
        from ..models.sendig_dataset import SendigDataset

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, SendigClassLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = SendigClassLinks.from_dict(_field_links)

        datasets = []
        _datasets = d.pop("datasets", UNSET)
        for datasets_item_data in _datasets or []:
            datasets_item = SendigDataset.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        sendig_class = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
            datasets=datasets,
        )

        sendig_class.additional_properties = d
        return sendig_class

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
