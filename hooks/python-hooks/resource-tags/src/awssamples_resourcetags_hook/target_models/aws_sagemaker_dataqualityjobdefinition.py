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
class AwsSagemakerDataqualityjobdefinition(BaseModel):
    JobDefinitionArn: Optional[str]
    JobDefinitionName: Optional[str]
    DataQualityBaselineConfig: Optional["_DataQualityBaselineConfig"]
    DataQualityAppSpecification: Optional["_DataQualityAppSpecification"]
    DataQualityJobInput: Optional["_DataQualityJobInput"]
    DataQualityJobOutputConfig: Optional["_MonitoringOutputConfig"]
    JobResources: Optional["_MonitoringResources"]
    NetworkConfig: Optional["_NetworkConfig"]
    EndpointName: Optional[str]
    RoleArn: Optional[str]
    StoppingCondition: Optional["_StoppingCondition"]
    Tags: Optional[Any]
    CreationTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerDataqualityjobdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerDataqualityjobdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            JobDefinitionArn=json_data.get("JobDefinitionArn"),
            JobDefinitionName=json_data.get("JobDefinitionName"),
            DataQualityBaselineConfig=DataQualityBaselineConfig._deserialize(json_data.get("DataQualityBaselineConfig")),
            DataQualityAppSpecification=DataQualityAppSpecification._deserialize(json_data.get("DataQualityAppSpecification")),
            DataQualityJobInput=DataQualityJobInput._deserialize(json_data.get("DataQualityJobInput")),
            DataQualityJobOutputConfig=MonitoringOutputConfig._deserialize(json_data.get("DataQualityJobOutputConfig")),
            JobResources=MonitoringResources._deserialize(json_data.get("JobResources")),
            NetworkConfig=NetworkConfig._deserialize(json_data.get("NetworkConfig")),
            EndpointName=json_data.get("EndpointName"),
            RoleArn=json_data.get("RoleArn"),
            StoppingCondition=StoppingCondition._deserialize(json_data.get("StoppingCondition")),
            Tags=json_data.get("Tags"),
            CreationTime=json_data.get("CreationTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerDataqualityjobdefinition = AwsSagemakerDataqualityjobdefinition


@dataclass
class DataQualityBaselineConfig(BaseModel):
    BaseliningJobName: Optional[str]
    ConstraintsResource: Optional["_ConstraintsResource"]
    StatisticsResource: Optional["_StatisticsResource"]

    @classmethod
    def _deserialize(
        cls: Type["_DataQualityBaselineConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataQualityBaselineConfig"]:
        if not json_data:
            return None
        return cls(
            BaseliningJobName=json_data.get("BaseliningJobName"),
            ConstraintsResource=ConstraintsResource._deserialize(json_data.get("ConstraintsResource")),
            StatisticsResource=StatisticsResource._deserialize(json_data.get("StatisticsResource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataQualityBaselineConfig = DataQualityBaselineConfig


@dataclass
class ConstraintsResource(BaseModel):
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsResource"]:
        if not json_data:
            return None
        return cls(
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsResource = ConstraintsResource


@dataclass
class StatisticsResource(BaseModel):
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatisticsResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatisticsResource"]:
        if not json_data:
            return None
        return cls(
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatisticsResource = StatisticsResource


@dataclass
class DataQualityAppSpecification(BaseModel):
    ContainerArguments: Optional[Sequence[str]]
    ContainerEntrypoint: Optional[Sequence[str]]
    ImageUri: Optional[str]
    PostAnalyticsProcessorSourceUri: Optional[str]
    RecordPreprocessorSourceUri: Optional[str]
    Environment: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_DataQualityAppSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataQualityAppSpecification"]:
        if not json_data:
            return None
        return cls(
            ContainerArguments=json_data.get("ContainerArguments"),
            ContainerEntrypoint=json_data.get("ContainerEntrypoint"),
            ImageUri=json_data.get("ImageUri"),
            PostAnalyticsProcessorSourceUri=json_data.get("PostAnalyticsProcessorSourceUri"),
            RecordPreprocessorSourceUri=json_data.get("RecordPreprocessorSourceUri"),
            Environment=json_data.get("Environment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataQualityAppSpecification = DataQualityAppSpecification


@dataclass
class DataQualityJobInput(BaseModel):
    EndpointInput: Optional["_EndpointInput"]
    BatchTransformInput: Optional["_BatchTransformInput"]

    @classmethod
    def _deserialize(
        cls: Type["_DataQualityJobInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataQualityJobInput"]:
        if not json_data:
            return None
        return cls(
            EndpointInput=EndpointInput._deserialize(json_data.get("EndpointInput")),
            BatchTransformInput=BatchTransformInput._deserialize(json_data.get("BatchTransformInput")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataQualityJobInput = DataQualityJobInput


@dataclass
class EndpointInput(BaseModel):
    EndpointName: Optional[str]
    LocalPath: Optional[str]
    S3DataDistributionType: Optional[str]
    S3InputMode: Optional[str]
    ExcludeFeaturesAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointInput"]:
        if not json_data:
            return None
        return cls(
            EndpointName=json_data.get("EndpointName"),
            LocalPath=json_data.get("LocalPath"),
            S3DataDistributionType=json_data.get("S3DataDistributionType"),
            S3InputMode=json_data.get("S3InputMode"),
            ExcludeFeaturesAttribute=json_data.get("ExcludeFeaturesAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointInput = EndpointInput


@dataclass
class BatchTransformInput(BaseModel):
    DataCapturedDestinationS3Uri: Optional[str]
    DatasetFormat: Optional["_DatasetFormat"]
    LocalPath: Optional[str]
    S3DataDistributionType: Optional[str]
    S3InputMode: Optional[str]
    ExcludeFeaturesAttribute: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchTransformInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchTransformInput"]:
        if not json_data:
            return None
        return cls(
            DataCapturedDestinationS3Uri=json_data.get("DataCapturedDestinationS3Uri"),
            DatasetFormat=DatasetFormat._deserialize(json_data.get("DatasetFormat")),
            LocalPath=json_data.get("LocalPath"),
            S3DataDistributionType=json_data.get("S3DataDistributionType"),
            S3InputMode=json_data.get("S3InputMode"),
            ExcludeFeaturesAttribute=json_data.get("ExcludeFeaturesAttribute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchTransformInput = BatchTransformInput


@dataclass
class DatasetFormat(BaseModel):
    Csv: Optional["_Csv"]
    Json: Optional["_Json"]
    Parquet: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetFormat"]:
        if not json_data:
            return None
        return cls(
            Csv=Csv._deserialize(json_data.get("Csv")),
            Json=Json._deserialize(json_data.get("Json")),
            Parquet=json_data.get("Parquet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetFormat = DatasetFormat


@dataclass
class Csv(BaseModel):
    Header: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Csv"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Csv"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Csv = Csv


@dataclass
class Json(BaseModel):
    Line: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Json"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Json"]:
        if not json_data:
            return None
        return cls(
            Line=json_data.get("Line"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Json = Json


@dataclass
class MonitoringOutputConfig(BaseModel):
    KmsKeyId: Optional[str]
    MonitoringOutputs: Optional[Sequence["_MonitoringOutput"]]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringOutputConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringOutputConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            MonitoringOutputs=deserialize_list(json_data.get("MonitoringOutputs"), MonitoringOutput),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringOutputConfig = MonitoringOutputConfig


@dataclass
class MonitoringOutput(BaseModel):
    S3Output: Optional["_S3Output"]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringOutput"]:
        if not json_data:
            return None
        return cls(
            S3Output=S3Output._deserialize(json_data.get("S3Output")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringOutput = MonitoringOutput


@dataclass
class S3Output(BaseModel):
    LocalPath: Optional[str]
    S3UploadMode: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Output"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Output"]:
        if not json_data:
            return None
        return cls(
            LocalPath=json_data.get("LocalPath"),
            S3UploadMode=json_data.get("S3UploadMode"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Output = S3Output


@dataclass
class MonitoringResources(BaseModel):
    ClusterConfig: Optional["_ClusterConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringResources"]:
        if not json_data:
            return None
        return cls(
            ClusterConfig=ClusterConfig._deserialize(json_data.get("ClusterConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringResources = MonitoringResources


@dataclass
class ClusterConfig(BaseModel):
    InstanceCount: Optional[int]
    InstanceType: Optional[str]
    VolumeKmsKeyId: Optional[str]
    VolumeSizeInGB: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfig"]:
        if not json_data:
            return None
        return cls(
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            VolumeKmsKeyId=json_data.get("VolumeKmsKeyId"),
            VolumeSizeInGB=json_data.get("VolumeSizeInGB"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfig = ClusterConfig


@dataclass
class NetworkConfig(BaseModel):
    EnableInterContainerTrafficEncryption: Optional[bool]
    EnableNetworkIsolation: Optional[bool]
    VpcConfig: Optional["_VpcConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfig"]:
        if not json_data:
            return None
        return cls(
            EnableInterContainerTrafficEncryption=json_data.get("EnableInterContainerTrafficEncryption"),
            EnableNetworkIsolation=json_data.get("EnableNetworkIsolation"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfig = NetworkConfig


@dataclass
class VpcConfig(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class StoppingCondition(BaseModel):
    MaxRuntimeInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StoppingCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StoppingCondition"]:
        if not json_data:
            return None
        return cls(
            MaxRuntimeInSeconds=json_data.get("MaxRuntimeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StoppingCondition = StoppingCondition


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


