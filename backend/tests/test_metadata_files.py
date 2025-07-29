import pytest
import yaml.scanner
from pydantic import ValidationError

from api.services import metadata

metadata_paths = metadata.get_all_metadata_paths()


@pytest.mark.parametrize("metadata_path", metadata_paths)
def test_read_yaml(metadata_path: str) -> None:
    raw_data = metadata.load_metadata_yaml(metadata_path)
    assert isinstance(raw_data, dict)


@pytest.mark.parametrize("metadata_path", metadata_paths)
def test_schema(metadata_path: str) -> None:
    models = {}
    physics_based_components = {}
    machine_learning_components = {}

    try:
        raw_data = metadata.load_metadata_yaml(metadata_path)
    except yaml.scanner.ScannerError as e:
        raise RuntimeError(f"Failed to load metadata file {metadata_path}. Ensure that the file is valid YAML.") from e

    try:
        metadata.add_model_and_components(
            raw_data,
            models,
            physics_based_components,
            machine_learning_components,
        )
    except ValidationError as e:
        message = f"Validation error in metadata file {metadata_path}."
        for error in e.errors():
            message += f"\n- {error['loc']}: {error['msg']}"
        raise RuntimeError(message) from e

    assert isinstance(next(iter(next(iter(models.values())).values())), metadata.HybridModel)
    for component_family in physics_based_components.values():
        for component in component_family.values():
            assert isinstance(component, metadata.PhysicsBasedComponent)
    for component_family in machine_learning_components.values():
        for component in component_family.values():
            assert isinstance(component, metadata.MachineLearningComponent)


def test_unique_ids() -> None:
    """Test that the call runs without raising an exception."""
    try:
        metadata.get_hybrid_model_ids()
        metadata.get_component_ids()

    except yaml.scanner.ScannerError as e:
        raise RuntimeError("Failed to load metadata files. Ensure that all metadata files are valid YAML.") from e

    except ValidationError as e:
        raise RuntimeError(
            "Validation error in metadata files. Ensure that all metadata files follow the expected schema."
        ) from e
