from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.about_links import AboutLinks


T = TypeVar("T", bound="About")


@_attrs_define
class About:
    """
    Attributes:
        field_links (Union[Unset, AboutLinks]):
        release_notes (Union[Unset, str]):  Example: https://wiki.cdisc.org/display/LIBSUPRT/Release+Notes.
        api_documentation (Union[Unset, str]):  Example: https://www.cdisc.org/cdisc-library/api-documentation.
    """

    field_links: Union[Unset, "AboutLinks"] = UNSET
    release_notes: Union[Unset, str] = UNSET
    api_documentation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        release_notes = self.release_notes

        api_documentation = self.api_documentation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if release_notes is not UNSET:
            field_dict["release-notes"] = release_notes
        if api_documentation is not UNSET:
            field_dict["api-documentation"] = api_documentation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.about_links import AboutLinks

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, AboutLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AboutLinks.from_dict(_field_links)

        release_notes = d.pop("release-notes", UNSET)

        api_documentation = d.pop("api-documentation", UNSET)

        about = cls(
            field_links=field_links,
            release_notes=release_notes,
            api_documentation=api_documentation,
        )

        about.additional_properties = d
        return about

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
