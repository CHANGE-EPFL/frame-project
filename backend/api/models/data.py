from datetime import date

from pydantic import BaseModel


class Data(BaseModel):
    """Data structure for input and output data."""

    name: str
    encoding_format: str
    identifier: str | None = None
    url: str | None = None
    quality: int | str | None = None
    units: str | None = None
    precision: str | None = None
    scale: float | int | None = None
    offset: float | int | None = None

    # Extent
    min_value: float | int | None = None
    max_value: float | int | None = None
    temporal_coverage: str | date | None = None
    spatial_coverage: str | None = None

    # Resolution
    spatial_resolution: str | None = None
    temporal_resolution: str | None = None


class DataIO(BaseModel):
    """Collection of input and output data for a hybrid model."""

    inputs: list[Data]
    outputs: list[Data]
