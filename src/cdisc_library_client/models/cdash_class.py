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
    from ..models.cdash_class_field import CdashClassField
    from ..models.cdash_class_links import CdashClassLinks


T = TypeVar("T", bound="CdashClass")


@_attrs_define
class CdashClass:
    """
    Attributes:
        ordinal (Union[Unset, str]):  Example: 5.
        name (Union[Unset, str]):  Example: Timing.
        label (Union[Unset, str]):  Example: Timing Class.
        description (Union[Unset, str]):  Example: Timing class variables.
        field_links (Union[Unset, CdashClassLinks]):
        cdash_model_fields (Union[Unset, list['CdashClassField']]):
    """

    ordinal: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CdashClassLinks"] = UNSET
    cdash_model_fields: Union[Unset, list["CdashClassField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordinal = self.ordinal

        name = self.name

        label = self.label

        description = self.description

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        cdash_model_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cdash_model_fields, Unset):
            cdash_model_fields = []
            for cdash_model_fields_item_data in self.cdash_model_fields:
                cdash_model_fields_item = cdash_model_fields_item_data.to_dict()
                cdash_model_fields.append(cdash_model_fields_item)

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
        if cdash_model_fields is not UNSET:
            field_dict["cdashModelFields"] = cdash_model_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_field import CdashClassField
        from ..models.cdash_class_links import CdashClassLinks

        d = dict(src_dict)
        ordinal = d.pop("ordinal", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CdashClassLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CdashClassLinks.from_dict(_field_links)

        cdash_model_fields = []
        _cdash_model_fields = d.pop("cdashModelFields", UNSET)
        for cdash_model_fields_item_data in _cdash_model_fields or []:
            cdash_model_fields_item = CdashClassField.from_dict(
                cdash_model_fields_item_data
            )

            cdash_model_fields.append(cdash_model_fields_item)

        cdash_class = cls(
            ordinal=ordinal,
            name=name,
            label=label,
            description=description,
            field_links=field_links,
            cdash_model_fields=cdash_model_fields,
        )

        cdash_class.additional_properties = d
        return cdash_class

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
