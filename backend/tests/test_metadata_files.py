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
    models = []
    physics_based_components = []
    machine_learning_components = []
    metadata.add_model_and_components(
        metadata_filename,
        models,
        physics_based_components,
        machine_learning_components,
    )
    assert isinstance(models[0], metadata.HybridModel)
    assert isinstance(physics_based_components[0], metadata.PhysicsBasedComponent)
    for component in machine_learning_components:
        assert isinstance(component, metadata.MachineLearningComponent)


@pytest.mark.asyncio
async def test_unique_short_names() -> None:
    short_names = await metadata.get_models_short_names()
    assert len(short_names) == len(set(short_names))
