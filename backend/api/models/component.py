from pydantic import BaseModel

from .common_metadata import CommonMetadataIncomplete, CommonMetadataSummary


class ComponentFromFile(CommonMetadataIncomplete):
    """Component of hybrid model."""


class ComponentSummary(CommonMetadataSummary, extra="ignore"):
    """Essential metadata fields for hybrid model components."""


class Component(ComponentFromFile, ComponentSummary):
    """Component of hybrid model."""


class ComponentReference(BaseModel, extra="forbid"):
    """Reference to an existing component of a hybrid model."""

    id: str
