from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.controllers.health_controller import HealthController
from app.schemas.health_schema import HealthResponse


router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "",
    response_model=HealthResponse,
    summary="Verificar saúde da aplicação",
    description=(
        "Verifica a saúde da aplicação testando a conexão com o banco de "
        "dados (Postgres). Responde 200 quando o banco está acessível e 503 "
        "quando a conexão falha."
    ),
    responses={
        200: {
            "model": HealthResponse,
            "description": "Aplicação e banco de dados operacionais",
            "content": {
                "application/json": {
                    "example": {
                        "status": "Ok",
                        "message": "Postgres database está on",
                    }
                }
            },
        },
        503: {
            "model": HealthResponse,
            "description": "Banco de dados indisponível",
            "content": {
                "application/json": {
                    "example": {
                        "status": "Failure",
                        "message": "Postgres database está off",
                    }
                }
            },
        },
    },
)
async def healthchecker(db: Session = Depends(get_db)):
    controller = HealthController(db)
    return controller.healthchecker()
