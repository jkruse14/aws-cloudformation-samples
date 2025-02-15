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
class AwsWafv2Rulegroup(BaseModel):
    Arn: Optional[str]
    Capacity: Optional[int]
    Description: Optional[str]
    Name: Optional[str]
    Id: Optional[str]
    Scope: Optional[str]
    Rules: Optional[Sequence["_Rule"]]
    VisibilityConfig: Optional["_VisibilityConfig"]
    Tags: Optional[Any]
    LabelNamespace: Optional[str]
    CustomResponseBodies: Optional[MutableMapping[str, "_CustomResponseBody"]]
    AvailableLabels: Optional[Sequence["_LabelSummary"]]
    ConsumedLabels: Optional[Sequence["_LabelSummary"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWafv2Rulegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWafv2Rulegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Capacity=json_data.get("Capacity"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Id=json_data.get("Id"),
            Scope=json_data.get("Scope"),
            Rules=deserialize_list(json_data.get("Rules"), Rule),
            VisibilityConfig=VisibilityConfig._deserialize(json_data.get("VisibilityConfig")),
            Tags=json_data.get("Tags"),
            LabelNamespace=json_data.get("LabelNamespace"),
            CustomResponseBodies=json_data.get("CustomResponseBodies"),
            AvailableLabels=deserialize_list(json_data.get("AvailableLabels"), LabelSummary),
            ConsumedLabels=deserialize_list(json_data.get("ConsumedLabels"), LabelSummary),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWafv2Rulegroup = AwsWafv2Rulegroup


@dataclass
class Rule(BaseModel):
    Name: Optional[str]
    Priority: Optional[int]
    Statement: Optional["_Statement"]
    Action: Optional["_RuleAction"]
    RuleLabels: Optional[Sequence["_Label"]]
    VisibilityConfig: Optional["_VisibilityConfig"]
    CaptchaConfig: Optional["_CaptchaConfig"]
    ChallengeConfig: Optional["_ChallengeConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Statement=Statement._deserialize(json_data.get("Statement")),
            Action=RuleAction._deserialize(json_data.get("Action")),
            RuleLabels=deserialize_list(json_data.get("RuleLabels"), Label),
            VisibilityConfig=VisibilityConfig._deserialize(json_data.get("VisibilityConfig")),
            CaptchaConfig=CaptchaConfig._deserialize(json_data.get("CaptchaConfig")),
            ChallengeConfig=ChallengeConfig._deserialize(json_data.get("ChallengeConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Statement(BaseModel):
    ByteMatchStatement: Optional["_ByteMatchStatement"]
    SqliMatchStatement: Optional["_SqliMatchStatement"]
    XssMatchStatement: Optional["_XssMatchStatement"]
    SizeConstraintStatement: Optional["_SizeConstraintStatement"]
    GeoMatchStatement: Optional["_GeoMatchStatement"]
    IPSetReferenceStatement: Optional["_IPSetReferenceStatement"]
    RegexPatternSetReferenceStatement: Optional["_RegexPatternSetReferenceStatement"]
    RateBasedStatement: Optional["_RateBasedStatement"]
    AndStatement: Optional["_AndStatement"]
    OrStatement: Optional["_OrStatement"]
    NotStatement: Optional["_NotStatement"]
    LabelMatchStatement: Optional["_LabelMatchStatement"]
    RegexMatchStatement: Optional["_RegexMatchStatement"]

    @classmethod
    def _deserialize(
        cls: Type["_Statement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Statement"]:
        if not json_data:
            return None
        return cls(
            ByteMatchStatement=ByteMatchStatement._deserialize(json_data.get("ByteMatchStatement")),
            SqliMatchStatement=SqliMatchStatement._deserialize(json_data.get("SqliMatchStatement")),
            XssMatchStatement=XssMatchStatement._deserialize(json_data.get("XssMatchStatement")),
            SizeConstraintStatement=SizeConstraintStatement._deserialize(json_data.get("SizeConstraintStatement")),
            GeoMatchStatement=GeoMatchStatement._deserialize(json_data.get("GeoMatchStatement")),
            IPSetReferenceStatement=IPSetReferenceStatement._deserialize(json_data.get("IPSetReferenceStatement")),
            RegexPatternSetReferenceStatement=RegexPatternSetReferenceStatement._deserialize(json_data.get("RegexPatternSetReferenceStatement")),
            RateBasedStatement=RateBasedStatement._deserialize(json_data.get("RateBasedStatement")),
            AndStatement=AndStatement._deserialize(json_data.get("AndStatement")),
            OrStatement=OrStatement._deserialize(json_data.get("OrStatement")),
            NotStatement=NotStatement._deserialize(json_data.get("NotStatement")),
            LabelMatchStatement=LabelMatchStatement._deserialize(json_data.get("LabelMatchStatement")),
            RegexMatchStatement=RegexMatchStatement._deserialize(json_data.get("RegexMatchStatement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Statement = Statement


@dataclass
class ByteMatchStatement(BaseModel):
    SearchString: Optional[str]
    SearchStringBase64: Optional[str]
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformations: Optional[Sequence["_TextTransformation"]]
    PositionalConstraint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ByteMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ByteMatchStatement"]:
        if not json_data:
            return None
        return cls(
            SearchString=json_data.get("SearchString"),
            SearchStringBase64=json_data.get("SearchStringBase64"),
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
            PositionalConstraint=json_data.get("PositionalConstraint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ByteMatchStatement = ByteMatchStatement


@dataclass
class FieldToMatch(BaseModel):
    SingleHeader: Optional["_SingleHeader"]
    SingleQueryArgument: Optional["_SingleQueryArgument"]
    AllQueryArguments: Optional[MutableMapping[str, Any]]
    UriPath: Optional[MutableMapping[str, Any]]
    QueryString: Optional[MutableMapping[str, Any]]
    Body: Optional["_Body"]
    Method: Optional[MutableMapping[str, Any]]
    JsonBody: Optional["_JsonBody"]
    Headers: Optional["_Headers"]
    Cookies: Optional["_Cookies"]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatch"]:
        if not json_data:
            return None
        return cls(
            SingleHeader=SingleHeader._deserialize(json_data.get("SingleHeader")),
            SingleQueryArgument=SingleQueryArgument._deserialize(json_data.get("SingleQueryArgument")),
            AllQueryArguments=json_data.get("AllQueryArguments"),
            UriPath=json_data.get("UriPath"),
            QueryString=json_data.get("QueryString"),
            Body=Body._deserialize(json_data.get("Body")),
            Method=json_data.get("Method"),
            JsonBody=JsonBody._deserialize(json_data.get("JsonBody")),
            Headers=Headers._deserialize(json_data.get("Headers")),
            Cookies=Cookies._deserialize(json_data.get("Cookies")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatch = FieldToMatch


@dataclass
class SingleHeader(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleHeader = SingleHeader


@dataclass
class SingleQueryArgument(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleQueryArgument"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleQueryArgument"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleQueryArgument = SingleQueryArgument


@dataclass
class Body(BaseModel):
    OversizeHandling: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Body"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Body"]:
        if not json_data:
            return None
        return cls(
            OversizeHandling=json_data.get("OversizeHandling"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Body = Body


@dataclass
class JsonBody(BaseModel):
    MatchPattern: Optional["_JsonMatchPattern"]
    MatchScope: Optional[str]
    InvalidFallbackBehavior: Optional[str]
    OversizeHandling: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonBody"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonBody"]:
        if not json_data:
            return None
        return cls(
            MatchPattern=JsonMatchPattern._deserialize(json_data.get("MatchPattern")),
            MatchScope=json_data.get("MatchScope"),
            InvalidFallbackBehavior=json_data.get("InvalidFallbackBehavior"),
            OversizeHandling=json_data.get("OversizeHandling"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonBody = JsonBody


@dataclass
class JsonMatchPattern(BaseModel):
    All: Optional[MutableMapping[str, Any]]
    IncludedPaths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_JsonMatchPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonMatchPattern"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            IncludedPaths=json_data.get("IncludedPaths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonMatchPattern = JsonMatchPattern


@dataclass
class Headers(BaseModel):
    MatchPattern: Optional["_HeaderMatchPattern"]
    MatchScope: Optional[str]
    OversizeHandling: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            MatchPattern=HeaderMatchPattern._deserialize(json_data.get("MatchPattern")),
            MatchScope=json_data.get("MatchScope"),
            OversizeHandling=json_data.get("OversizeHandling"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class HeaderMatchPattern(BaseModel):
    All: Optional[MutableMapping[str, Any]]
    IncludedHeaders: Optional[Sequence[str]]
    ExcludedHeaders: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatchPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatchPattern"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            IncludedHeaders=json_data.get("IncludedHeaders"),
            ExcludedHeaders=json_data.get("ExcludedHeaders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatchPattern = HeaderMatchPattern


@dataclass
class Cookies(BaseModel):
    MatchPattern: Optional["_CookieMatchPattern"]
    MatchScope: Optional[str]
    OversizeHandling: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cookies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cookies"]:
        if not json_data:
            return None
        return cls(
            MatchPattern=CookieMatchPattern._deserialize(json_data.get("MatchPattern")),
            MatchScope=json_data.get("MatchScope"),
            OversizeHandling=json_data.get("OversizeHandling"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cookies = Cookies


@dataclass
class CookieMatchPattern(BaseModel):
    All: Optional[MutableMapping[str, Any]]
    IncludedCookies: Optional[Sequence[str]]
    ExcludedCookies: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieMatchPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieMatchPattern"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            IncludedCookies=json_data.get("IncludedCookies"),
            ExcludedCookies=json_data.get("ExcludedCookies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieMatchPattern = CookieMatchPattern


@dataclass
class TextTransformation(BaseModel):
    Priority: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TextTransformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextTransformation"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextTransformation = TextTransformation


@dataclass
class SqliMatchStatement(BaseModel):
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformations: Optional[Sequence["_TextTransformation"]]
    SensitivityLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqliMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqliMatchStatement"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
            SensitivityLevel=json_data.get("SensitivityLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqliMatchStatement = SqliMatchStatement


@dataclass
class XssMatchStatement(BaseModel):
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_XssMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XssMatchStatement"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_XssMatchStatement = XssMatchStatement


@dataclass
class SizeConstraintStatement(BaseModel):
    FieldToMatch: Optional["_FieldToMatch"]
    ComparisonOperator: Optional[str]
    Size: Optional[float]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_SizeConstraintStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SizeConstraintStatement"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Size=json_data.get("Size"),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_SizeConstraintStatement = SizeConstraintStatement


@dataclass
class GeoMatchStatement(BaseModel):
    CountryCodes: Optional[Sequence[str]]
    ForwardedIPConfig: Optional["_ForwardedIPConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_GeoMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoMatchStatement"]:
        if not json_data:
            return None
        return cls(
            CountryCodes=json_data.get("CountryCodes"),
            ForwardedIPConfig=ForwardedIPConfiguration._deserialize(json_data.get("ForwardedIPConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoMatchStatement = GeoMatchStatement


@dataclass
class ForwardedIPConfiguration(BaseModel):
    HeaderName: Optional[str]
    FallbackBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardedIPConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardedIPConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            FallbackBehavior=json_data.get("FallbackBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardedIPConfiguration = ForwardedIPConfiguration


@dataclass
class IPSetReferenceStatement(BaseModel):
    Arn: Optional[str]
    IPSetForwardedIPConfig: Optional["_IPSetForwardedIPConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_IPSetReferenceStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IPSetReferenceStatement"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            IPSetForwardedIPConfig=IPSetForwardedIPConfiguration._deserialize(json_data.get("IPSetForwardedIPConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IPSetReferenceStatement = IPSetReferenceStatement


@dataclass
class IPSetForwardedIPConfiguration(BaseModel):
    HeaderName: Optional[str]
    FallbackBehavior: Optional[str]
    Position: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IPSetForwardedIPConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IPSetForwardedIPConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            FallbackBehavior=json_data.get("FallbackBehavior"),
            Position=json_data.get("Position"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IPSetForwardedIPConfiguration = IPSetForwardedIPConfiguration


@dataclass
class RegexPatternSetReferenceStatement(BaseModel):
    Arn: Optional[str]
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RegexPatternSetReferenceStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexPatternSetReferenceStatement"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexPatternSetReferenceStatement = RegexPatternSetReferenceStatement


@dataclass
class RateBasedStatement(BaseModel):
    Limit: Optional[int]
    AggregateKeyType: Optional[str]
    CustomKeys: Optional[Sequence["_RateBasedStatementCustomKey"]]
    ScopeDownStatement: Optional["_Statement"]
    ForwardedIPConfig: Optional["_ForwardedIPConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RateBasedStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateBasedStatement"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            AggregateKeyType=json_data.get("AggregateKeyType"),
            CustomKeys=deserialize_list(json_data.get("CustomKeys"), RateBasedStatementCustomKey),
            ScopeDownStatement=Statement._deserialize(json_data.get("ScopeDownStatement")),
            ForwardedIPConfig=ForwardedIPConfiguration._deserialize(json_data.get("ForwardedIPConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateBasedStatement = RateBasedStatement


@dataclass
class RateBasedStatementCustomKey(BaseModel):
    Cookie: Optional["_RateLimitCookie"]
    ForwardedIP: Optional[MutableMapping[str, Any]]
    Header: Optional["_RateLimitHeader"]
    HTTPMethod: Optional[MutableMapping[str, Any]]
    IP: Optional[MutableMapping[str, Any]]
    LabelNamespace: Optional["_RateLimitLabelNamespace"]
    QueryArgument: Optional["_RateLimitQueryArgument"]
    QueryString: Optional["_RateLimitQueryString"]
    UriPath: Optional["_RateLimitUriPath"]

    @classmethod
    def _deserialize(
        cls: Type["_RateBasedStatementCustomKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateBasedStatementCustomKey"]:
        if not json_data:
            return None
        return cls(
            Cookie=RateLimitCookie._deserialize(json_data.get("Cookie")),
            ForwardedIP=json_data.get("ForwardedIP"),
            Header=RateLimitHeader._deserialize(json_data.get("Header")),
            HTTPMethod=json_data.get("HTTPMethod"),
            IP=json_data.get("IP"),
            LabelNamespace=RateLimitLabelNamespace._deserialize(json_data.get("LabelNamespace")),
            QueryArgument=RateLimitQueryArgument._deserialize(json_data.get("QueryArgument")),
            QueryString=RateLimitQueryString._deserialize(json_data.get("QueryString")),
            UriPath=RateLimitUriPath._deserialize(json_data.get("UriPath")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateBasedStatementCustomKey = RateBasedStatementCustomKey


@dataclass
class RateLimitCookie(BaseModel):
    Name: Optional[str]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitCookie"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitCookie"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitCookie = RateLimitCookie


@dataclass
class RateLimitHeader(BaseModel):
    Name: Optional[str]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitHeader = RateLimitHeader


@dataclass
class RateLimitLabelNamespace(BaseModel):
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitLabelNamespace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitLabelNamespace"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitLabelNamespace = RateLimitLabelNamespace


@dataclass
class RateLimitQueryArgument(BaseModel):
    Name: Optional[str]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitQueryArgument"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitQueryArgument"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitQueryArgument = RateLimitQueryArgument


@dataclass
class RateLimitQueryString(BaseModel):
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitQueryString"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitQueryString"]:
        if not json_data:
            return None
        return cls(
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitQueryString = RateLimitQueryString


@dataclass
class RateLimitUriPath(BaseModel):
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitUriPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitUriPath"]:
        if not json_data:
            return None
        return cls(
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitUriPath = RateLimitUriPath


@dataclass
class AndStatement(BaseModel):
    Statements: Optional[Sequence["_Statement"]]

    @classmethod
    def _deserialize(
        cls: Type["_AndStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AndStatement"]:
        if not json_data:
            return None
        return cls(
            Statements=deserialize_list(json_data.get("Statements"), Statement),
        )


# work around possible type aliasing issues when variable has same name as a model
_AndStatement = AndStatement


@dataclass
class OrStatement(BaseModel):
    Statements: Optional[Sequence["_Statement"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrStatement"]:
        if not json_data:
            return None
        return cls(
            Statements=deserialize_list(json_data.get("Statements"), Statement),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrStatement = OrStatement


@dataclass
class NotStatement(BaseModel):
    Statement: Optional["_Statement"]

    @classmethod
    def _deserialize(
        cls: Type["_NotStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotStatement"]:
        if not json_data:
            return None
        return cls(
            Statement=Statement._deserialize(json_data.get("Statement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotStatement = NotStatement


@dataclass
class LabelMatchStatement(BaseModel):
    Scope: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelMatchStatement"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelMatchStatement = LabelMatchStatement


@dataclass
class RegexMatchStatement(BaseModel):
    RegexString: Optional[str]
    FieldToMatch: Optional["_FieldToMatch"]
    TextTransformations: Optional[Sequence["_TextTransformation"]]

    @classmethod
    def _deserialize(
        cls: Type["_RegexMatchStatement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexMatchStatement"]:
        if not json_data:
            return None
        return cls(
            RegexString=json_data.get("RegexString"),
            FieldToMatch=FieldToMatch._deserialize(json_data.get("FieldToMatch")),
            TextTransformations=deserialize_list(json_data.get("TextTransformations"), TextTransformation),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexMatchStatement = RegexMatchStatement


@dataclass
class RuleAction(BaseModel):
    Allow: Optional["_AllowAction"]
    Block: Optional["_BlockAction"]
    Count: Optional["_CountAction"]
    Captcha: Optional["_CaptchaAction"]
    Challenge: Optional["_ChallengeAction"]

    @classmethod
    def _deserialize(
        cls: Type["_RuleAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleAction"]:
        if not json_data:
            return None
        return cls(
            Allow=AllowAction._deserialize(json_data.get("Allow")),
            Block=BlockAction._deserialize(json_data.get("Block")),
            Count=CountAction._deserialize(json_data.get("Count")),
            Captcha=CaptchaAction._deserialize(json_data.get("Captcha")),
            Challenge=ChallengeAction._deserialize(json_data.get("Challenge")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleAction = RuleAction


@dataclass
class AllowAction(BaseModel):
    CustomRequestHandling: Optional["_CustomRequestHandling"]

    @classmethod
    def _deserialize(
        cls: Type["_AllowAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowAction"]:
        if not json_data:
            return None
        return cls(
            CustomRequestHandling=CustomRequestHandling._deserialize(json_data.get("CustomRequestHandling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowAction = AllowAction


@dataclass
class CustomRequestHandling(BaseModel):
    InsertHeaders: Optional[Sequence["_CustomHTTPHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRequestHandling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRequestHandling"]:
        if not json_data:
            return None
        return cls(
            InsertHeaders=deserialize_list(json_data.get("InsertHeaders"), CustomHTTPHeader),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRequestHandling = CustomRequestHandling


@dataclass
class CustomHTTPHeader(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHTTPHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHTTPHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHTTPHeader = CustomHTTPHeader


@dataclass
class BlockAction(BaseModel):
    CustomResponse: Optional["_CustomResponse"]

    @classmethod
    def _deserialize(
        cls: Type["_BlockAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockAction"]:
        if not json_data:
            return None
        return cls(
            CustomResponse=CustomResponse._deserialize(json_data.get("CustomResponse")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockAction = BlockAction


@dataclass
class CustomResponse(BaseModel):
    ResponseCode: Optional[int]
    CustomResponseBodyKey: Optional[str]
    ResponseHeaders: Optional[Sequence["_CustomHTTPHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomResponse"]:
        if not json_data:
            return None
        return cls(
            ResponseCode=json_data.get("ResponseCode"),
            CustomResponseBodyKey=json_data.get("CustomResponseBodyKey"),
            ResponseHeaders=deserialize_list(json_data.get("ResponseHeaders"), CustomHTTPHeader),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomResponse = CustomResponse


@dataclass
class CountAction(BaseModel):
    CustomRequestHandling: Optional["_CustomRequestHandling"]

    @classmethod
    def _deserialize(
        cls: Type["_CountAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CountAction"]:
        if not json_data:
            return None
        return cls(
            CustomRequestHandling=CustomRequestHandling._deserialize(json_data.get("CustomRequestHandling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CountAction = CountAction


@dataclass
class CaptchaAction(BaseModel):
    CustomRequestHandling: Optional["_CustomRequestHandling"]

    @classmethod
    def _deserialize(
        cls: Type["_CaptchaAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptchaAction"]:
        if not json_data:
            return None
        return cls(
            CustomRequestHandling=CustomRequestHandling._deserialize(json_data.get("CustomRequestHandling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptchaAction = CaptchaAction


@dataclass
class ChallengeAction(BaseModel):
    CustomRequestHandling: Optional["_CustomRequestHandling"]

    @classmethod
    def _deserialize(
        cls: Type["_ChallengeAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChallengeAction"]:
        if not json_data:
            return None
        return cls(
            CustomRequestHandling=CustomRequestHandling._deserialize(json_data.get("CustomRequestHandling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChallengeAction = ChallengeAction


@dataclass
class Label(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Label"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Label"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Label = Label


@dataclass
class VisibilityConfig(BaseModel):
    SampledRequestsEnabled: Optional[bool]
    CloudWatchMetricsEnabled: Optional[bool]
    MetricName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VisibilityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisibilityConfig"]:
        if not json_data:
            return None
        return cls(
            SampledRequestsEnabled=json_data.get("SampledRequestsEnabled"),
            CloudWatchMetricsEnabled=json_data.get("CloudWatchMetricsEnabled"),
            MetricName=json_data.get("MetricName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisibilityConfig = VisibilityConfig


@dataclass
class CaptchaConfig(BaseModel):
    ImmunityTimeProperty: Optional["_ImmunityTimeProperty"]

    @classmethod
    def _deserialize(
        cls: Type["_CaptchaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptchaConfig"]:
        if not json_data:
            return None
        return cls(
            ImmunityTimeProperty=ImmunityTimeProperty._deserialize(json_data.get("ImmunityTimeProperty")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptchaConfig = CaptchaConfig


@dataclass
class ImmunityTimeProperty(BaseModel):
    ImmunityTime: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ImmunityTimeProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImmunityTimeProperty"]:
        if not json_data:
            return None
        return cls(
            ImmunityTime=json_data.get("ImmunityTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImmunityTimeProperty = ImmunityTimeProperty


@dataclass
class ChallengeConfig(BaseModel):
    ImmunityTimeProperty: Optional["_ImmunityTimeProperty"]

    @classmethod
    def _deserialize(
        cls: Type["_ChallengeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChallengeConfig"]:
        if not json_data:
            return None
        return cls(
            ImmunityTimeProperty=ImmunityTimeProperty._deserialize(json_data.get("ImmunityTimeProperty")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChallengeConfig = ChallengeConfig


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
class CustomResponseBody(BaseModel):
    ContentType: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomResponseBody"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomResponseBody"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomResponseBody = CustomResponseBody


@dataclass
class LabelSummary(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelSummary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelSummary"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelSummary = LabelSummary


