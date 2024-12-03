from .common_metadata import CommonMetadataIncomplete, CommonMetadataSummary


class ComponentFromFile(CommonMetadataIncomplete):
    """Component of hybrid model, without assigned id."""


class ComponentSummary(CommonMetadataSummary):
    """Essential metadata fields for hybrid model components."""

    short_name: str


class Component(ComponentFromFile, ComponentSummary):
    """Component of hybrid model."""

    id: int
