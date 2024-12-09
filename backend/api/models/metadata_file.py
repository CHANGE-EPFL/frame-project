from pydantic import BaseModel

from .data import DataIO
from .hybrid_model import HybridModelFromFile
from .machine_learning_component import MachineLearningComponentFromFile
from .physics_based_component import PhysicsBasedComponentFromFile


class MetadataFromFile(BaseModel, extra="forbid"):
    """Metadata fields for a metadata file."""

    hybrid_model: HybridModelFromFile
    physics_based_components: list[PhysicsBasedComponentFromFile] = []
    machine_learning_components: list[MachineLearningComponentFromFile] = []
    data: DataIO = DataIO()
