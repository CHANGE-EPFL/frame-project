import json

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


def export_json_schema(output_path: str) -> None:
    """Export JSON schema for MetadataFromFile."""
    json_schema = MetadataFromFile.model_json_schema()

    with open(output_path, "w") as file:
        json.dump(json_schema, file, indent=4)
