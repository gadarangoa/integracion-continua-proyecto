from fastapi import FastAPI
import httpx
import os

app = FastAPI(
    title="Servicio 1",
    description="Microservicio 1 - Proyecto Integración Continua",
    version="1.0.0"
)

SERVICIO2_URL = os.getenv("SERVICIO2_URL", "http://contenedor2:4000")


@app.get("/")
def root():
    return {
        "servicio": "servicio1",
        "status": "ok",
        "puerto": 3000,
        "mensaje": "Servicio 1 corriendo correctamente"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "servicio": "servicio1"}


@app.get("/ping-servicio2")
async def ping_servicio2():
    """Prueba la comunicacion con servicio2"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{SERVICIO2_URL}/health", timeout=5.0)
            return {
                "desde": "servicio1",
                "hacia": "servicio2",
                "status_code": response.status_code,
                "respuesta": response.json(),
                "comunicacion": "exitosa"
            }
    except Exception as e:
        return {
            "desde": "servicio1",
            "hacia": "servicio2",
            "comunicacion": "fallida",
            "error": str(e)
        }
