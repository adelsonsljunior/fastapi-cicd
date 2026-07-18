from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from uuid import UUID


class IdResponse(BaseModel):
    id: UUID = Field(
        description="Identificador único do recurso criado (UUID)",
        examples=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
    )


class ErrorResponse(BaseModel):
    message: str = Field(
        description="Mensagem de erro",
        examples=[""],
    )


T = TypeVar("T")


class PaginationResponse(BaseModel, Generic[T]):
    data: list[T]
    items_per_page: int = Field(
        description="Quantidade de itens por página",
        examples=[10],
    )
    total_items: int = Field(
        description="Total de itens encontrados",
        examples=[1],
    )
    current_page: int = Field(
        description="Página atual",
        examples=[1],
    )
    total_pages: int = Field(
        description="Total de páginas disponíveis",
        examples=[1],
    )
