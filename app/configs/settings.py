from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Obrigatória. O tipo PostgresDsn valida esquema/host no boot (fail fast).
    DB_URL: PostgresDsn

    # Modo da API. "prod" desabilita a documentação (Swagger/ReDoc/OpenAPI).
    API_MODE: Literal["dev", "prod"] = "dev"


settings = Settings()
