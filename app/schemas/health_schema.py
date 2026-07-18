from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(
        description="Estado da verificação de saúde da aplicação",
        examples=["Ok"],
    )
    message: str = Field(
        description="Detalhe sobre o resultado da verificação",
        examples=["Postgres database está on"],
    )
