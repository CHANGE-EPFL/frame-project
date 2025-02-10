import os

import pytest

from api.services import metadata

metadata_filenames = metadata.get_all_metadata_filenames()


@pytest.mark.parametrize("metadata_filename", metadata_filenames)
def test_read_yaml(metadata_filename: str) -> None:
    path = os.path.join(metadata.METADATA_DIR_PATH, metadata_filename)
    data = metadata.read_yaml(path)
    assert isinstance(data, dict)


@pytest.mark.parametrize("metadata_filename", metadata_filenames)
def test_schema(metadata_filename: str) -> None:
    models = {}
    physics_based_components = {}
    machine_learning_components = {}
    metadata.add_model_and_components(
        metadata_filename,
        models,
        physics_based_components,
        machine_learning_components,
    )
    assert isinstance(list(models.values())[0], metadata.HybridModel)
    for component in physics_based_components.values():
        assert isinstance(component, metadata.PhysicsBasedComponent)
    for component in machine_learning_components.values():
        assert isinstance(component, metadata.MachineLearningComponent)


@pytest.mark.asyncio
async def test_unique_ids() -> None:
    """Test that the call runs without raising an exception."""
    await metadata.get_hybrid_model_ids()
    await metadata.get_component_ids()
