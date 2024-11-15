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
    model = metadata.load_model(metadata_filename, id=0)
    assert isinstance(model, metadata.Model)
