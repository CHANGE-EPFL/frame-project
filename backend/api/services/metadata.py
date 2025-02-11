"""This module contains functions to retrieve metadata about models.

Mock data for testing.
"""

import os
from typing import Any, Callable, TypeVar

import yaml
from fastapi import HTTPException

from ..models.common_metadata import CommonMetadata
from ..models.component import ComponentReference
from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..models.machine_learning_component import MachineLearningComponent, MachineLearningComponentSummary
from ..models.metadata_file import MetadataFromFile
from ..models.physics_based_component import PhysicsBasedComponent, PhysicsBasedComponentSummary

METADATA_DIR_PATH = os.path.join(os.path.dirname(__file__), "..", "metadata_files")
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


def format_contributors(contributors: list[str]) -> list[str]:
    """Format contributors to title case. If a comma is found, split the string and exchange the first and last name."""
    formatted_contributors = []
    for contributor in contributors:
        if "," in contributor:
            last_name, first_name = contributor.split(", ")
            contributor = f"{first_name} {last_name}"

        formatted_contributors.append(contributor.title())

    return formatted_contributors


def format_keywords(keywords: list[str]) -> list[str]:
    """Format keywords to lowercase."""
    return [keyword.lower() for keyword in keywords]


T = TypeVar("T", PhysicsBasedComponent, MachineLearningComponent)


def add_components(
    metadata: MetadataFromFile,
    components: dict[str, T],
    ComponentType: type[T],
) -> list[str]:
    if ComponentType == PhysicsBasedComponent:
        component_type_name = "physics_based_components"
    else:
        component_type_name = "machine_learning_components"

    ids = []

    for component_from_file in getattr(metadata, component_type_name):
        component_id = component_from_file.id
        ids.append(component_id)
        if isinstance(component_from_file, ComponentReference):
            continue

        if component_id in components:
            raise ValueError(f'Duplicate {ComponentType.__name__} ID "{component_id}"')
        component = ComponentType(
            **component_from_file.model_dump(),
        )
        component.contributors = format_contributors(component.contributors)
        component.keywords = format_keywords(component.keywords)
        components[component_id] = component

        for field in CommonMetadata.model_fields.keys():
            if not getattr(component, field):  # empty or None
                setattr(component, field, getattr(metadata.hybrid_model, field))

    return ids


def add_model_and_components(
    metadata_filename: str,
    models: dict[str, HybridModel],
    physics_based_components: dict[str, PhysicsBasedComponent],
    machine_learning_components: dict[str, MachineLearningComponent],
) -> None:
    metadata_filepath = os.path.join(METADATA_DIR_PATH, metadata_filename)
    raw_data = read_yaml(metadata_filepath)
    metadata = MetadataFromFile(**raw_data)
    metadata.hybrid_model.contributors = format_contributors(metadata.hybrid_model.contributors)
    metadata.hybrid_model.keywords = format_keywords(metadata.hybrid_model.keywords)

    physics_based_component_ids = add_components(metadata, physics_based_components, PhysicsBasedComponent)
    machine_learning_component_ids = add_components(metadata, machine_learning_components, MachineLearningComponent)

    model_id = metadata_filename.split(".")[0]
    model = HybridModel(
        **metadata.hybrid_model.model_dump(),
        id=model_id,
        compatible_physics_based_component_ids=physics_based_component_ids,
        compatible_machine_learning_component_ids=machine_learning_component_ids,
        data=metadata.data,
    )
    models[model_id] = model


def load_models_and_components() -> (
    tuple[dict[str, HybridModel], dict[str, PhysicsBasedComponent], dict[str, MachineLearningComponent]]
):
    """Load metadata for all models and components.

    Raises:
    """

    models = {}
    physics_based_components = {}
    machine_learning_components = {}

    for metadata_filename in get_all_metadata_filenames():
        add_model_and_components(
            metadata_filename,
            models,
            physics_based_components,
            machine_learning_components,
        )

    return models, physics_based_components, machine_learning_components


def check_non_duplicated_component_ids(
    physics_based_components: dict[str, PhysicsBasedComponent],
    machine_learning_components: dict[str, MachineLearningComponent],
) -> None:
    """Check if component IDs are duplicated between physics-based and machine-learning components.

    Raises:
        ValueError: If some component IDs are duplicated.
    """

    physics_based_component_ids = list(physics_based_components.keys())
    machine_learning_component_ids = list(machine_learning_components.keys())
    intersection = set(physics_based_component_ids) & set(machine_learning_component_ids)

    if intersection:
        raise ValueError(
            f"Some component IDs are duplicated between physics-based and machine-learning components: {intersection}"
        )


def check_component_references(
    models: dict[str, HybridModel],
    physics_based_components: dict[str, PhysicsBasedComponent],
    machine_learning_components: dict[str, MachineLearningComponent],
) -> None:
    """Check that component references in models are valid.

    Raises:
        ValueError: If a component ID is not found in the corresponding components dictionary.
    """

    for model in models.values():
        for component_type, components in [
            ("physics_based", physics_based_components),
            ("machine_learning", machine_learning_components),
        ]:
            for component_id in getattr(model, f"compatible_{component_type}_component_ids"):
                if component_id not in components:
                    raise ValueError(f'{component_type} component ID "{component_id}" does not exist.')


def get_model_keywords(
    models: dict[str, HybridModel],
    physics_based_components: dict[str, PhysicsBasedComponent],
    machine_learning_components: dict[str, MachineLearningComponent],
) -> dict[str, set[str]]:
    """Get a dictionary of model IDs and their keywords."""

    model_keywords = {}

    for model_id, model in models.items():
        s = set(model.keywords)
        s.add(model_id)
        s.update(model.name.lower().split())
        for contributor in model.contributors:
            s.update(contributor.lower().split())

        for component_type, components in [
            ("physics_based", physics_based_components),
            ("machine_learning", machine_learning_components),
        ]:
            for component_id in getattr(model, f"compatible_{component_type}_component_ids"):
                component = components[component_id]
                for keyword in component.keywords:
                    s.update(keyword.split(" "))

        model_keywords[model_id] = s

    return model_keywords


models: dict[str, HybridModel] = {}
model_summaries: dict[str, HybridModelSummary] = {}
model_keywords: dict[str, set[str]] = {}
physics_based_components: dict[str, PhysicsBasedComponent] = {}
physics_based_components_summaries: dict[str, PhysicsBasedComponentSummary] = {}
machine_learning_components: dict[str, MachineLearningComponent] = {}
machine_learning_components_summaries: dict[str, MachineLearningComponentSummary] = {}
metadata_loaded = False


def _load_metadata():
    """Load models and components metadata in module scope."""
    global models
    global model_summaries
    global model_keywords
    global physics_based_components
    global physics_based_components_summaries
    global machine_learning_components
    global machine_learning_components_summaries, metadata_loaded

    models, physics_based_components, machine_learning_components = load_models_and_components()
    check_non_duplicated_component_ids(physics_based_components, machine_learning_components)
    check_component_references(models, physics_based_components, machine_learning_components)

    model_summaries = {model_id: HybridModelSummary(**model.model_dump()) for model_id, model in models.items()}
    model_keywords = get_model_keywords(models, physics_based_components, machine_learning_components)
    physics_based_components_summaries = {
        component_id: PhysicsBasedComponentSummary(**component.model_dump())
        for component_id, component in physics_based_components.items()
    }
    machine_learning_components_summaries = {
        component_id: MachineLearningComponentSummary(**component.model_dump())
        for component_id, component in machine_learning_components.items()
    }

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
    return list(model_summaries.values())


@load_metadata
async def get_filtered_hybrid_models(query: str) -> list[HybridModelSummary]:
    query_keywords = query.lower().split()
    model_ids = []

    for model_id, keywords in model_keywords.items():
        full_query_match = True

        for query_keyword in query_keywords:
            match = any(keyword.startswith(query_keyword) for keyword in keywords)  # allow partial match
            if not match:  # all query keywords must match
                full_query_match = False
                break

        if full_query_match:
            model_ids.append(model_id)

    return [model_summaries[model_id] for model_id in model_ids]


@load_metadata
async def get_hybrid_model(model_id: str) -> HybridModel:
    try:
        return models[model_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")


@load_metadata
async def get_hybrid_model_ids() -> list[str]:
    return list(models.keys())


@load_metadata
async def get_physics_based_component_models(component_id: str) -> list[HybridModelSummary]:
    try:
        component = physics_based_components[component_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="PhysicsBasedComponent not found.")

    return [
        model_summaries[model_id]
        for model_id, model in models.items()
        if component.id in model.compatible_physics_based_component_ids
    ]


@load_metadata
async def get_machine_learning_component_models(component_id: str) -> list[HybridModelSummary]:
    try:
        component = machine_learning_components[component_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="MachineLearningComponent not found.")

    return [
        model_summaries[model_id]
        for model_id, model in models.items()
        if component.id in model.compatible_machine_learning_component_ids
    ]


@load_metadata
async def get_model_physics_based_components(model_id: str) -> list[PhysicsBasedComponentSummary]:
    try:
        model = models[model_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")

    return [
        physics_based_components_summaries[component_id]
        for component_id in model.compatible_physics_based_component_ids
    ]


@load_metadata
async def get_physics_based_component(component_id: str) -> PhysicsBasedComponent:
    try:
        return physics_based_components[component_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="PhysicsBasedComponent not found.")


@load_metadata
async def get_model_machine_learning_components(model_id: str) -> list[MachineLearningComponentSummary]:
    try:
        model = models[model_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="HybridModel not found.")

    return [
        machine_learning_components_summaries[component_id]
        for component_id in model.compatible_machine_learning_component_ids
    ]


@load_metadata
async def get_machine_learning_component(component_id: str) -> MachineLearningComponent:
    try:
        return machine_learning_components[component_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="MachineLearningComponent not found.")


@load_metadata
async def get_component_ids() -> list[str]:
    physics_based_component_ids = list(physics_based_components.keys())
    machine_learning_component_ids = list(machine_learning_components.keys())
    return physics_based_component_ids + machine_learning_component_ids


@load_metadata
async def get_physics_based_component_ids() -> list[str]:
    return list(physics_based_components.keys())


@load_metadata
async def get_machine_learning_component_ids() -> list[str]:
    return list(machine_learning_components.keys())
