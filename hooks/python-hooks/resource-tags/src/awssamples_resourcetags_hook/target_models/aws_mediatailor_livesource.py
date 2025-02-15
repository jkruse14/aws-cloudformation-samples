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
class AwsMediatailorLivesource(BaseModel):
    Arn: Optional[str]
    HttpPackageConfigurations: Optional[Sequence["_HttpPackageConfiguration"]]
    LiveSourceName: Optional[str]
    SourceLocationName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediatailorLivesource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediatailorLivesource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            HttpPackageConfigurations=deserialize_list(json_data.get("HttpPackageConfigurations"), HttpPackageConfiguration),
            LiveSourceName=json_data.get("LiveSourceName"),
            SourceLocationName=json_data.get("SourceLocationName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediatailorLivesource = AwsMediatailorLivesource


@dataclass
class HttpPackageConfiguration(BaseModel):
    Path: Optional[str]
    SourceGroup: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpPackageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpPackageConfiguration"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            SourceGroup=json_data.get("SourceGroup"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpPackageConfiguration = HttpPackageConfiguration


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


