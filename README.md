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

### Levantar solo servicio1 (con PostgreSQL)

Si quieres trabajar únicamente en autenticación de `servicio1`, puedes levantar solo su base y el servicio:

```bash
# Levantar PostgreSQL y servicio1
docker compose up -d --build postgres servicio1

# Verificar estado de contenedores
docker compose ps

# Ver logs de servicio1
docker compose logs -f servicio1
```

Notas importantes:

- `servicio1` queda disponible en `http://localhost:3000`
- PostgreSQL del compose se expone en `localhost:5433` para evitar conflicto con un PostgreSQL local en `5432`
- El servicio crea la base de datos automáticamente al iniciar si no existe (según variables de entorno)

Verificación rápida:

```bash
curl http://localhost:3000/health
curl -I http://localhost:3000/docs
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
| POST | `/auth/register` | Registro de usuario |
| POST | `/auth/login` | Login y emisión de token Bearer |
| GET | `/auth/me` | Perfil del usuario autenticado (requiere token) |
| GET | `/users/{id}` | Consulta de usuario por id |
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

## 🧪 Pruebas locales (servicio1)

```bash
# Crear entorno virtual (si no existe)
python3 -m venv .venv

# Instalar dependencias de servicio1
. .venv/bin/activate && pip install -r docker/servicio1/requirements.txt

# Ejecutar pruebas de servicio1
cd docker/servicio1 && pytest -q
```

### ▶️ Cómo ejecutar los tests (rápido)

Desde la raíz del proyecto:

```bash
. .venv/bin/activate
cd docker/servicio1
pytest -q
```

O en una sola línea desde la raíz:

```bash
PYTHONPATH=docker/servicio1 ./.venv/bin/python -m pytest -q docker/servicio1/tests
```

Nota (zsh/bash): evita usar sintaxis de PowerShell como `$env:PYTHONPATH=.`.
En macOS/Linux usa `PYTHONPATH=... comando` o `export PYTHONPATH=...`.

## 🤖 Jenkins (pipeline local)

Se agregó un `Jenkinsfile` declarativo con etapas:

1. checkout
2. install
3. test
4. build
5. deploy

Comandos clave del pipeline:

- `pytest -q` sobre `docker/servicio1`
- `docker build -t servicio1:ci ./docker/servicio1`
- `docker compose up -d --build servicio1 postgres`

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
| Gustavo Adolfo Arango | gadarangoa |
| Anngie Paola Casteblanco | Acasteb30|
| Kevin Alexander Fierro Cortes | Kevin-Fierro |
| Julio Cesar Rosero Mejia | JulioTheCoder |
| (Pendiente) | - |

---

## 📚 Referencias

- Docker. (s.f.). *Get started*. https://docs.docker.com/get-started/part1
- Docker. (s.f.). *Docker Compose overview*. https://docs.docker.com/compose/
- FastAPI. (s.f.). *FastAPI documentation*. https://fastapi.tiangolo.com
- Politécnico Grancolombiano. (2017). *Máquinas virtuales y Dockers para construcción de ambientes*. Unidad 2, Escenario 3.
