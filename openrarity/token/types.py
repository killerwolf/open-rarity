from typing_extensions import NotRequired, TypedDict

AttributeName = str
AttributeValue = str | int | float
TokenId = int | str


class MetadataAttribute(TypedDict):
    """A class to represent `MetadataAttribute`."""
    name: str
    value: str | int | float
    display_type: NotRequired[str | None]


class RawToken(TypedDict):
    """A class to represent `RawToken`."""
    attributes: list[MetadataAttribute]
    token_supply: NotRequired[dict[str | int, int]]


class TokenAttribute(TypedDict):
    """A class to represent `TokenAttribute`."""
    token_id: int
    name: str
    value: str | int | float
    display_type: NotRequired[str | None]


ValidatedTokenAttribute = TypedDict(
    "ValidatedTokenAttribute",
    {
        "token_id": int,
        "name": str,
        "value": str | int | float,
        "display_type": str,
        "token.supply": int,
    },
)
ValidatedTokenNumericAttribute = TypedDict(
    "ValidatedTokenNumericAttribute",
    {
        "token_id": int,
        "name": str,
        "value": str | int | float,
        "display_type": str,
        "token.supply": int,
        "bin": float,
    },
)


AttributeStatistic = TypedDict(
    "AttributeStatistic",
    {
        "name": str,
        "value": str | int | float,
        "attribute.token_count": int,
        "attribute.supply": int,
        "metric.probability": float,
        "metric.information": float,
    },
)

TokenStatistic = TypedDict(
    "TokenStatistic",
    {
        "token_id": str | int,
        "name": str,
        "value": str,
        "attribute.token_count": int,
        "attribute.supply": int,
        "metric.probability": float,
        "metric.information": float,
        "metric.information_entropy": NotRequired[float],
        "metric.unique_trait_count": NotRequired[int],
        "metric.max_trait_information": NotRequired[float],
    },
)


RankedToken = TypedDict(
    "RankedToken",
    {
        "token_id": str | int,
        "metric.probability": float,
        "metric.information": float,
        "metric.unique_trait_count": int,
        "metric.max_trait_information": float,
        "rank": int,
    },
)

TokenSchema = dict[tuple[AttributeName, str], int]

__all__ = [
    "AttributeName",
    "AttributeValue",
    "MetadataAttribute",
    "RawToken",
    "TokenAttribute",
    "AttributeStatistic",
    "RankedToken",
    "TokenSchema",
    "TokenId",
    "TokenStatistic",
    "ValidatedTokenAttribute",
]
