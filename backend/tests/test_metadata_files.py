import pytest

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
    raw_data = metadata.load_metadata_yaml(metadata_path)
    metadata.add_model_and_components(
        raw_data,
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
