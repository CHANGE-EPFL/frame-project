"""This module contains functions to retrieve metadata about models.

Mock data for testing.
"""

import os
import re
from typing import Any, Callable, TypeVar

import yaml
from fastapi import HTTPException

from ..models.common_metadata import CommonMetadata
from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..models.machine_learning_component import MachineLearningComponent, MachineLearningComponentSummary
from ..models.metadata_file import MetadataFromFile
from ..models.physics_based_component import PhysicsBasedComponent, PhysicsBasedComponentSummary

METADATA_DIR_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "metadata")
METADATA_TEMPLATE_FILENAME = "template.yaml"


def read_yaml(path: str) -> Any:
    with open(path) as f:
        return yaml.safe_load(f.read())


def get_all_metadata_filenames() -> list[str]:
    return [
        filename
        for filename in os.listdir(METADATA_DIR_PATH)
        if filename != METADATA_TEMPLATE_FILENAME and filename.endswith(".yaml")
    ]


def generate_short_name(name: str) -> str:
    return re.sub(r"\W", "_", name).lower()


T = TypeVar("T", PhysicsBasedComponent, MachineLearningComponent)


def add_components(
    metadata: MetadataFromFile,
    components: list[T],
    ComponentType: type[T],
) -> list[int]:
    if ComponentType == PhysicsBasedComponent:
        component_type_name = "physics_based_components"
    else:
        component_type_name = "machine_learning_components"

    ids = []

    for component_from_file in getattr(metadata, component_type_name):
        component_id = len(components)
        component_from_file.short_name = component_from_file.short_name or generate_short_name(component_from_file.name)
        ids.append(component_id)
        component = ComponentType(
            **component_from_file.model_dump(),
            id=component_id,
        )
        components.append(component)

        for field in CommonMetadata.model_fields.keys():
            if not getattr(component, field):  # empty or None
                setattr(component, field, getattr(metadata.hybrid_model, field))

    return ids


def add_model_and_components(
    metadata_filename: str,
    models: list[HybridModel],
    physics_based_components: list[PhysicsBasedComponent],
    machine_learning_components: list[MachineLearningComponent],
) -> None:
    metadata_filepath = os.path.join(METADATA_DIR_PATH, metadata_filename)
    raw_data = read_yaml(metadata_filepath)
    metadata = MetadataFromFile(**raw_data)

    physics_based_component_ids = add_components(metadata, physics_based_components, PhysicsBasedComponent)

    machine_learning_component_ids = add_components(metadata, machine_learning_components, MachineLearningComponent)

    model_id = len(models)
    model_short_name = metadata_filename.split(".")[0]
    model = HybridModel(
        **metadata.hybrid_model.model_dump(),
        short_name=model_short_name,
        id=model_id,
        compatible_physical_based_component_ids=physics_based_component_ids,
        compatible_machine_learning_component_ids=machine_learning_component_ids,
        data=metadata.data,
    )
    models.append(model)


def load_models_and_components() -> (
    tuple[list[HybridModel], list[PhysicsBasedComponent], list[MachineLearningComponent]]
):
    """Load metadata for all models and components.

    Raises:
    """

    models = []
    physics_based_components = []
    machine_learning_components = []

    for metadata_filename in get_all_metadata_filenames():
        add_model_and_components(
            metadata_filename,
            models,
            physics_based_components,
            machine_learning_components,
        )

    return models, physics_based_components, machine_learning_components


models = []
model_summaries = []
physics_based_components = []
physics_based_components_summaries = []
machine_learning_components = []
machine_learning_components_summaries = []
metadata_loaded = False


def _load_metadata():
    """Load models and components metadata in module scope."""
    global models
    global model_summaries
    global physics_based_components
    global physics_based_components_summaries
    global machine_learning_components
    global machine_learning_components_summaries, metadata_loaded

    models, physics_based_components, machine_learning_components = load_models_and_components()
    model_summaries = [HybridModelSummary(**model.model_dump()) for model in models]
    physics_based_components_summaries = [
        PhysicsBasedComponentSummary(**component.model_dump()) for component in physics_based_components
    ]
    machine_learning_components_summaries = [
        MachineLearningComponentSummary(**component.model_dump()) for component in machine_learning_components
    ]

    metadata_loaded = True


def load_metadata(func: Callable):
    """Decorator to trigger loading metadata."""

    async def wrapped(*args, **kwargs):
        if not metadata_loaded:
            _load_metadata()

        return await func(*args, **kwargs)

    return wrapped


@load_metadata
async def get_hybrid_models() -> list[HybridModelSummary]:
    return model_summaries


@load_metadata
async def get_hybrid_model(model_id: int) -> HybridModel:
    try:
        return models[model_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")


@load_metadata
async def get_hybrid_model_short_names() -> list[str]:
    return [model.short_name for model in models]


@load_metadata
async def get_model_physics_based_components(model_id: int) -> list[PhysicsBasedComponentSummary]:
    try:
        model = models[model_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")

    return [
        physics_based_components_summaries[component_id]
        for component_id in model.compatible_physical_based_component_ids
    ]


@load_metadata
async def get_physics_based_component(component_id: int) -> PhysicsBasedComponent:
    try:
        return physics_based_components[component_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="PhysicsBasedComponent not found.")


@load_metadata
async def get_model_machine_learning_components(model_id: int) -> list[MachineLearningComponentSummary]:
    try:
        model = models[model_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")

    return [
        machine_learning_components_summaries[component_id]
        for component_id in model.compatible_machine_learning_component_ids
    ]


@load_metadata
async def get_machine_learning_component(component_id: int) -> MachineLearningComponent:
    try:
        return machine_learning_components[component_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="MachineLearningComponent not found.")
