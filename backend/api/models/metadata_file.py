from pydantic import BaseModel

from .hybrid_model import HybridModelFromFile
from .machine_learning_component import MachineLearningComponentFromFile
from .physics_based_component import PhysicsBasedComponentFromFile


class MetadataFromFile(BaseModel):
    """Metadata fields for a metadata file."""

    hybrid_model: HybridModelFromFile
    physics_based_components: list[PhysicsBasedComponentFromFile]
    machine_learning_components: list[MachineLearningComponentFromFile]
    data: dict

    # TODO: For testing, remove
    class Config:
        extra = "ignore"  # Ignore extra fields in metadata files
