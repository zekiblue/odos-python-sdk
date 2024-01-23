from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssemblePathRequest")


@_attrs_define
class AssemblePathRequest:
    """Assemble Path Request Schema

    Attributes:
        user_addr (str):
        path_id (str):
        simulate (Union[None, Unset, bool]):  Default: False.
        receiver (Union[None, Unset, str]):
    """

    user_addr: str
    path_id: str
    simulate: Union[None, Unset, bool] = False
    receiver: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_addr = self.user_addr

        path_id = self.path_id

        simulate: Union[None, Unset, bool]
        if isinstance(self.simulate, Unset):
            simulate = UNSET
        else:
            simulate = self.simulate

        receiver: Union[None, Unset, str]
        if isinstance(self.receiver, Unset):
            receiver = UNSET
        else:
            receiver = self.receiver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userAddr": user_addr,
                "pathId": path_id,
            }
        )
        if simulate is not UNSET:
            field_dict["simulate"] = simulate
        if receiver is not UNSET:
            field_dict["receiver"] = receiver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_addr = d.pop("userAddr")

        path_id = d.pop("pathId")

        def _parse_simulate(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        simulate = _parse_simulate(d.pop("simulate", UNSET))

        def _parse_receiver(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        receiver = _parse_receiver(d.pop("receiver", UNSET))

        assemble_path_request = cls(
            user_addr=user_addr,
            path_id=path_id,
            simulate=simulate,
            receiver=receiver,
        )

        assemble_path_request.additional_properties = d
        return assemble_path_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
