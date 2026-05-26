# Integración Continua - Proyecto Grupal

**Módulo:** Énfasis Profesional I - Integración Continua  
**Institución:** Politécnico Grancolombiano  
**Tipo de entrega:** Proyecto Grupal  

---

## 📋 Descripción

Este repositorio contiene el proyecto grupal del módulo de Integración Continua, desarrollado en tres entregas progresivas que integran herramientas como **GitHub**, **Docker**, **Jenkins**, **Travis CI** y **Codeship**.

Cada servicio es una API REST construida con **FastAPI** (Python), desplegada en contenedores Docker que se comunican entre sí a través de una red interna.

---

## 🗂️ Estructura del proyecto

```
integracion-continua-proyecto/
├── README.md
├── .gitignore
├── docker-compose.yml
├── docs/
│   └── entrega1/
└── docker/
    ├── servicio1/
    │   ├── Dockerfile
    │   ├── main.py
    │   └── requirements.txt
    └── servicio2/
        ├── Dockerfile
        ├── main.py
        └── requirements.txt
```

---

## 🚀 Entregas

### Entrega 1 - Semana 3
- [x] Proyecto creado en GitHub
- [x] Construcción de dos contenedores Docker con FastAPI
- [x] Comunicación entre contenedores via Docker Compose

### Entrega 2 - Semana 5
- [ ] Implementación de Jenkins como gestor de operaciones
- [ ] Documento con características de la implementación

### Entrega 3 y Sustentación - Semanas 7 y 8
- [ ] Integración completa con contenedores, Jenkins, Travis CI y Codeship
- [ ] Historial de cambios consolidado
- [ ] Documento con responsabilidades y conclusiones

---

## 🐳 Cómo levantar los servicios

### ✅ Opción recomendada: Docker Compose

```bash
# Construir imágenes y levantar ambos servicios
docker-compose up --build

# Levantar en segundo plano
docker-compose up --build -d

# Ver logs de un servicio
docker-compose logs servicio1
docker-compose logs servicio2

# Detener los servicios
docker-compose down
```

### Opción manual: Docker sin Compose

```bash
# Crear la red compartida
docker network create red-ic

# Construir imágenes
docker build -t servicio1 ./docker/servicio1
docker build -t servicio2 ./docker/servicio2

# Levantar contenedores en la red
docker run -d --name contenedor1 --network red-ic -p 3000:3000 servicio1
docker run -d --name contenedor2 --network red-ic -p 4000:4000 servicio2

# Verificar contenedores activos
docker ps
```

---

## 🌐 Endpoints

### Servicio 1 — `http://localhost:3000`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Info del servicio |
| GET | `/health` | Estado de salud |
| GET | `/ping-servicio2` | Prueba comunicación hacia Servicio 2 |
| GET | `/docs` | Documentación interactiva Swagger UI |

### Servicio 2 — `http://localhost:4000`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Info del servicio |
| GET | `/health` | Estado de salud |
| GET | `/ping-servicio1` | Prueba comunicación hacia Servicio 1 |
| GET | `/docs` | Documentación interactiva Swagger UI |

---

## 🔌 Probar comunicación entre contenedores

Una vez levantados los servicios con `docker-compose up --build`:

```bash
# Desde el host: S1 llama a S2
curl http://localhost:3000/ping-servicio2

# Desde el host: S2 llama a S1
curl http://localhost:4000/ping-servicio1

# Desde dentro del contenedor2 hacia contenedor1
docker exec -it contenedor2 curl http://contenedor1:3000/health
```

Respuesta esperada de `/ping-servicio2`:
```json
{
  "desde": "servicio1",
  "hacia": "servicio2",
  "status_code": 200,
  "respuesta": { "status": "healthy", "servicio": "servicio2" },
  "comunicacion": "exitosa"
}
```

Los contenedores se comunican a través de la red interna `red-ic` y se reconocen por nombre (`contenedor1`, `contenedor2`).

---

## 🛠️ Stack tecnológico

| Herramienta | Versión | Uso |
|-------------|---------|-----|
| Python | 3.11 | Lenguaje base |
| FastAPI | 0.111.0 | Framework API REST |
| Uvicorn | 0.29.0 | Servidor ASGI |
| HTTPX | 0.27.0 | Cliente HTTP entre servicios |
| Docker | - | Contenedores |
| Docker Compose | - | Orquestación local |

---

## 👥 Integrantes

| Nombre | GitHub |
|--------|--------|
| (Pendiente) | - |
| Anngie Paola Casteblanco | Acasteb30|
| Kevin Alexander Fierro Cortes | Kevin-Fierro |
| (Pendiente) | - |
| (Pendiente) | - |

---

## 📚 Referencias

- Docker. (s.f.). *Get started*. https://docs.docker.com/get-started/part1
- Docker. (s.f.). *Docker Compose overview*. https://docs.docker.com/compose/
- FastAPI. (s.f.). *FastAPI documentation*. https://fastapi.tiangolo.com
- Politécnico Grancolombiano. (2017). *Máquinas virtuales y Dockers para construcción de ambientes*. Unidad 2, Escenario 3.
