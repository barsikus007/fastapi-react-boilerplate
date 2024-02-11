import secrets
from pathlib import Path

from pydantic import AnyHttpUrl, EmailStr, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str

    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    FIRST_SUPERUSER_NAME: str
    FIRST_SUPERUSER_EMAIL: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")  # pylint-pydantic
    def assemble_cors_origins(cls, v: str | list[str]) -> str | list[str]:  # pylint: disable=no-self-argument
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, str | list):
            return v
        raise ValueError(v)

    POOL_SIZE: int = 32
    MAX_OVERFLOW: int = 64
    POSTGRES_PASSWORD: str = "TODO_CHANGE"
    POSTGRES_USER: str = "postgres"
    POSTGRES_HOST: str = "postgres-dev"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = POSTGRES_USER
    DATABASE_URL: PostgresDsn = PostgresDsn(
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

    model_config = SettingsConfigDict(case_sensitive=True, env_file=Path("../.env"))


settings = Settings()  # type: ignore
