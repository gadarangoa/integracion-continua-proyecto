"""Health and base routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root() -> dict[str, object]:
    """Returns basic service metadata."""
    return {
        "servicio": "servicio1",
        "status": "ok",
        "puerto": 3000,
        "mensaje": "Servicio 1 corriendo correctamente",
    }


@router.get("/health")
def health() -> dict[str, str]:
    """Returns service health status."""
    return {"status": "healthy", "servicio": "servicio1"}
