from fastapi import FastAPI, APIRouter
import uvicorn

from app.configs.database import create_tables
from app.configs.settings import settings
from app.routes.post_router import router as post
from app.routes.health_router import router as health

create_tables()

# Em prod a documentação é desabilitada
is_dev = settings.API_MODE == "dev"

app = FastAPI(
    title="First Crud FastAPI",
    description="Uma api simples para testar FastAPI",
    version="0.0.1",
    docs_url="/api/docs" if is_dev else None,
    redoc_url="/api/redoc" if is_dev else None,
    openapi_url="/api/openapi.json" if is_dev else None,
)

api_router = APIRouter(prefix="/api")
api_router.include_router(post)
api_router.include_router(health)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
