"""This module contains functions to retrieve metadata about models.

Mock data for testing.
"""

import os
from typing import Any, Callable, TypeVar

import requests
import yaml
from fastapi import HTTPException
from packaging.version import InvalidVersion, Version

from ..models.common_metadata import CommonMetadata
from ..models.component import ComponentReference
from ..models.hybrid_model import HybridModel, HybridModelSummary
from ..models.machine_learning_component import MachineLearningComponent, MachineLearningComponentSummary
from ..models.metadata_file import MetadataFromFile
from ..models.physics_based_component import PhysicsBasedComponent, PhysicsBasedComponentSummary

METADATA_DIR_PATH = os.path.relpath(os.path.join(os.path.dirname(__file__), "..", "metadata_files"))
METADATA_TEMPLATE_FILENAME = "template.yaml"
EXTERNAL_METADATA_FILENAME: str = "external_metadata_files.yaml"
DEFAULT_VERSION = "none"


def read_yaml(path: str) -> Any:
    with open(path) as f:
        return yaml.safe_load(f.read())


def get_all_local_metadata_filenames() -> list[str]:
    return [
        filename
        for filename in os.listdir(METADATA_DIR_PATH)
        if filename != METADATA_TEMPLATE_FILENAME
        and filename != EXTERNAL_METADATA_FILENAME
        and filename.endswith(".yaml")
    ]


def get_all_external_metadata_urls() -> list[str]:
    external_metadata_filepath = os.path.join(METADATA_DIR_PATH, EXTERNAL_METADATA_FILENAME)
    return read_yaml(external_metadata_filepath)


def get_all_metadata_paths() -> list[str]:
    local_metadata_filepaths = [
        os.path.join(METADATA_DIR_PATH, filename) for filename in get_all_local_metadata_filenames()
    ]
    return local_metadata_filepaths + get_all_external_metadata_urls()


def load_metadata_yaml(metadata_path: str) -> dict[str, Any]:
    if metadata_path.startswith("http"):
        response = requests.get(metadata_path)
        response.raise_for_status()
        return yaml.safe_load(response.text)

    return read_yaml(metadata_path)


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


C = TypeVar("C", PhysicsBasedComponent, MachineLearningComponent)
U = TypeVar("U", HybridModel, PhysicsBasedComponent, MachineLearningComponent)


def add_components(
    metadata: MetadataFromFile,
    components: dict[str, dict[str, C]],
    ComponentType: type[C],
) -> list[str]:
    if ComponentType == PhysicsBasedComponent:
        component_type_name = "physics_based"
    else:
        component_type_name = "machine_learning"

    ids = []

    for component_from_file in getattr(metadata, f"{component_type_name}_components"):
        component_id = component_from_file.id
        ids.append(component_id)
        if isinstance(component_from_file, ComponentReference):
            continue

        component = ComponentType(
            **component_from_file.model_dump(),
        )
        component.contributors = format_contributors(component.contributors)
        component.keywords = format_keywords(component.keywords)

        if component_id not in components:
            components[component_id] = {}

        for field in CommonMetadata.model_fields.keys():
            if not getattr(component, field):  # empty or None
                setattr(component, field, getattr(metadata.hybrid_model, field))

        component.version = component.version or DEFAULT_VERSION
        component_version = component.version
        if component_version in components[component_id]:
            raise ValueError(
                f'Duplicate {ComponentType.__name__} version "{component_version}" for ID "{component_id}"'
            )

        components[component_id][component_version] = component

    return ids


def add_model_and_components(
    raw_data: dict[str, Any],
    models: dict[str, dict[str, HybridModel]],
    physics_based_components: dict[str, dict[str, PhysicsBasedComponent]],
    machine_learning_components: dict[str, dict[str, MachineLearningComponent]],
) -> None:
    metadata = MetadataFromFile(**raw_data)
    model_id = metadata.hybrid_model.id
    metadata.hybrid_model.contributors = format_contributors(metadata.hybrid_model.contributors)
    metadata.hybrid_model.keywords = format_keywords(metadata.hybrid_model.keywords)

    physics_based_component_ids = add_components(metadata, physics_based_components, PhysicsBasedComponent)
    machine_learning_component_ids = add_components(metadata, machine_learning_components, MachineLearningComponent)

    model = HybridModel(
        **metadata.hybrid_model.model_dump(),
        compatible_physics_based_component_ids=physics_based_component_ids,
        compatible_machine_learning_component_ids=machine_learning_component_ids,
        data=metadata.data,
    )

    if model_id not in models:
        models[model_id] = {}

    model.version = model.version or DEFAULT_VERSION
    model_version = model.version
    if model_version in models[model_id]:
        raise ValueError(f'Duplicate model version "{model_version}" for model ID "{model_id}"')

    models[model_id][model_version] = model


def sort_by_version(units: dict[str, dict[str, U]]) -> dict[str, dict[str, U]]:
    units = units.copy()

    for unit_id in units.keys():
        unit_family = units[unit_id]
        try:
            unit_family = dict(sorted(unit_family.items(), key=lambda item: Version(item[0]), reverse=True))
        except InvalidVersion:
            unit_family = dict(sorted(unit_family.items(), key=lambda item: item[0], reverse=True))
        units[unit_id] = unit_family

        latest_model = next(iter(unit_family.values()))
        latest_model.latest = True

    return units


def load_models_and_components() -> tuple[
    dict[str, dict[str, HybridModel]],
    dict[str, dict[str, PhysicsBasedComponent]],
    dict[str, dict[str, MachineLearningComponent]],
]:
    """Load metadata for all models and components.

    Raises:
    """

    models = {}
    physics_based_components = {}
    machine_learning_components = {}

    for metadata_path in get_all_metadata_paths():
        raw_data = load_metadata_yaml(metadata_path)

        add_model_and_components(
            raw_data,
            models,
            physics_based_components,
            machine_learning_components,
        )

    models = sort_by_version(models)
    physics_based_components = sort_by_version(physics_based_components)
    machine_learning_components = sort_by_version(machine_learning_components)

    return models, physics_based_components, machine_learning_components


def check_non_duplicated_component_ids(
    physics_based_components: dict[str, dict[str, PhysicsBasedComponent]],
    machine_learning_components: dict[str, dict[str, MachineLearningComponent]],
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
    models: dict[str, dict[str, HybridModel]],
    physics_based_components: dict[str, dict[str, PhysicsBasedComponent]],
    machine_learning_components: dict[str, dict[str, MachineLearningComponent]],
) -> None:
    """Check that component references in models are valid.

    Raises:
        ValueError: If a component ID is not found in the corresponding components dictionary.
    """

    for model_family in models.values():
        for model in model_family.values():
            for component_type, components in [
                ("physics_based", physics_based_components),
                ("machine_learning", machine_learning_components),
            ]:
                for component_id in getattr(model, f"compatible_{component_type}_component_ids"):
                    if component_id not in components:
                        raise ValueError(f'{component_type} component ID "{component_id}" does not exist.')


def get_model_keywords(
    models: dict[str, dict[str, HybridModel]],
    physics_based_components: dict[str, dict[str, PhysicsBasedComponent]],
    machine_learning_components: dict[str, dict[str, MachineLearningComponent]],
) -> dict[str, set[str]]:
    """Get a dictionary of model IDs and their keywords."""

    model_keywords = {}

    for model_id, model_family in models.items():
        s = set()

        for model in model_family.values():
            s.update(model.keywords)
            s.add(model_id)
            s.update(model.name.lower().split())

            for contributor in model.contributors:
                s.update(contributor.lower().split())

            for component_type, components in [
                ("physics_based", physics_based_components),
                ("machine_learning", machine_learning_components),
            ]:
                for component_id in getattr(model, f"compatible_{component_type}_component_ids"):
                    component = next(iter(components[component_id].values()))
                    for keyword in component.keywords:
                        s.update(keyword.split(" "))

        model_keywords[model_id] = s

    return model_keywords


models: dict[str, dict[str, HybridModel]] = {}  # First key is model ID, second key is version
model_summaries: dict[str, HybridModelSummary] = {}  # Key is model ID
model_keywords: dict[str, set[str]] = {}
physics_based_components: dict[str, dict[str, PhysicsBasedComponent]] = {}
physics_based_components_summaries: dict[str, PhysicsBasedComponentSummary] = {}
machine_learning_components: dict[str, dict[str, MachineLearningComponent]] = {}
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
    global machine_learning_components_summaries
    global metadata_loaded

    models, physics_based_components, machine_learning_components = load_models_and_components()
    check_non_duplicated_component_ids(physics_based_components, machine_learning_components)
    check_component_references(models, physics_based_components, machine_learning_components)

    # Summary of latest version of each model
    model_summaries = {
        model_id: HybridModelSummary(**next(iter(model_family.values())).model_dump())
        for model_id, model_family in models.items()
    }
    model_keywords = get_model_keywords(models, physics_based_components, machine_learning_components)
    physics_based_components_summaries = {
        component_id: PhysicsBasedComponentSummary(**next(iter(component_family.values())).model_dump())
        for component_id, component_family in physics_based_components.items()
    }
    machine_learning_components_summaries = {
        component_id: MachineLearningComponentSummary(**next(iter(component_family.values())).model_dump())
        for component_id, component_family in machine_learning_components.items()
    }

    metadata_loaded = True


def load_metadata(func: Callable):
    """Decorator to trigger loading metadata."""

    def wrapped(*args, **kwargs):
        if not metadata_loaded:
            _load_metadata()

        return func(*args, **kwargs)

    return wrapped


@load_metadata
def get_hybrid_models() -> list[HybridModelSummary]:
    return list(model_summaries.values())


@load_metadata
def get_filtered_hybrid_models(query: str) -> list[HybridModelSummary]:
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


def get_unit(unit_id: str, unit_version: str | None, units: dict[str, dict[str, U]], UnitType: type[U]) -> U:
    if unit_id not in units:
        raise HTTPException(status_code=404, detail=f"{UnitType.__name__} ID not found.")

    if unit_version is None:
        unit_version = next(iter(units[unit_id].keys()))

    elif unit_version not in units[unit_id]:
        raise HTTPException(status_code=404, detail=f"{UnitType.__name__} version not found.")

    return units[unit_id][unit_version]


@load_metadata
def get_hybrid_model(model_id: str, model_version: str | None) -> HybridModel:
    return get_unit(model_id, model_version, models, HybridModel)


@load_metadata
def get_hybrid_model_ids() -> list[str]:
    return list(models.keys())


@load_metadata
def get_hybrid_model_versions(model_id: str) -> list[str]:
    if model_id not in models:
        raise HTTPException(status_code=404, detail="HybridModel ID not found.")

    return list(models[model_id].keys())


def get_component_models(
    component_id: str,
    component_version: str | None,
    components: dict[str, dict[str, C]],
    ComponentType: type[C],
) -> list[HybridModelSummary]:
    if ComponentType == PhysicsBasedComponent:
        component_type_name = "physics_based"
    else:
        component_type_name = "machine_learning"

    component = get_unit(component_id, component_version, components, ComponentType)

    return [
        model_summaries[model_id]
        for model_id, model in models.items()
        if component.id in model.get(f"compatible_{component_type_name}_component_ids", {})
    ]


@load_metadata
def get_physics_based_component_models(component_id: str, component_version: str | None) -> list[HybridModelSummary]:
    return get_component_models(component_id, component_version, physics_based_components, PhysicsBasedComponent)


@load_metadata
def get_machine_learning_component_models(component_id: str, component_version: str | None) -> list[HybridModelSummary]:
    return get_component_models(component_id, component_version, machine_learning_components, MachineLearningComponent)


@load_metadata
def get_model_physics_based_components(model_id: str, model_version: str | None) -> list[PhysicsBasedComponentSummary]:
    model = get_hybrid_model(model_id, model_version)

    return [
        physics_based_components_summaries[component_id]
        for component_id in model.compatible_physics_based_component_ids
    ]


@load_metadata
def get_physics_based_component(component_id: str, component_version: str | None) -> PhysicsBasedComponent:
    return get_unit(component_id, component_version, physics_based_components, PhysicsBasedComponent)


@load_metadata
def get_model_machine_learning_components(
    model_id: str, model_version: str | None
) -> list[MachineLearningComponentSummary]:
    model = get_hybrid_model(model_id, model_version)

    return [
        machine_learning_components_summaries[component_id]
        for component_id in model.compatible_machine_learning_component_ids
    ]


@load_metadata
def get_machine_learning_component(component_id: str, component_version: str | None) -> MachineLearningComponent:
    return get_unit(component_id, component_version, machine_learning_components, MachineLearningComponent)


@load_metadata
def get_component_ids() -> list[str]:
    physics_based_component_ids = list(physics_based_components.keys())
    machine_learning_component_ids = list(machine_learning_components.keys())
    return physics_based_component_ids + machine_learning_component_ids


@load_metadata
def get_physics_based_component_ids() -> list[str]:
    return list(physics_based_components.keys())


@load_metadata
def get_machine_learning_component_ids() -> list[str]:
    return list(machine_learning_components.keys())


@load_metadata
def get_physics_based_component_versions(component_id: str) -> list[str]:
    if component_id not in physics_based_components:
        raise HTTPException(status_code=404, detail="PhysicsBasedComponent ID not found.")

    return list(physics_based_components[component_id].keys())


@load_metadata
def get_machine_learning_component_versions(component_id: str) -> list[str]:
    if component_id not in machine_learning_components:
        raise HTTPException(status_code=404, detail="MachineLearningComponent ID not found.")

    return list(machine_learning_components[component_id].keys())
