from functools import lru_cache
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str = ""
    SOME_URL: str = ""


@lru_cache
def get_config() -> Config:
    return Config()