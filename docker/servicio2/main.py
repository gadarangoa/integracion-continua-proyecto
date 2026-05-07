from fastapi import FastAPI
import httpx
import os

app = FastAPI(
    title="Servicio 2",
    description="Microservicio 2 - Proyecto Integración Continua",
    version="1.0.0"
)

SERVICIO1_URL = os.getenv("SERVICIO1_URL", "http://contenedor1:3000")


@app.get("/")
def root():
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
async def ping_servicio1():
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
