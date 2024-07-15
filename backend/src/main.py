from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRoute
from fastapi_pagination import add_pagination
from fastapi_responses import custom_openapi
from starlette.middleware.cors import CORSMiddleware

from src.api.v1 import api_router
from src.core.config import settings

logger = structlog.stdlib.get_logger()


def app_factory(title: str) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info(f"Application {app.title} startup")
        yield
        logger.info(f"Application {app.title} shutdown")

    def custom_generate_unique_id(route: APIRoute) -> str:
        """For correct naming in generated frontend client"""
        return route.name

    created_app = FastAPI(
        title=title,
        version="0.1",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        default_response_class=ORJSONResponse,
        docs_url="/docs",
        redoc_url=None,
        lifespan=lifespan,
        generate_unique_id_function=custom_generate_unique_id,
    )
    created_app.openapi = custom_openapi(created_app)

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        created_app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    add_pagination(created_app)
    api_router.add_api_route("/health", lambda: {"status": "I am alive!"}, include_in_schema=False)
    created_app.include_router(api_router, prefix=settings.API_V1_STR)

    return created_app


app = app_factory(settings.PROJECT_NAME)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=settings.DEBUG,
        log_level="debug" if settings.DEBUG else "critical",
    )
