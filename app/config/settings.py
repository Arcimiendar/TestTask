from functools import lru_cache

from pydantic import (
    BaseSettings,
    PostgresDsn
)


class Settings(BaseSettings):
    """
    all variable will be taken from env, else default will be used
    """
    db_uri: PostgresDsn = 'postgresql://calc:calc@postgres:5432/calc'


@lru_cache  # to parse settings once
def get_settings() -> Settings:
    """
    :return: application settings
    """
    return Settings()
