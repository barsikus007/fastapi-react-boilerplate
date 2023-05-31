import secrets

from pydantic import PostgresDsn, BaseSettings, EmailStr, AnyHttpUrl, validator


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

    @validator("BACKEND_CORS_ORIGINS", pre=True)  # pylint-pydantic
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
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = POSTGRES_USER  # PostgresDsn can't be casted to PostgresDsn lol
    DATABASE_URL: PostgresDsn = PostgresDsn(  # type: ignore
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}", scheme="postgresql+asyncpg")

    class Config:
        case_sensitive = True
        env_file = "../.env"


settings = Settings()  # type: ignore
