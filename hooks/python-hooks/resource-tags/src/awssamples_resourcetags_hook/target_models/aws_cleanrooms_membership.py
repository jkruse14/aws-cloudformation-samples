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
class AwsCleanroomsMembership(BaseModel):
    Arn: Optional[str]
    Tags: Optional[Any]
    CollaborationArn: Optional[str]
    CollaborationCreatorAccountId: Optional[str]
    CollaborationIdentifier: Optional[str]
    MembershipIdentifier: Optional[str]
    QueryLogStatus: Optional[str]
    DefaultResultConfiguration: Optional["_MembershipProtectedQueryResultConfiguration"]
    PaymentConfiguration: Optional["_MembershipPaymentConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCleanroomsMembership"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCleanroomsMembership"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            CollaborationArn=json_data.get("CollaborationArn"),
            CollaborationCreatorAccountId=json_data.get("CollaborationCreatorAccountId"),
            CollaborationIdentifier=json_data.get("CollaborationIdentifier"),
            MembershipIdentifier=json_data.get("MembershipIdentifier"),
            QueryLogStatus=json_data.get("QueryLogStatus"),
            DefaultResultConfiguration=MembershipProtectedQueryResultConfiguration._deserialize(json_data.get("DefaultResultConfiguration")),
            PaymentConfiguration=MembershipPaymentConfiguration._deserialize(json_data.get("PaymentConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCleanroomsMembership = AwsCleanroomsMembership


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


@dataclass
class MembershipProtectedQueryResultConfiguration(BaseModel):
    OutputConfiguration: Optional["_MembershipProtectedQueryOutputConfiguration"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembershipProtectedQueryResultConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembershipProtectedQueryResultConfiguration"]:
        if not json_data:
            return None
        return cls(
            OutputConfiguration=MembershipProtectedQueryOutputConfiguration._deserialize(json_data.get("OutputConfiguration")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembershipProtectedQueryResultConfiguration = MembershipProtectedQueryResultConfiguration


@dataclass
class MembershipProtectedQueryOutputConfiguration(BaseModel):
    S3: Optional["_ProtectedQueryS3OutputConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_MembershipProtectedQueryOutputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembershipProtectedQueryOutputConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3=ProtectedQueryS3OutputConfiguration._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembershipProtectedQueryOutputConfiguration = MembershipProtectedQueryOutputConfiguration


@dataclass
class ProtectedQueryS3OutputConfiguration(BaseModel):
    ResultFormat: Optional[str]
    Bucket: Optional[str]
    KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtectedQueryS3OutputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtectedQueryS3OutputConfiguration"]:
        if not json_data:
            return None
        return cls(
            ResultFormat=json_data.get("ResultFormat"),
            Bucket=json_data.get("Bucket"),
            KeyPrefix=json_data.get("KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtectedQueryS3OutputConfiguration = ProtectedQueryS3OutputConfiguration


@dataclass
class MembershipPaymentConfiguration(BaseModel):
    QueryCompute: Optional["_MembershipQueryComputePaymentConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_MembershipPaymentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembershipPaymentConfiguration"]:
        if not json_data:
            return None
        return cls(
            QueryCompute=MembershipQueryComputePaymentConfig._deserialize(json_data.get("QueryCompute")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembershipPaymentConfiguration = MembershipPaymentConfiguration


@dataclass
class MembershipQueryComputePaymentConfig(BaseModel):
    IsResponsible: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MembershipQueryComputePaymentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembershipQueryComputePaymentConfig"]:
        if not json_data:
            return None
        return cls(
            IsResponsible=json_data.get("IsResponsible"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembershipQueryComputePaymentConfig = MembershipQueryComputePaymentConfig


