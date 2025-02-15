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
class AwsManagedblockchainAccessor(BaseModel):
    Arn: Optional[str]
    BillingToken: Optional[str]
    CreationDate: Optional[str]
    Id: Optional[str]
    Status: Optional[str]
    AccessorType: Optional[str]
    NetworkType: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsManagedblockchainAccessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsManagedblockchainAccessor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            BillingToken=json_data.get("BillingToken"),
            CreationDate=json_data.get("CreationDate"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
            AccessorType=json_data.get("AccessorType"),
            NetworkType=json_data.get("NetworkType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsManagedblockchainAccessor = AwsManagedblockchainAccessor


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


