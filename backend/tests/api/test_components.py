import pytest
import yaml
from fastapi.testclient import TestClient
from pydantic import ValidationError

from api.main import app
from api.services.metadata import (
    get_hybrid_model_ids,
    get_hybrid_model_versions,
    get_machine_learning_component_ids,
    get_machine_learning_component_versions,
    get_physics_based_component_ids,
    get_physics_based_component_versions,
)

client = TestClient(app)

try:
    test_model_id = get_hybrid_model_ids()[0]
    test_model_version = get_hybrid_model_versions(test_model_id)[-1]
    test_physics_based_component_id = get_physics_based_component_ids()[0]
    test_physics_based_component_version = get_physics_based_component_versions(test_physics_based_component_id)[-1]
    test_machine_learning_component_id = get_machine_learning_component_ids()[0]
    test_machine_learning_component_version = get_machine_learning_component_versions(
        test_machine_learning_component_id
    )[-1]

except yaml.YAMLError as e:
    raise RuntimeError("Failed to load metadata files. Ensure that all metadata files are valid YAML.") from e

except ValidationError as e:
    raise RuntimeError(
        "Validation error in metadata files. Ensure that all metadata files follow the expected schema."
    ) from e


@pytest.mark.parametrize("component_type_name", ["physics_based", "machine_learning"])
class TestGetModelComponents:
    """Test the get_model_physics_based_components and get_model_machine_learning_components endpoints."""

    def test_invalid_id(self, component_type_name: str) -> None:
        """Test invalid model_id."""
        response = client.get(f"components/model_{component_type_name}/invalid_id")
        assert response.status_code == 404

    def test_no_version(self, component_type_name: str) -> None:
        """Test with no model_version."""
        response = client.get(f"components/model_{component_type_name}/{test_model_id}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_invalid_version(self, component_type_name: str) -> None:
        """Test invalid model_version."""
        response = client.get(
            f"components/model_{component_type_name}/{test_model_id}", params={"model_version": "invalid_version"}
        )
        assert response.status_code == 404

    def test_valid_version(self, component_type_name: str) -> None:
        """Test valid model_version."""
        response = client.get(
            f"components/model_{component_type_name}/{test_model_id}", params={"model_version": test_model_version}
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


@pytest.mark.parametrize("component_type_name", ["physics_based", "machine_learning"])
class TestGetComponent:
    """Test the get_physics_based_component and get_machine_learning_component endpoints."""

    @pytest.fixture
    def component_id(self, component_type_name: str) -> str:
        """Return a test component ID based on the component type."""
        if component_type_name == "physics_based":
            return test_physics_based_component_id
        else:
            return test_machine_learning_component_id

    @pytest.fixture
    def component_version(self, component_type_name: str) -> str:
        """Return a test component version based on the component type."""
        if component_type_name == "physics_based":
            return test_physics_based_component_version
        else:
            return test_machine_learning_component_version

    def test_invalid_id(self, component_type_name: str) -> None:
        """Test invalid model_id."""
        response = client.get(f"components/{component_type_name}/invalid_id")
        assert response.status_code == 404

    def test_no_version(self, component_type_name: str, component_id: str) -> None:
        """Test with no model_version."""
        response = client.get(f"components/{component_type_name}/{component_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["latest"] is True

    def test_invalid_version(self, component_type_name: str, component_id: str) -> None:
        """Test invalid model_version."""
        response = client.get(
            f"components/{component_type_name}/{component_id}", params={"component_version": "invalid_version"}
        )
        assert response.status_code == 404

    def test_valid_version(self, component_type_name: str, component_id: str, component_version: str) -> None:
        """Test valid model_version."""
        response = client.get(
            f"components/{component_type_name}/{component_id}", params={"component_version": component_version}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["version"] == component_version


@pytest.mark.parametrize("component_type_name", [None, "physics_based", "machine_learning"])
def test_get_component_ids(component_type_name: str | None) -> None:
    """Test the get_component_ids, get_physics_based_component_ids, and get_machine_learning_component_ids endpoints."""

    response = client.get(f"components/{component_type_name + '_' if component_type_name is not None else ''}ids/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.parametrize("component_type_name", ["physics_based", "machine_learning"])
def test_get_component_versions(component_type_name: str) -> None:
    """Test the get_physics_based_component_versions and get_machine_learning_component_versions endpoints."""

    component_id = (
        test_physics_based_component_id
        if component_type_name == "physics_based"
        else test_machine_learning_component_id
    )
    component_version = (
        test_physics_based_component_version
        if component_type_name == "physics_based"
        else test_machine_learning_component_version
    )

    response = client.get(f"components/{component_type_name}_versions/{component_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert component_version in data
