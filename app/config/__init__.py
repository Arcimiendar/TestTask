from functools import lru_cache

from pydantic import (
    BaseSettings,
    AnyUrl
)


class AnyUrlWithoutHost(AnyUrl):
    host_required = False


class Settings(BaseSettings):
    db_uri: AnyUrlWithoutHost = 'postgresql://calc:calc@postgres:5432/calc'


@lru_cache
def get_settings() -> Settings:
    return Settings()
