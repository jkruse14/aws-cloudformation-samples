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
class AwsIotSoftwarepackageversion(BaseModel):
    Attributes: Optional[MutableMapping[str, str]]
    Description: Optional[str]
    ErrorReason: Optional[str]
    PackageName: Optional[str]
    PackageVersionArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]
    VersionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotSoftwarepackageversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotSoftwarepackageversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Attributes=json_data.get("Attributes"),
            Description=json_data.get("Description"),
            ErrorReason=json_data.get("ErrorReason"),
            PackageName=json_data.get("PackageName"),
            PackageVersionArn=json_data.get("PackageVersionArn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            VersionName=json_data.get("VersionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotSoftwarepackageversion = AwsIotSoftwarepackageversion


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


