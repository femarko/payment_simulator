import os
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
from typing import (
    Annotated,
    Optional,
)


BASE_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = BASE_DIR / ".env.prod" if os.getenv("MODE") == "prod" else BASE_DIR / ".env.local"


def parse_comma_separated_hosts(value: str | list[str]) -> list[str]:
    if isinstance(value, list):
        return [host.strip() for host in value if isinstance(host, str) and host.strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [host.strip() for host in value.split(",") if host.strip()]
    return value

def parse_secure_proxy_ssl_header(value: str) -> tuple[str, ...]:
    return tuple(value.split(","))


class Settings(BaseSettings):
    debug: bool
    secret_key: str
    session_cookie_secure: Optional[bool] = None
    csrf_cookie_secure: Optional[bool] = None
    db_host: Optional[str] = None
    db_port: Optional[str] = None
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    secure_proxy_ssl_header: Optional[
        Annotated[
            tuple[str, ...],
            NoDecode,
            BeforeValidator(parse_secure_proxy_ssl_header),
        ]
    ] = None
    base_dir: Path = BASE_DIR
    allowed_hosts: Annotated[
        list[str],
        NoDecode,
        BeforeValidator(parse_comma_separated_hosts), 
    ] = Field(default_factory=list)


    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )



@lru_cache
def get_settings():
    return Settings()
