from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lastupdated_links import LastupdatedLinks


T = TypeVar("T", bound="Lastupdated")


@_attrs_define
class Lastupdated:
    """
    Attributes:
        field_links (Union[Unset, LastupdatedLinks]):
        overall (Union[Unset, str]):  Example: 2020-02-14.
        data_analysis (Union[Unset, str]):  Example: 2020-02-14.
        data_collection (Union[Unset, str]):  Example: 2020-02-14.
        data_tabulation (Union[Unset, str]):  Example: 2020-02-14.
        measure (Union[Unset, str]):  Example: 2020-02-14.
        terminology (Union[Unset, str]):  Example: 2020-02-14.
    """

    field_links: Union[Unset, "LastupdatedLinks"] = UNSET
    overall: Union[Unset, str] = UNSET
    data_analysis: Union[Unset, str] = UNSET
    data_collection: Union[Unset, str] = UNSET
    data_tabulation: Union[Unset, str] = UNSET
    measure: Union[Unset, str] = UNSET
    terminology: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        overall = self.overall

        data_analysis = self.data_analysis

        data_collection = self.data_collection

        data_tabulation = self.data_tabulation

        measure = self.measure

        terminology = self.terminology

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if overall is not UNSET:
            field_dict["overall"] = overall
        if data_analysis is not UNSET:
            field_dict["data-analysis"] = data_analysis
        if data_collection is not UNSET:
            field_dict["data-collection"] = data_collection
        if data_tabulation is not UNSET:
            field_dict["data-tabulation"] = data_tabulation
        if measure is not UNSET:
            field_dict["measure"] = measure
        if terminology is not UNSET:
            field_dict["terminology"] = terminology

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lastupdated_links import LastupdatedLinks

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, LastupdatedLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = LastupdatedLinks.from_dict(_field_links)

        overall = d.pop("overall", UNSET)

        data_analysis = d.pop("data-analysis", UNSET)

        data_collection = d.pop("data-collection", UNSET)

        data_tabulation = d.pop("data-tabulation", UNSET)

        measure = d.pop("measure", UNSET)

        terminology = d.pop("terminology", UNSET)

        lastupdated = cls(
            field_links=field_links,
            overall=overall,
            data_analysis=data_analysis,
            data_collection=data_collection,
            data_tabulation=data_tabulation,
            measure=measure,
            terminology=terminology,
        )

        lastupdated.additional_properties = d
        return lastupdated

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
