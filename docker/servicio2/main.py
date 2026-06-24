from __future__ import annotations

from typing import Annotated

import httpx
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from config import settings

app = FastAPI(
    title="Servicio 2",
    description="Microservicio 2 - Proyecto Integración Continua",
    version="1.0.0"
)

SERVICIO1_URL = settings.servicio1_url
SERVICIO1_VALIDATE_TOKEN_URL = settings.validate_token_url
SERVICIO1_VALIDATE_TIMEOUT = settings.servicio1_validate_timeout
bearer_scheme = HTTPBearer(auto_error=False)


async def require_valid_token(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)] = None,
) -> None:
    """Validates bearer token through servicio1 and raises 401 on any authentication failure."""
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization token",
        )

    if credentials.scheme.lower() != "bearer" or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
        )

    token = credentials.credentials

    try:
        async with httpx.AsyncClient(timeout=SERVICIO1_VALIDATE_TIMEOUT) as client:
            response = await client.post(
                SERVICIO1_VALIDATE_TOKEN_URL,
                json={"token": token},
            )
    except httpx.HTTPError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token validation service unavailable",
        )

    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    payload = response.json()
    if not payload.get("valid", False):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


@app.get("/")
async def root(_: None = Depends(require_valid_token)):
    return {
        "servicio": "servicio2",
        "status": "ok",
        "puerto": 4000,
        "mensaje": "Servicio 2 corriendo correctamente"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "servicio": "servicio2"}


@app.get("/ping-servicio1")
async def ping_servicio1(_: None = Depends(require_valid_token)):
    """Prueba la comunicacion con servicio1"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{SERVICIO1_URL}/health", timeout=5.0)
            return {
                "desde": "servicio2",
                "hacia": "servicio1",
                "status_code": response.status_code,
                "respuesta": response.json(),
                "comunicacion": "exitosa"
            }
    except Exception as e:
        return {
            "desde": "servicio2",
            "hacia": "servicio1",
            "comunicacion": "fallida",
            "error": str(e)
        }
