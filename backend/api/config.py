from functools import lru_cache

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PATH_PREFIX: str = "/api"
    REQUESTS_TIMEOUT: int = 2


@lru_cache()
def get_config():
    return Config()


config = get_config()
