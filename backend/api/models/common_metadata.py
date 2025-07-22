"""Common metadata fields for hybrid models and components.

Based on Dublin Core Metadata Initiative (DCMI) Metadata Terms.
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
"""

from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field, conlist

if TYPE_CHECKING:  # Static type checker may not accept conlist
    NonEmptyList = list[str]
else:
    NonEmptyList = conlist(str, min_length=1)


class CommonMetadataSummary(BaseModel, extra="forbid"):
    """Essential metadata fields for hybrid models."""

    description: str = Field(min_length=1, description="Summarized description of the unit.")
    created: date | None = Field(None, description="Date when the unit was created. E.g. 2000-12-31.")
    id: str = Field(
        min_length=1,
        pattern="^[a-z0-9_]+$",
        description=(
            "Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces"
            '(use "_" instead) or special characters.'
        ),
    )
    keywords: NonEmptyList = Field(description="List of keywords that describe the unit.")
    name: str = Field(min_length=1, description="Full name of the unit.")


class CommonMetadataSummaryIncomplete(BaseModel, extra="forbid"):
    """Essential metadata fields for components that allows for missing fields."""

    description: str = Field(description=CommonMetadataSummary.model_fields["description"].description)
    created: date | None = Field(
        None,
        description=(
            f"{CommonMetadataSummary.model_fields['created'].description}"
            " If not provided, will be filled with the associated hybrid model's creation date."
        ),
    )
    id: str = Field(min_length=1, description=CommonMetadataSummary.model_fields["id"].description)
    keywords: list[str] = Field(
        [],
        description=(
            f"{CommonMetadataSummary.model_fields['keywords'].description}"
            " If not provided, will be filled with the associated hybrid model's keywords."
        ),
    )
    name: str = Field(min_length=1, description=CommonMetadataSummary.model_fields["name"].description)


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models."""

    #: List of contributor names
    contributors: NonEmptyList
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Markdown readme URL
    readme: str | None = None
    #: Repository URL
    url: str = Field(..., min_length=1)
    #: Semantic version
    version: str | None = None


class CommonMetadataIncomplete(CommonMetadataSummaryIncomplete):
    """Common metadata fields for components that allows for missing fields."""

    #: List of contributor names
    contributors: list[str] = []
    #: URLs or DOIs
    documentation: list[str] | None = None
    #: DOI
    identifier: str | None = None
    license: str | None = None
    #: Markdown readme URL
    readme: str | None = None
    #: Repository URL
    url: str | None = None
    #: Semantic version
    version: str | None = None
