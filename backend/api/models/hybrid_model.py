from .common_metadata import CommonMetadata, CommonMetadataSummary
from .data import DataIO


class HybridModelFromFile(CommonMetadata):
    """Hybrid model, without assigned id."""

    ml_process: str
    host_physics: str
    latent_variable: str


class HybridModelSummary(CommonMetadataSummary):
    """Contains essential metadata fields for hybrid models."""

    short_name: str


class HybridModel(HybridModelFromFile, HybridModelSummary):
    """Hybrid model."""

    id: int
    compatible_machine_learning_component_ids: list[int]
    compatible_physical_based_component_ids: list[int]
    data: DataIO
