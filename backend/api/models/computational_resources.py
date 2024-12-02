from pydantic import BaseModel, Extra


class ComputationalResources(BaseModel, extra=Extra.forbid):
    """Computational resources need for a hybrid model or component."""

    cpu: str
    gpu: str | None = None
    memory: str
    storage: str
    software: list[str]
    operating_system: str | None = None
    compute_time: str
