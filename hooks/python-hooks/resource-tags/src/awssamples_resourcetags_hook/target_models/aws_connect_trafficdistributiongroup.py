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
class AwsConnectTrafficdistributiongroup(BaseModel):
    InstanceArn: Optional[str]
    TrafficDistributionGroupArn: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]
    IsDefault: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectTrafficdistributiongroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectTrafficdistributiongroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            TrafficDistributionGroupArn=json_data.get("TrafficDistributionGroupArn"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            IsDefault=json_data.get("IsDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectTrafficdistributiongroup = AwsConnectTrafficdistributiongroup


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


