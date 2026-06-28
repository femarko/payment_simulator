from pathlib import Path
from functools import lru_cache
from pydantic import (
    Field,
    BeforeValidator,
)
from pydantic_settings import (
    BaseSettings,
    NoDecode,
    SettingsConfigDict,
)
from typing import Annotated



ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


def parse_comma_separated_hosts(value: str | list[str]) -> list[str]:
    if isinstance(value, list):
        return [host.strip() for host in value if isinstance(host, str) and host.strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [host.strip() for host in value.split(",") if host.strip()]
    return value


class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str
    secret_key: str
    allowed_hosts: Annotated[
        list[str],
        NoDecode,
        BeforeValidator(parse_comma_separated_hosts), 
    ] = Field(default_factory=list)
    base_dir: Path = Field(default=Path(__file__).resolve().parent) 

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )



@lru_cache
def get_settings():
    return Settings()
