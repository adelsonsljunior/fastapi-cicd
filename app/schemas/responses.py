from pydantic import BaseModel
from typing import Generic, TypeVar
from uuid import UUID


class IdResponse(BaseModel):
    id: UUID


class ErrorResponse(BaseModel):
    message: str


T = TypeVar("T")


class PaginationResponse(BaseModel, Generic[T]):
    data: list[T]
    items_per_page: int
    total_items: int
    current_page: int
    total_pages: int
