import secrets

from pydantic import PostgresDsn, BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    # PROJECT_NAME: str = os.environ["PROJECT_NAME"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 180
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    POSTGRES_PASSWORD: str = "TODO_CHANGE"
    POSTGRES_USER: str = "postgres"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = POSTGRES_USER
    DATABASE_URL: PostgresDsn = PostgresDsn(
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}", scheme="postgresql+asyncpg")

    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True
        env_file = "../.env"


settings = Settings()
