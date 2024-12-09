from pydantic import BaseModel


class Cpu(BaseModel, extra="forbid"):
    """Central processing unit (CPU) metadata."""

    count: int = 1
    manufacturer: str | None = None
    model: str | None = None
    cores: int | None = None
    threads: int | None = None
    cache: str | None = None
    clock_speed: str | None = None


class Gpu(BaseModel, extra="forbid"):
    """Graphics processing unit (GPU) metadata."""

    count: int = 1
    manufacturer: str | None = None
    model: str | None = None
    memory: str | None = None
    memory_bandwidth: str | None = None
    clock_speed: str | None = None
    cuda_cores: int | None = None
    tensor_cores: int | None = None
    rt_cores: int | None = None
    ray_tracing: bool | None = None


class ComputationalResources(BaseModel, extra="forbid"):
    """Computational resources need for a hybrid model or component."""

    cpus: list[Cpu] = []
    gpus: list[Gpu] = []
    memory: str | None = None
    storage: str | None = None
    software: list[str] | None = None
    operating_system: str | None = None
    compute_time: str | None = None
