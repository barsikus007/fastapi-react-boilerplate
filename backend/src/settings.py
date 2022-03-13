from os import getenv
import secrets

from pydantic import SecretStr, PostgresDsn, BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = getenv('DEBUG')
    API_V1_STR: str = '/api/v1'
    # PROJECT_NAME: str = os.environ['PROJECT_NAME']
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    DATABASE_USER: str = getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = getenv('DATABASE_PASSWORD')
    DATABASE_HOST: str = getenv('DATABASE_HOST')
    DATABASE_PORT: int | str = getenv('DATABASE_PORT')
    DATABASE_NAME: str = getenv('DATABASE_NAME')
    DATABASE_URL: PostgresDsn = getenv(
        'DATABASE_URL',
        f'postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
    )

    SECRET_KEY: SecretStr = secrets.token_urlsafe(32)
    class Config:
        case_sensitive = True
    #     env_file = os.path.expanduser('~/.env')

settings = Settings()
