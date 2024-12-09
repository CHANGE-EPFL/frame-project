from .common_metadata import CommonMetadata, CommonMetadataSummary
from .data import Data, DataIO


class HybridModelFromFile(CommonMetadata):
    """Hybrid model, without assigned id."""

    ml_process: str | None = None
    host_physics: str | None = None
    latent_variables: list[Data] = []


class HybridModelSummary(CommonMetadataSummary, extra="ignore"):
    """Contains essential metadata fields for hybrid models."""

    id: int
    short_name: str


class HybridModel(HybridModelFromFile, HybridModelSummary):
    """Hybrid model."""

    compatible_machine_learning_component_ids: list[int]
    compatible_physical_based_component_ids: list[int]
    data: DataIO
