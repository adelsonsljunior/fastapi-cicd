from typing import Literal

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Obrigatória. O tipo PostgresDsn valida esquema/host no boot (fail fast).
    DB_URL: PostgresDsn

    # Modo da API. "prod" desabilita a documentação (Swagger/ReDoc/OpenAPI).
    API_MODE: Literal["dev", "prod"] = "dev"

    # Porta de escuta. Coagida para int e validada em 1-65535 no boot (fail fast).
    PORT: int = Field(8000, ge=1, le=65535)


settings = Settings()
