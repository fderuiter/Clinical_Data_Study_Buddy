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
    from ..models.ct_codelist_terms_ref import CtCodelistTermsRef
    from ..models.ct_package_ref import CtPackageRef
    from ..models.ct_term_ref_element import CtTermRefElement
    from ..models.root_ct_codelist_ref import RootCtCodelistRef


T = TypeVar("T", bound="CtCodelistTermsLinks")


@_attrs_define
class CtCodelistTermsLinks:
    """
    Attributes:
        self_ (Union[Unset, CtCodelistTermsRef]):
        parent_package (Union[Unset, CtPackageRef]):
        root_item (Union[Unset, RootCtCodelistRef]):
        prior_version (Union[Unset, CtCodelistTermsRef]):
        terms (Union[Unset, list['CtTermRefElement']]):
    """

    self_: Union[Unset, "CtCodelistTermsRef"] = UNSET
    parent_package: Union[Unset, "CtPackageRef"] = UNSET
    root_item: Union[Unset, "RootCtCodelistRef"] = UNSET
    prior_version: Union[Unset, "CtCodelistTermsRef"] = UNSET
    terms: Union[Unset, list["CtTermRefElement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_package: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_package, Unset):
            parent_package = self.parent_package.to_dict()

        root_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.root_item, Unset):
            root_item = self.root_item.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        terms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_package is not UNSET:
            field_dict["parentPackage"] = parent_package
        if root_item is not UNSET:
            field_dict["rootItem"] = root_item
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct_codelist_terms_ref import CtCodelistTermsRef
        from ..models.ct_package_ref import CtPackageRef
        from ..models.ct_term_ref_element import CtTermRefElement
        from ..models.root_ct_codelist_ref import RootCtCodelistRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CtCodelistTermsRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CtCodelistTermsRef.from_dict(_self_)

        _parent_package = d.pop("parentPackage", UNSET)
        parent_package: Union[Unset, CtPackageRef]
        if isinstance(_parent_package, Unset):
            parent_package = UNSET
        else:
            parent_package = CtPackageRef.from_dict(_parent_package)

        _root_item = d.pop("rootItem", UNSET)
        root_item: Union[Unset, RootCtCodelistRef]
        if isinstance(_root_item, Unset):
            root_item = UNSET
        else:
            root_item = RootCtCodelistRef.from_dict(_root_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CtCodelistTermsRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CtCodelistTermsRef.from_dict(_prior_version)

        terms = []
        _terms = d.pop("terms", UNSET)
        for terms_item_data in _terms or []:
            terms_item = CtTermRefElement.from_dict(terms_item_data)

            terms.append(terms_item)

        ct_codelist_terms_links = cls(
            self_=self_,
            parent_package=parent_package,
            root_item=root_item,
            prior_version=prior_version,
            terms=terms,
        )

        ct_codelist_terms_links.additional_properties = d
        return ct_codelist_terms_links

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
