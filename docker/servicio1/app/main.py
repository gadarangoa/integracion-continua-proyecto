"""FastAPI application entrypoint for servicio1."""

from __future__ import annotations

from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from app.api.routes_auth import router as auth_router
from app.api.routes_health import router as health_router
from app.api.routes_users import router as users_router
from app.config import settings
from app.db.database import create_db_and_tables, ensure_database_exists


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Runs startup initialization and keeps compatibility with modern FastAPI lifecycle."""
    if settings.db_init_on_startup:
        if settings.db_create_database_if_missing:
            ensure_database_exists()
        create_db_and_tables()
    yield


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/ping-servicio2")
async def ping_servicio2() -> dict[str, object]:
    """Checks communication with servicio2 health endpoint."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.service2_url}/health", timeout=5.0)
            return {
                "desde": "servicio1",
                "hacia": "servicio2",
                "status_code": response.status_code,
                "respuesta": response.json(),
                "comunicacion": "exitosa",
            }
    except Exception as exc:
        return {
            "desde": "servicio1",
            "hacia": "servicio2",
            "comunicacion": "fallida",
            "error": str(exc),
        }
