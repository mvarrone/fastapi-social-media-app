from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app import main, oauth2
from app.config import settings
from fastapi import APIRouter, Depends

router = APIRouter(
    tags=["Documentation"]
)


@router.get("/docs", include_in_schema=False)
async def get_swagger_documentation(username: str = Depends(oauth2.get_swagger_access)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Docs - Swagger UI")


@router.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(username: str = Depends(oauth2.get_swagger_access)):
    return get_redoc_html(openapi_url="/openapi.json", title="Docs - ReDocly")


@router.get("/openapi.json", include_in_schema=False)
async def get_openapi_json_file(username: str = Depends(oauth2.get_swagger_access)):
    return get_openapi(
        title=main.app.title,
        description="📍Logged as " + username + " " + main.app.description,
        # version=settings.app_version,
        version="1.0.0",
        routes=main.app.routes
    )
