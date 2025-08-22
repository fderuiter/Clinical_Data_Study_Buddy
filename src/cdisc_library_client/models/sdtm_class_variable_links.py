from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_sdtm_class_variable_ref import RootSdtmClassVariableRef
    from ..models.sdtm_class_ref import SdtmClassRef
    from ..models.sdtm_class_variable_ref import SdtmClassVariableRef
    from ..models.sdtm_class_variable_ref_qualifies import SdtmClassVariableRefQualifies
    from ..models.sdtm_product_ref import SdtmProductRef


T = TypeVar("T", bound="SdtmClassVariableLinks")


@_attrs_define
class SdtmClassVariableLinks:
    """
    Attributes:
        self_ (Union[Unset, SdtmClassVariableRef]):
        parent_product (Union[Unset, SdtmProductRef]):
        parent_class (Union[Unset, SdtmClassRef]):
        qualifies_variables (Union[Unset, list['SdtmClassVariableRefQualifies']]):
        root_item (Union[Unset, RootSdtmClassVariableRef]):
        prior_version (Union[Unset, SdtmClassVariableRef]):
    """

    self_: Union[Unset, "SdtmClassVariableRef"] = UNSET
    parent_product: Union[Unset, "SdtmProductRef"] = UNSET
    parent_class: Union[Unset, "SdtmClassRef"] = UNSET
    qualifies_variables: Union[Unset, list["SdtmClassVariableRefQualifies"]] = UNSET
    root_item: Union[Unset, "RootSdtmClassVariableRef"] = UNSET
    prior_version: Union[Unset, "SdtmClassVariableRef"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        qualifies_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.qualifies_variables, Unset):
            qualifies_variables = []
            for qualifies_variables_item_data in self.qualifies_variables:
                qualifies_variables_item = qualifies_variables_item_data.to_dict()
                qualifies_variables.append(qualifies_variables_item)

        root_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.root_item, Unset):
            root_item = self.root_item.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if qualifies_variables is not UNSET:
            field_dict["qualifiesVariables"] = qualifies_variables
        if root_item is not UNSET:
            field_dict["rootItem"] = root_item
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_sdtm_class_variable_ref import RootSdtmClassVariableRef
        from ..models.sdtm_class_ref import SdtmClassRef
        from ..models.sdtm_class_variable_ref import SdtmClassVariableRef
        from ..models.sdtm_class_variable_ref_qualifies import SdtmClassVariableRefQualifies
        from ..models.sdtm_product_ref import SdtmProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SdtmClassVariableRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SdtmClassVariableRef.from_dict(_self_)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SdtmProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SdtmProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, SdtmClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = SdtmClassRef.from_dict(_parent_class)

        qualifies_variables = []
        _qualifies_variables = d.pop("qualifiesVariables", UNSET)
        for qualifies_variables_item_data in _qualifies_variables or []:
            qualifies_variables_item = SdtmClassVariableRefQualifies.from_dict(qualifies_variables_item_data)

            qualifies_variables.append(qualifies_variables_item)

        _root_item = d.pop("rootItem", UNSET)
        root_item: Union[Unset, RootSdtmClassVariableRef]
        if isinstance(_root_item, Unset):
            root_item = UNSET
        else:
            root_item = RootSdtmClassVariableRef.from_dict(_root_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SdtmClassVariableRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SdtmClassVariableRef.from_dict(_prior_version)

        sdtm_class_variable_links = cls(
            self_=self_,
            parent_product=parent_product,
            parent_class=parent_class,
            qualifies_variables=qualifies_variables,
            root_item=root_item,
            prior_version=prior_version,
        )

        sdtm_class_variable_links.additional_properties = d
        return sdtm_class_variable_links

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
