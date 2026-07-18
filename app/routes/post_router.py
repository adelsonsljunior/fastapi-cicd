from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.controllers.post_controller import PostController
from app.schemas.post_schema import PostCreateDto, PostResponseDto, PostUpdateDto
from app.schemas.responses import IdResponse, ErrorResponse, PaginationResponse

router = APIRouter(prefix="/posts", tags=["Posts"])

PostIdPath = Annotated[
    UUID,
    Path(
        description="ID do Post (UUID)",
        openapi_examples={
            "exemplo": {
                "summary": "UUID de exemplo",
                "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            },
        },
    ),
]

PageQuery = Annotated[
    int,
    Query(ge=1, description="Número da página a ser retornada (começa em 1)"),
]

LimitQuery = Annotated[
    int,
    Query(ge=1, description="Quantidade de Posts por página"),
]


@router.get(
    "",
    response_model=PaginationResponse[PostResponseDto],
    summary="Listar Posts",
    description=(
        "Retorna uma lista paginada de todos os Posts cadastrados. "
        "Use os parâmetros `page` e `limit` para navegar entre as páginas."
    ),
)
async def find_all(
    page: PageQuery = 1,
    limit: LimitQuery = 10,
    db: Session = Depends(get_db),
):
    controller = PostController(db)
    return controller.find_all(page, limit)


@router.post(
    "",
    response_model=IdResponse,
    status_code=201,
    summary="Criar Post",
    description="Cria um novo Post e retorna o ID (UUID) gerado para o registro.",
)
async def create(data: PostCreateDto, db: Session = Depends(get_db)):
    controller = PostController(db)
    return controller.create(data)


@router.get(
    "/{post_id}",
    response_model=PostResponseDto,
    responses={
        404: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post não encontrado"}}
            },
        }
    },
    summary="Buscar Post por ID",
    description=(
        "Retorna os dados de um Post específico a partir do seu ID (UUID). "
        "Responde 404 caso o Post não seja encontrado."
    ),
)
async def find_by_id(post_id: PostIdPath, db: Session = Depends(get_db)):
    controller = PostController(db)
    return controller.find_by_id(post_id)


@router.get(
    "/username/{posts_username}",
    response_model=PaginationResponse[PostResponseDto],
    summary="Listar Posts por username",
    description=(
        "Retorna uma lista paginada de Posts cujo username contém o termo "
        "informado (busca parcial, sem diferenciar posição do texto)."
    ),
)
async def find_all_by_username(
    posts_username: Annotated[
        str,
        Path(
            description="Username (ou parte dele) para filtrar os Posts",
            openapi_examples={
                "exemplo": {
                    "summary": "Username de exemplo",
                    "value": "juninhogameplays",
                },
            },
        ),
    ],
    page: PageQuery = 1,
    limit: LimitQuery = 10,
    db: Session = Depends(get_db),
):
    controller = PostController(db)
    return controller.find_all_by_username(posts_username, page, limit)


@router.patch(
    "/{post_id}",
    responses={
        404: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post não encontrado"}}
            },
        }
    },
    summary="Atualizar Post",
    description=(
        "Atualiza o conteúdo (body) de um Post existente. "
        "Responde 404 caso o Post não seja encontrado."
    ),
)
async def update(
    post_id: PostIdPath, data: PostUpdateDto, db: Session = Depends(get_db)
):
    controller = PostController(db)
    return controller.update(post_id, data)


@router.patch(
    "/archive/{post_id}",
    status_code=204,
    responses={
        404: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post não encontrado"}}
            },
        },
        409: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post já está arquivado"}}
            },
        },
    },
    summary="Arquivar Post",
    description=(
        "Marca um Post como arquivado. Responde 404 caso o Post não seja "
        "encontrado e 409 caso ele já esteja arquivado."
    ),
)
async def archive(post_id: PostIdPath, db: Session = Depends(get_db)):
    controller = PostController(db)
    return controller.archive(post_id)


@router.patch(
    "/unarchive/{post_id}",
    status_code=204,
    responses={
        404: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post não encontrado"}}
            },
        },
        409: {
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {"message": "Post já está desarquivado"}
                }
            },
        },
    },
    summary="Desarquivar Post",
    description=(
        "Remove a marcação de arquivado de um Post. Responde 404 caso o Post "
        "não seja encontrado e 409 caso ele já esteja desarquivado."
    ),
)
async def unarchive(post_id: PostIdPath, db: Session = Depends(get_db)):
    controller = PostController(db)
    return controller.unarchive(post_id)


@router.delete(
    "/{post_id}",
    status_code=204,
    responses={
        404: {
            "model": ErrorResponse,
            "content": {
                "application/json": {"example": {"message": "Post não encontrado"}}
            },
        }
    },
    summary="Excluir Post",
    description=(
        "Remove permanentemente um Post a partir do seu ID (UUID). "
        "Responde 404 caso o Post não seja encontrado."
    ),
)
async def delete(post_id: PostIdPath, db: Session = Depends(get_db)):
    controller = PostController(db)
    return controller.delete(post_id)
