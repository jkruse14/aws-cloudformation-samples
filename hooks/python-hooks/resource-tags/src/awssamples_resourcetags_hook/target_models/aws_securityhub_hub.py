# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsSecurityhubHub(BaseModel):
    ControlFindingGenerator: Optional[str]
    EnableDefaultStandards: Optional[bool]
    AutoEnableControls: Optional[bool]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecurityhubHub"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecurityhubHub"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ControlFindingGenerator=json_data.get("ControlFindingGenerator"),
            EnableDefaultStandards=json_data.get("EnableDefaultStandards"),
            AutoEnableControls=json_data.get("AutoEnableControls"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecurityhubHub = AwsSecurityhubHub


