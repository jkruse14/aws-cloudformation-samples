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
class AwsAppconfigConfigurationprofile(BaseModel):
    LocationUri: Optional[str]
    Type: Optional[str]
    Description: Optional[str]
    Validators: Optional[Sequence["_Validators"]]
    RetrievalRoleArn: Optional[str]
    ConfigurationProfileId: Optional[str]
    ApplicationId: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    KmsKeyIdentifier: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigConfigurationprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigConfigurationprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LocationUri=json_data.get("LocationUri"),
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            Validators=deserialize_list(json_data.get("Validators"), Validators),
            RetrievalRoleArn=json_data.get("RetrievalRoleArn"),
            ConfigurationProfileId=json_data.get("ConfigurationProfileId"),
            ApplicationId=json_data.get("ApplicationId"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            KmsKeyIdentifier=json_data.get("KmsKeyIdentifier"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigConfigurationprofile = AwsAppconfigConfigurationprofile


@dataclass
class Validators(BaseModel):
    Type: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Validators"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Validators"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Validators = Validators


@dataclass
class Tags(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


