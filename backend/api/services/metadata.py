"""This module contains functions to retrieve metadata about models.

Mock data for testing.
"""

import os
import re
from typing import Any

import yaml
from fastapi import HTTPException

from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..models.machine_learning_component import MachineLearningComponent
from ..models.metadata_file import MetadataFromFile
from ..models.physics_based_component import PhysicsBasedComponent

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


def add_model_and_components(
    metadata_filename: str,
    models: list[HybridModel],
    physics_based_components: list[PhysicsBasedComponent],
    machine_learning_components: list[MachineLearningComponent],
) -> None:
    metadata_filepath = os.path.join(METADATA_DIR_PATH, metadata_filename)
    raw_data = read_yaml(metadata_filepath)
    metadata = MetadataFromFile(**raw_data)

    physics_based_component_ids = []
    for p in metadata.physics_based_components:
        component_id = len(physics_based_components)
        component_short_name = generate_short_name(p.name)
        physics_based_component_ids.append(component_id)
        physics_based_component = PhysicsBasedComponent(
            **p.dict(),
            short_name=component_short_name,
            id=component_id,
        )
        physics_based_components.append(physics_based_component)

    machine_learning_component_ids = []
    for m in metadata.machine_learning_components:
        component_id = len(machine_learning_components)
        component_short_name = generate_short_name(m.name)
        machine_learning_component_ids.append(component_id)
        machine_learning_component = MachineLearningComponent(
            **m.dict(),
            short_name=component_short_name,
            id=component_id,
        )
        machine_learning_components.append(machine_learning_component)

    model_id = len(models)
    model_short_name = metadata_filename.split(".")[0]
    model = HybridModel(
        **metadata.hybrid_model.dict(),
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
machine_learning_components = []


# from datetime import date
# models = [
#     HybridModel(
#         id=0,
#         contributors=["Smith, John"],
#         created=date(2024, 1, 1),
#         description="A simple model.",
#         keywords=["simple", "example"],
#         license="GPL-3.0",
#         name="HybridModel 1",
#         url="https://github.com/example/model1",
#         short_name="model1",
#         ml_process="",
#         host_physics="",
#         latent_variable="",
#         compatible_machine_learning_component_ids=[0, 1],
#         compatible_physical_based_component_ids=[0],
#     ),
#     HybridModel(
#         id=1,
#         contributors=[],
#         created=date(2024, 2, 1),
#         description="",
#         keywords=[],
#         license="",
#         name="HybridModel 2",
#         url="",
#         short_name="model2",
#         ml_process="",
#         host_physics="",
#         latent_variable="",
#         compatible_machine_learning_component_ids=[],
#         compatible_physical_based_component_ids=[],
#     ),
#     HybridModel(
#         id=2,
#         contributors=[],
#         created=date(2024, 3, 1),
#         description="",
#         keywords=[],
#         license="",
#         name="HybridModel 3",
#         url="",
#         short_name="model3",
#         ml_process="",
#         host_physics="",
#         latent_variable="",
#         compatible_machine_learning_component_ids=[],
#         compatible_physical_based_component_ids=[],
#     ),
# ]

metadata_loaded = False


def load_metadata():
    global models, model_summaries, physics_based_components, machine_learning_components, metadata_loaded

    models, physics_based_components, machine_learning_components = load_models_and_components()

    model_summaries = [
        HybridModelSummary(
            short_name=model.short_name,
            id=model.id,
            created=model.created,
            description=model.description,
            keywords=model.keywords,
            name=model.name,
        )
        for model in models
    ]

    metadata_loaded = True


async def get_models() -> list[HybridModelSummary]:
    if not metadata_loaded:
        load_metadata()

    return model_summaries


async def get_model(model_id: int) -> HybridModel:
    if not metadata_loaded:
        load_metadata()

    try:
        return models[model_id]

    except IndexError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")


async def get_models_short_names() -> list[str]:
    return [model.short_name for model in models]
