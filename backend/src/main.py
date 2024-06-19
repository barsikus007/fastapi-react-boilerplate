from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRoute
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from src.api.v1 import api_router
from src.core.config import settings


def custom_generate_unique_id(route: APIRoute):
    """For cerrect naming in generated frontend client"""
    return route.name


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    default_response_class=ORJSONResponse,
    docs_url="/docs",
    redoc_url=None,
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

add_pagination(app)
app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_api_route("api/health", lambda: {"status": "I am alive!"}, include_in_schema=False)  # pyright: ignore[reportArgumentType]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=settings.DEBUG,
        log_level="debug" if settings.DEBUG else "critical",
    )
