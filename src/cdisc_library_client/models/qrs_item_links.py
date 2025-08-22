from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.qrs_responsegroup import QrsResponsegroup
    from ..models.root_ct_term_ref import RootCtTermRef


T = TypeVar("T", bound="QrsItemLinks")


@_attrs_define
class QrsItemLinks:
    """
    Attributes:
        qrs_item_test (Union[Unset, RootCtTermRef]):
        qrs_item_testcd (Union[Unset, RootCtTermRef]):
        qrs_item_eval (Union[Unset, RootCtTermRef]):
        qrs_item_scat (Union[Unset, RootCtTermRef]):
        responsegroup (Union[Unset, QrsResponsegroup]):
    """

    qrs_item_test: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_item_testcd: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_item_eval: Union[Unset, "RootCtTermRef"] = UNSET
    qrs_item_scat: Union[Unset, "RootCtTermRef"] = UNSET
    responsegroup: Union[Unset, "QrsResponsegroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qrs_item_test: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_item_test, Unset):
            qrs_item_test = self.qrs_item_test.to_dict()

        qrs_item_testcd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_item_testcd, Unset):
            qrs_item_testcd = self.qrs_item_testcd.to_dict()

        qrs_item_eval: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_item_eval, Unset):
            qrs_item_eval = self.qrs_item_eval.to_dict()

        qrs_item_scat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qrs_item_scat, Unset):
            qrs_item_scat = self.qrs_item_scat.to_dict()

        responsegroup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsegroup, Unset):
            responsegroup = self.responsegroup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qrs_item_test is not UNSET:
            field_dict["qrsItemTEST"] = qrs_item_test
        if qrs_item_testcd is not UNSET:
            field_dict["qrsItemTESTCD"] = qrs_item_testcd
        if qrs_item_eval is not UNSET:
            field_dict["qrsItemEVAL"] = qrs_item_eval
        if qrs_item_scat is not UNSET:
            field_dict["qrsItemSCAT"] = qrs_item_scat
        if responsegroup is not UNSET:
            field_dict["responsegroup"] = responsegroup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.qrs_responsegroup import QrsResponsegroup
        from ..models.root_ct_term_ref import RootCtTermRef

        d = dict(src_dict)
        _qrs_item_test = d.pop("qrsItemTEST", UNSET)
        qrs_item_test: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_item_test, Unset):
            qrs_item_test = UNSET
        else:
            qrs_item_test = RootCtTermRef.from_dict(_qrs_item_test)

        _qrs_item_testcd = d.pop("qrsItemTESTCD", UNSET)
        qrs_item_testcd: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_item_testcd, Unset):
            qrs_item_testcd = UNSET
        else:
            qrs_item_testcd = RootCtTermRef.from_dict(_qrs_item_testcd)

        _qrs_item_eval = d.pop("qrsItemEVAL", UNSET)
        qrs_item_eval: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_item_eval, Unset):
            qrs_item_eval = UNSET
        else:
            qrs_item_eval = RootCtTermRef.from_dict(_qrs_item_eval)

        _qrs_item_scat = d.pop("qrsItemSCAT", UNSET)
        qrs_item_scat: Union[Unset, RootCtTermRef]
        if isinstance(_qrs_item_scat, Unset):
            qrs_item_scat = UNSET
        else:
            qrs_item_scat = RootCtTermRef.from_dict(_qrs_item_scat)

        _responsegroup = d.pop("responsegroup", UNSET)
        responsegroup: Union[Unset, QrsResponsegroup]
        if isinstance(_responsegroup, Unset):
            responsegroup = UNSET
        else:
            responsegroup = QrsResponsegroup.from_dict(_responsegroup)

        qrs_item_links = cls(
            qrs_item_test=qrs_item_test,
            qrs_item_testcd=qrs_item_testcd,
            qrs_item_eval=qrs_item_eval,
            qrs_item_scat=qrs_item_scat,
            responsegroup=responsegroup,
        )

        qrs_item_links.additional_properties = d
        return qrs_item_links

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
