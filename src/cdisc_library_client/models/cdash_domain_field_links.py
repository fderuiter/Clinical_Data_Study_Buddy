from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cdash_class_ref import CdashClassRef
    from ..models.cdash_domain_field_ref import CdashDomainFieldRef
    from ..models.cdash_domain_ref import CdashDomainRef
    from ..models.cdash_product_ref import CdashProductRef
    from ..models.root_cdash_domain_field_ref import RootCdashDomainFieldRef
    from ..models.root_ct_codelist_ref_element import RootCtCodelistRefElement
    from ..models.sdtm_dataset_variable_ref_target import SdtmDatasetVariableRefTarget
    from ..models.sdtmig_dataset_variable_ref_target import SdtmigDatasetVariableRefTarget


T = TypeVar("T", bound="CdashDomainFieldLinks")


@_attrs_define
class CdashDomainFieldLinks:
    """
    Attributes:
        self_ (Union[Unset, CdashDomainFieldRef]):
        codelist (Union[Unset, list['RootCtCodelistRefElement']]):
        parent_product (Union[Unset, CdashProductRef]):
        parent_class (Union[Unset, CdashClassRef]):
        parent_domain (Union[Unset, CdashDomainRef]):
        root_item (Union[Unset, RootCdashDomainFieldRef]):
        prior_version (Union[Unset, CdashDomainFieldRef]):
        sdtm_dataset_mapping_targets (Union[Unset, list['SdtmDatasetVariableRefTarget']]):
        sdtmig_dataset_mapping_targets (Union[Unset, list['SdtmigDatasetVariableRefTarget']]):
    """

    self_: Union[Unset, "CdashDomainFieldRef"] = UNSET
    codelist: Union[Unset, list["RootCtCodelistRefElement"]] = UNSET
    parent_product: Union[Unset, "CdashProductRef"] = UNSET
    parent_class: Union[Unset, "CdashClassRef"] = UNSET
    parent_domain: Union[Unset, "CdashDomainRef"] = UNSET
    root_item: Union[Unset, "RootCdashDomainFieldRef"] = UNSET
    prior_version: Union[Unset, "CdashDomainFieldRef"] = UNSET
    sdtm_dataset_mapping_targets: Union[Unset, list["SdtmDatasetVariableRefTarget"]] = UNSET
    sdtmig_dataset_mapping_targets: Union[Unset, list["SdtmigDatasetVariableRefTarget"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        codelist: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.codelist, Unset):
            codelist = []
            for codelist_item_data in self.codelist:
                codelist_item = codelist_item_data.to_dict()
                codelist.append(codelist_item)

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_class: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_class, Unset):
            parent_class = self.parent_class.to_dict()

        parent_domain: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_domain, Unset):
            parent_domain = self.parent_domain.to_dict()

        root_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.root_item, Unset):
            root_item = self.root_item.to_dict()

        prior_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prior_version, Unset):
            prior_version = self.prior_version.to_dict()

        sdtm_dataset_mapping_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sdtm_dataset_mapping_targets, Unset):
            sdtm_dataset_mapping_targets = []
            for sdtm_dataset_mapping_targets_item_data in self.sdtm_dataset_mapping_targets:
                sdtm_dataset_mapping_targets_item = sdtm_dataset_mapping_targets_item_data.to_dict()
                sdtm_dataset_mapping_targets.append(sdtm_dataset_mapping_targets_item)

        sdtmig_dataset_mapping_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sdtmig_dataset_mapping_targets, Unset):
            sdtmig_dataset_mapping_targets = []
            for sdtmig_dataset_mapping_targets_item_data in self.sdtmig_dataset_mapping_targets:
                sdtmig_dataset_mapping_targets_item = sdtmig_dataset_mapping_targets_item_data.to_dict()
                sdtmig_dataset_mapping_targets.append(sdtmig_dataset_mapping_targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if codelist is not UNSET:
            field_dict["codelist"] = codelist
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_class is not UNSET:
            field_dict["parentClass"] = parent_class
        if parent_domain is not UNSET:
            field_dict["parentDomain"] = parent_domain
        if root_item is not UNSET:
            field_dict["rootItem"] = root_item
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version
        if sdtm_dataset_mapping_targets is not UNSET:
            field_dict["sdtmDatasetMappingTargets"] = sdtm_dataset_mapping_targets
        if sdtmig_dataset_mapping_targets is not UNSET:
            field_dict["sdtmigDatasetMappingTargets"] = sdtmig_dataset_mapping_targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cdash_class_ref import CdashClassRef
        from ..models.cdash_domain_field_ref import CdashDomainFieldRef
        from ..models.cdash_domain_ref import CdashDomainRef
        from ..models.cdash_product_ref import CdashProductRef
        from ..models.root_cdash_domain_field_ref import RootCdashDomainFieldRef
        from ..models.root_ct_codelist_ref_element import RootCtCodelistRefElement
        from ..models.sdtm_dataset_variable_ref_target import SdtmDatasetVariableRefTarget
        from ..models.sdtmig_dataset_variable_ref_target import SdtmigDatasetVariableRefTarget

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, CdashDomainFieldRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = CdashDomainFieldRef.from_dict(_self_)

        codelist = []
        _codelist = d.pop("codelist", UNSET)
        for codelist_item_data in _codelist or []:
            codelist_item = RootCtCodelistRefElement.from_dict(codelist_item_data)

            codelist.append(codelist_item)

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, CdashProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = CdashProductRef.from_dict(_parent_product)

        _parent_class = d.pop("parentClass", UNSET)
        parent_class: Union[Unset, CdashClassRef]
        if isinstance(_parent_class, Unset):
            parent_class = UNSET
        else:
            parent_class = CdashClassRef.from_dict(_parent_class)

        _parent_domain = d.pop("parentDomain", UNSET)
        parent_domain: Union[Unset, CdashDomainRef]
        if isinstance(_parent_domain, Unset):
            parent_domain = UNSET
        else:
            parent_domain = CdashDomainRef.from_dict(_parent_domain)

        _root_item = d.pop("rootItem", UNSET)
        root_item: Union[Unset, RootCdashDomainFieldRef]
        if isinstance(_root_item, Unset):
            root_item = UNSET
        else:
            root_item = RootCdashDomainFieldRef.from_dict(_root_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, CdashDomainFieldRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = CdashDomainFieldRef.from_dict(_prior_version)

        sdtm_dataset_mapping_targets = []
        _sdtm_dataset_mapping_targets = d.pop("sdtmDatasetMappingTargets", UNSET)
        for sdtm_dataset_mapping_targets_item_data in _sdtm_dataset_mapping_targets or []:
            sdtm_dataset_mapping_targets_item = SdtmDatasetVariableRefTarget.from_dict(
                sdtm_dataset_mapping_targets_item_data
            )

            sdtm_dataset_mapping_targets.append(sdtm_dataset_mapping_targets_item)

        sdtmig_dataset_mapping_targets = []
        _sdtmig_dataset_mapping_targets = d.pop("sdtmigDatasetMappingTargets", UNSET)
        for sdtmig_dataset_mapping_targets_item_data in _sdtmig_dataset_mapping_targets or []:
            sdtmig_dataset_mapping_targets_item = SdtmigDatasetVariableRefTarget.from_dict(
                sdtmig_dataset_mapping_targets_item_data
            )

            sdtmig_dataset_mapping_targets.append(sdtmig_dataset_mapping_targets_item)

        cdash_domain_field_links = cls(
            self_=self_,
            codelist=codelist,
            parent_product=parent_product,
            parent_class=parent_class,
            parent_domain=parent_domain,
            root_item=root_item,
            prior_version=prior_version,
            sdtm_dataset_mapping_targets=sdtm_dataset_mapping_targets,
            sdtmig_dataset_mapping_targets=sdtmig_dataset_mapping_targets,
        )

        cdash_domain_field_links.additional_properties = d
        return cdash_domain_field_links

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
