from pydantic_settings import BaseSettings

class Settings (BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    ALEMBIC_DATABASE_URL: str
    DATABASE_ECHO: bool
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()