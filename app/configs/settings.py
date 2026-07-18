from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Obrigatória. O tipo PostgresDsn valida esquema/host no boot (fail fast).
    DB_URL: PostgresDsn


settings = Settings()
