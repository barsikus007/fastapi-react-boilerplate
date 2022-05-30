import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.api.api_v1.api import api_router


app = FastAPI(
    title="Boilerplate",
    description="Fastapi React boilerplate",
    version="0.1",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    default_response_class=ORJSONResponse,
    docs_url="/docs",
    redoc_url=None,
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

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1",
        log_level='debug' if settings.DEBUG else "critical",
        debug=settings.DEBUG, reload=settings.DEBUG,
    )
