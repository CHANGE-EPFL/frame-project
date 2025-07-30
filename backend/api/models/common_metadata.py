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

    description: str = Field(
        min_length=1, description="Summarized description of the hybrid model. Can be formatted with HTML tags."
    )
    created: date | None = Field(None, description="Date when the hybrid was created. (e.g. 2000-12-31).")
    id: str = Field(
        min_length=1,
        pattern="^[a-z0-9_]+$",
        description=(
            "Short name that serves as unique identifier for the hybrid model. Should be all lowercase and"
            ' contain no spaces (use "_" instead) or special characters.'
        ),
    )
    keywords: NonEmptyList = Field(description="List of keywords that describe the hybrid model.")
    name: str = Field(min_length=1, description="Full name of the hybrid model.")


class CommonMetadataSummaryIncomplete(BaseModel, extra="forbid"):
    """Essential metadata fields for components that allows for missing fields."""

    description: str = Field(
        min_length=1, description="Summarized description of the component. Can be formatted with HTML tags."
    )
    created: date | None = Field(
        None,
        description=(
            "Date when the component was created (e.g. 2000-12-31)."
            " If not provided, will be filled with the associated hybrid model's creation date."
        ),
    )
    id: str = Field(
        min_length=1,
        pattern="^[a-z0-9_]+$",
        description=(
            "Short name that serves as unique identifier for the component. Should be all lowercase and contain no"
            ' spaces (use "_" instead) or special characters.'
        ),
    )
    keywords: list[str] = Field(
        [],
        description=(
            f"{CommonMetadataSummary.model_fields['keywords'].description}"
            " If not provided, will be filled with the associated hybrid model's keywords."
        ),
    )
    name: str = Field(min_length=1, description="Full name of the component.")


class CommonMetadata(CommonMetadataSummary):
    """Common metadata fields for hybrid models."""

    contributors: NonEmptyList = Field(description="List of contributor names.")
    documentation: list[str] | None = Field(None, description="List of URLs or DOIs for documentation.")
    identifier: str | None = Field(None, description="Digital Object Identifier (DOI).")
    license: str | None = Field(None, description="License short name.")
    readme: str | None = Field(None, description="URL to a Markdown README file.")
    url: str = Field(min_length=1, description="Repository URL.")
    version: str | None = Field(None, description="Semantic version.")


class CommonMetadataIncomplete(CommonMetadataSummaryIncomplete):
    """Common metadata fields for components that allows for missing fields."""

    contributors: list[str] = Field(
        [],
        description=(
            "List of contributor names. If not provided, will be filled with the associated hybrid model's"
            " contributors."
        ),
    )
    documentation: list[str] | None = Field(
        None,
        description=(
            "List of URLs or DOIs for documentation. If not provided, will be filled with the associated hybrid model's"
            " list of documentation."
        ),
    )
    identifier: str | None = Field(
        None,
        description=(
            "Digital Object Identifier (DOI). If not provided, will be filled with the associated hybrid model's DOI."
        ),
    )
    license: str | None = Field(
        None,
        description=("License short name. If not provided, will be filled with the associated hybrid model's license."),
    )
    readme: str | None = Field(
        None,
        description=(
            "URL to a Markdown README file. If not provided, will be filled with the associated hybrid model's README"
            " URL."
        ),
    )
    url: str | None = Field(
        None,
        description=(
            "Repository URL. If not provided, will be filled with the associated hybrid model's repository URL."
        ),
    )
    version: str | None = Field(
        None,
        description="Semantic version. If not provided, will be filled with the associated hybrid model's version.",
    )
