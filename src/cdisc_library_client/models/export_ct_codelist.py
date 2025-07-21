from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_ct_term import ExportCtTerm


T = TypeVar("T", bound="ExportCtCodelist")


@_attrs_define
class ExportCtCodelist:
    """
    Attributes:
        code (Union[Unset, str]):
        codelist_code (Union[Unset, str]):
        codelist_extensible_yes_no (Union[Unset, str]):
        codelist_name (Union[Unset, str]):
        cdisc_submission_value (Union[Unset, str]):
        cdisc_synonyms (Union[Unset, list[str]]):
        cdisc_definition (Union[Unset, str]):
        nci_preferred_term (Union[Unset, str]):
        standard_and_date (Union[Unset, str]):
        field_ (Union[Unset, list['ExportCtTerm']]):
    """

    code: Union[Unset, str] = UNSET
    codelist_code: Union[Unset, str] = UNSET
    codelist_extensible_yes_no: Union[Unset, str] = UNSET
    codelist_name: Union[Unset, str] = UNSET
    cdisc_submission_value: Union[Unset, str] = UNSET
    cdisc_synonyms: Union[Unset, list[str]] = UNSET
    cdisc_definition: Union[Unset, str] = UNSET
    nci_preferred_term: Union[Unset, str] = UNSET
    standard_and_date: Union[Unset, str] = UNSET
    field_: Union[Unset, list["ExportCtTerm"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        codelist_code = self.codelist_code

        codelist_extensible_yes_no = self.codelist_extensible_yes_no

        codelist_name = self.codelist_name

        cdisc_submission_value = self.cdisc_submission_value

        cdisc_synonyms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cdisc_synonyms, Unset):
            cdisc_synonyms = self.cdisc_synonyms

        cdisc_definition = self.cdisc_definition

        nci_preferred_term = self.nci_preferred_term

        standard_and_date = self.standard_and_date

        field_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.field_, Unset):
            field_ = []
            for field_item_data in self.field_:
                field_item = field_item_data.to_dict()
                field_.append(field_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if codelist_code is not UNSET:
            field_dict["Codelist Code"] = codelist_code
        if codelist_extensible_yes_no is not UNSET:
            field_dict["Codelist Extensible (Yes/No)"] = codelist_extensible_yes_no
        if codelist_name is not UNSET:
            field_dict["Codelist Name"] = codelist_name
        if cdisc_submission_value is not UNSET:
            field_dict["CDISC Submission Value"] = cdisc_submission_value
        if cdisc_synonyms is not UNSET:
            field_dict["CDISC Synonym(s)"] = cdisc_synonyms
        if cdisc_definition is not UNSET:
            field_dict["CDISC Definition"] = cdisc_definition
        if nci_preferred_term is not UNSET:
            field_dict["NCI Preferred Term"] = nci_preferred_term
        if standard_and_date is not UNSET:
            field_dict["Standard and Date"] = standard_and_date
        if field_ is not UNSET:
            field_dict[""] = field_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_ct_term import ExportCtTerm

        d = dict(src_dict)
        code = d.pop("Code", UNSET)

        codelist_code = d.pop("Codelist Code", UNSET)

        codelist_extensible_yes_no = d.pop("Codelist Extensible (Yes/No)", UNSET)

        codelist_name = d.pop("Codelist Name", UNSET)

        cdisc_submission_value = d.pop("CDISC Submission Value", UNSET)

        cdisc_synonyms = cast(list[str], d.pop("CDISC Synonym(s)", UNSET))

        cdisc_definition = d.pop("CDISC Definition", UNSET)

        nci_preferred_term = d.pop("NCI Preferred Term", UNSET)

        standard_and_date = d.pop("Standard and Date", UNSET)

        field_ = []
        _field_ = d.pop("", UNSET)
        for field_item_data in _field_ or []:
            field_item = ExportCtTerm.from_dict(field_item_data)

            field_.append(field_item)

        export_ct_codelist = cls(
            code=code,
            codelist_code=codelist_code,
            codelist_extensible_yes_no=codelist_extensible_yes_no,
            codelist_name=codelist_name,
            cdisc_submission_value=cdisc_submission_value,
            cdisc_synonyms=cdisc_synonyms,
            cdisc_definition=cdisc_definition,
            nci_preferred_term=nci_preferred_term,
            standard_and_date=standard_and_date,
            field_=field_,
        )

        export_ct_codelist.additional_properties = d
        return export_ct_codelist

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
