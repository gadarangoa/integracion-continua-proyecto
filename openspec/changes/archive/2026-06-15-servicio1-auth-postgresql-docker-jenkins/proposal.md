## Why

El servicio1 actualmente no cuenta con un flujo de autenticación básico desacoplado y verificable en CI, lo que impide demostrar seguridad mínima y trazabilidad de calidad en el proyecto. Se necesita ahora para cumplir los hitos académicos de integración continua con una base reproducible para evolución futura (JWT, roles y permisos).

## What Changes

- Implementar endpoints de autenticación básica en servicio1: registro, login, usuario autenticado, consulta de usuario y healthcheck.
- Añadir emisión y validación de token de acceso para proteger endpoints autenticados.
- Incorporar persistencia en PostgreSQL con configuración por variables de entorno.
- Agregar pruebas unitarias mínimas para validar comportamiento observable de autenticación y salud del servicio.
- Ajustar configuración de Docker y Docker Compose para ejecución local y validación en CI.
- Añadir configuración de Jenkins con etapas explícitas para Test, Build y Deploy local.

## Capabilities

### New Capabilities
- `servicio1-basic-auth`: Provee endpoints de autenticación básica, emisión de token y lectura de perfil de usuario autenticado mediante token válido.
- `servicio1-postgresql-config`: Define persistencia en PostgreSQL con parámetros por entorno y conexión en contenedor.
- `servicio1-ci-docker-jenkins`: Estandariza pruebas, build de imagen y despliegue local automatizado en pipeline Jenkins.

### Modified Capabilities
- Ninguna.

## Non-goals

- No se implementará OAuth2 completo ni refresh tokens en esta entrega.
- No se incorporará un sistema avanzado de autorización por permisos granulares.
- No se desplegará a nube; el alcance de deploy se limita a entorno local con Docker Compose.

## Impact

- Código afectado: servicio1 (rutas, lógica de autenticación, modelos/esquemas y configuración de base de datos), pruebas y artefactos de infraestructura.
- APIs afectadas: endpoints HTTP de autenticación, validación de token y consulta de usuario.
- Dependencias: controlador PostgreSQL para SQLAlchemy, utilidades de pruebas para FastAPI/pytest y librería de firma/validación de token.
- Sistemas: Docker/Docker Compose para ejecución y Jenkins para automatización CI/CD local.