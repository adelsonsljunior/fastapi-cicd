from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class PostBase(BaseModel):
    body: str = Field(
        min_length=1,
        max_length=255,
        description="O body deve ter entre 1 e 255 caracteres",
        examples=["Hey, Marceline!"],
    )


class PostCreateDto(PostBase):
    username: str = Field(
        min_length=3,
        max_length=50,
        description="O username deve ter entre 3 e 50 caracteres",
        examples=["juninhogameplays"],
    )


class PostUpdateDto(PostBase):
    pass


class PostResponseDto(PostBase):
    id: UUID = Field(
        description="Identificador único do Post (UUID)",
        examples=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
    )
    username: str = Field(
        description="Autor do Post",
        examples=["juninhogameplays"],
    )
    archived: bool = Field(
        description="Indica se o Post está arquivado",
        examples=[False],
    )
    created_at: datetime = Field(
        description="Data de criação do Post",
        examples=["2026-07-18T12:00:00"],
    )
    updated_at: datetime = Field(
        description="Data da última atualização do Post",
        examples=["2026-07-18T12:00:00"],
    )
