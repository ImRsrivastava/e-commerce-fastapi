from pydantic_settings import BaseSettings

class Settings (BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    ALEMBIC_DATABASE_URL: str
    DATABASE_ECHO: bool
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_TOKE_URL: str

    PROJECT_AUTHOR: str | None = None

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()