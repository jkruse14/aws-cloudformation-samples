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
class AwsOpensearchserverlessCollection(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Any]
    Arn: Optional[str]
    CollectionEndpoint: Optional[str]
    DashboardEndpoint: Optional[str]
    Type: Optional[str]
    StandbyReplicas: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpensearchserverlessCollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpensearchserverlessCollection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            CollectionEndpoint=json_data.get("CollectionEndpoint"),
            DashboardEndpoint=json_data.get("DashboardEndpoint"),
            Type=json_data.get("Type"),
            StandbyReplicas=json_data.get("StandbyReplicas"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpensearchserverlessCollection = AwsOpensearchserverlessCollection


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


