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
    from ..models.root_ct_codelist_ref_element import RootCtCodelistRefElement
    from ..models.root_sendig_dataset_variable_ref import RootSendigDatasetVariableRef
    from ..models.sdtm_class_variable_ref import SdtmClassVariableRef
    from ..models.sdtm_dataset_variable_ref import SdtmDatasetVariableRef
    from ..models.sendig_dataset_ref import SendigDatasetRef
    from ..models.sendig_dataset_variable_ref import SendigDatasetVariableRef
    from ..models.sendig_product_ref import SendigProductRef


T = TypeVar("T", bound="SendigDatasetVariableLinks")


@_attrs_define
class SendigDatasetVariableLinks:
    """
    Attributes:
        self_ (Union[Unset, SendigDatasetVariableRef]):
        codelist (Union[Unset, list['RootCtCodelistRefElement']]):
        model_class_variable (Union[Unset, SdtmClassVariableRef]):
        model_dataset_variable (Union[Unset, SdtmDatasetVariableRef]):
        parent_product (Union[Unset, SendigProductRef]):
        parent_dataset (Union[Unset, SendigDatasetRef]):
        root_item (Union[Unset, RootSendigDatasetVariableRef]):
        prior_version (Union[Unset, SendigDatasetVariableRef]):
    """

    self_: Union[Unset, "SendigDatasetVariableRef"] = UNSET
    codelist: Union[Unset, list["RootCtCodelistRefElement"]] = UNSET
    model_class_variable: Union[Unset, "SdtmClassVariableRef"] = UNSET
    model_dataset_variable: Union[Unset, "SdtmDatasetVariableRef"] = UNSET
    parent_product: Union[Unset, "SendigProductRef"] = UNSET
    parent_dataset: Union[Unset, "SendigDatasetRef"] = UNSET
    root_item: Union[Unset, "RootSendigDatasetVariableRef"] = UNSET
    prior_version: Union[Unset, "SendigDatasetVariableRef"] = UNSET
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

        model_class_variable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_class_variable, Unset):
            model_class_variable = self.model_class_variable.to_dict()

        model_dataset_variable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model_dataset_variable, Unset):
            model_dataset_variable = self.model_dataset_variable.to_dict()

        parent_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_product, Unset):
            parent_product = self.parent_product.to_dict()

        parent_dataset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_dataset, Unset):
            parent_dataset = self.parent_dataset.to_dict()

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
        if codelist is not UNSET:
            field_dict["codelist"] = codelist
        if model_class_variable is not UNSET:
            field_dict["modelClassVariable"] = model_class_variable
        if model_dataset_variable is not UNSET:
            field_dict["modelDatasetVariable"] = model_dataset_variable
        if parent_product is not UNSET:
            field_dict["parentProduct"] = parent_product
        if parent_dataset is not UNSET:
            field_dict["parentDataset"] = parent_dataset
        if root_item is not UNSET:
            field_dict["rootItem"] = root_item
        if prior_version is not UNSET:
            field_dict["priorVersion"] = prior_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_ct_codelist_ref_element import RootCtCodelistRefElement
        from ..models.root_sendig_dataset_variable_ref import (
            RootSendigDatasetVariableRef,
        )
        from ..models.sdtm_class_variable_ref import SdtmClassVariableRef
        from ..models.sdtm_dataset_variable_ref import SdtmDatasetVariableRef
        from ..models.sendig_dataset_ref import SendigDatasetRef
        from ..models.sendig_dataset_variable_ref import SendigDatasetVariableRef
        from ..models.sendig_product_ref import SendigProductRef

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, SendigDatasetVariableRef]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SendigDatasetVariableRef.from_dict(_self_)

        codelist = []
        _codelist = d.pop("codelist", UNSET)
        for codelist_item_data in _codelist or []:
            codelist_item = RootCtCodelistRefElement.from_dict(codelist_item_data)

            codelist.append(codelist_item)

        _model_class_variable = d.pop("modelClassVariable", UNSET)
        model_class_variable: Union[Unset, SdtmClassVariableRef]
        if isinstance(_model_class_variable, Unset):
            model_class_variable = UNSET
        else:
            model_class_variable = SdtmClassVariableRef.from_dict(_model_class_variable)

        _model_dataset_variable = d.pop("modelDatasetVariable", UNSET)
        model_dataset_variable: Union[Unset, SdtmDatasetVariableRef]
        if isinstance(_model_dataset_variable, Unset):
            model_dataset_variable = UNSET
        else:
            model_dataset_variable = SdtmDatasetVariableRef.from_dict(
                _model_dataset_variable
            )

        _parent_product = d.pop("parentProduct", UNSET)
        parent_product: Union[Unset, SendigProductRef]
        if isinstance(_parent_product, Unset):
            parent_product = UNSET
        else:
            parent_product = SendigProductRef.from_dict(_parent_product)

        _parent_dataset = d.pop("parentDataset", UNSET)
        parent_dataset: Union[Unset, SendigDatasetRef]
        if isinstance(_parent_dataset, Unset):
            parent_dataset = UNSET
        else:
            parent_dataset = SendigDatasetRef.from_dict(_parent_dataset)

        _root_item = d.pop("rootItem", UNSET)
        root_item: Union[Unset, RootSendigDatasetVariableRef]
        if isinstance(_root_item, Unset):
            root_item = UNSET
        else:
            root_item = RootSendigDatasetVariableRef.from_dict(_root_item)

        _prior_version = d.pop("priorVersion", UNSET)
        prior_version: Union[Unset, SendigDatasetVariableRef]
        if isinstance(_prior_version, Unset):
            prior_version = UNSET
        else:
            prior_version = SendigDatasetVariableRef.from_dict(_prior_version)

        sendig_dataset_variable_links = cls(
            self_=self_,
            codelist=codelist,
            model_class_variable=model_class_variable,
            model_dataset_variable=model_dataset_variable,
            parent_product=parent_product,
            parent_dataset=parent_dataset,
            root_item=root_item,
            prior_version=prior_version,
        )

        sendig_dataset_variable_links.additional_properties = d
        return sendig_dataset_variable_links

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
