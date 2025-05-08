from fastapi.testclient import TestClient

from api.main import app
from api.services.metadata import (
    get_hybrid_model_ids,
    get_hybrid_model_versions,
    get_machine_learning_component_ids,
    get_physics_based_component_ids,
)

client = TestClient(app)

test_model_id = get_hybrid_model_ids()[0]
test_model_version = get_hybrid_model_versions(test_model_id)[-1]
test_physics_based_component_id = get_physics_based_component_ids()[0]
test_machine_learning_component_id = get_machine_learning_component_ids()[0]


class TestGetHybridModels:
    """Test the get_hybrid_models endpoint."""

    def test_no_query(self) -> None:
        """Test without filtering by query."""

        response = client.get("hybrid_models/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_with_query(self) -> None:
        """Test with filtering by query."""

        response = client.get("hybrid_models/", params={"query": "hybrid"})
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


class TestGetHybridModel:
    """Test the get_hybrid_model endpoint."""

    def test_invalid_id(self) -> None:
        """Test invalid model_id."""
        response = client.get("hybrid_models/invalid_id")
        assert response.status_code == 404

    def test_no_version(self) -> None:
        """Test with no model_version."""
        response = client.get(f"hybrid_models/{test_model_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["latest"] is True

    def test_invalid_version(self) -> None:
        """Test invalid model_version."""
        response = client.get(f"hybrid_models/{test_model_id}", params={"model_version": "invalid_version"})
        assert response.status_code == 404

    def test_valid_version(self) -> None:
        """Test valid model_version."""
        response = client.get(f"hybrid_models/{test_model_id}", params={"model_version": test_model_version})
        assert response.status_code == 200
        data = response.json()
        assert data["version"] == test_model_version


def test_get_hybrid_model_ids() -> None:
    """Test the get_hybrid_model_ids endpoint."""

    response = client.get("hybrid_models/ids/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_hybrid_model_versions() -> None:
    """Test the get_hybrid_model_versions endpoint."""

    response = client.get(f"hybrid_models/versions/{test_model_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert test_model_version in data


def test_get_physics_based_component_models() -> None:
    """Test the get_physics_based_component_models endpoint."""

    response = client.get(f"hybrid_models/physics_based/{test_physics_based_component_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_machine_learning_component_models() -> None:
    """Test the get_machine_learning_component_models endpoint."""

    response = client.get(f"hybrid_models/machine_learning/{test_machine_learning_component_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
