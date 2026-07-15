"""FastAPI application construction and ASGI entry point."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_v1_router
from app.core.config import Settings, get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.schemas.health import ApplicationMetadata

logger = logging.getLogger(__name__)


def create_application(settings: Settings | None = None) -> FastAPI:
    """Create and configure the MindVault FastAPI application."""
    application_settings = settings or get_settings()
    configure_logging(application_settings.log_level)

    @asynccontextmanager
    async def lifespan(_application: FastAPI) -> AsyncIterator[None]:
        logger.info(
            "Starting %s version %s in %s",
            application_settings.app_name,
            application_settings.app_version,
            application_settings.app_env.value,
        )
        yield

    application = FastAPI(
        title=application_settings.app_name,
        description="AI-powered personal knowledge management API.",
        version=application_settings.app_version,
        debug=application_settings.app_debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    origins = application_settings.cors_origin_list
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials="*" not in origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_exception_handlers(application)
    application.include_router(api_v1_router, prefix=application_settings.api_v1_prefix)

    @application.get("/", response_model=ApplicationMetadata, tags=["metadata"])
    async def root() -> ApplicationMetadata:
        """Return public application metadata."""
        return ApplicationMetadata(
            name=application_settings.app_name,
            version=application_settings.app_version,
            environment=application_settings.app_env,
            docs_url=application.docs_url or "",
        )

    return application


app = create_application()
