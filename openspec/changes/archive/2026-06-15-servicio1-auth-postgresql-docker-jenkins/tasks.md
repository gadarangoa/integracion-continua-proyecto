## 1. Preparación de estructura y dependencias

- [x] 1.1 Crear estructura base en servicio1: app/main, api, models, schemas, services, db y tests
- [x] 1.2 Agregar dependencias de autenticación, firma/validación de token, PostgreSQL y testing en requirements de servicio1
- [x] 1.3 Definir archivo de configuración de entorno (.env.example) con variables requeridas para app y base de datos

## 2. Configuración de base de datos PostgreSQL

- [x] 2.1 Implementar módulo de configuración para leer variables de entorno y construir DATABASE_URL
- [x] 2.2 Implementar sesión y engine de SQLAlchemy para PostgreSQL
- [x] 2.3 Crear modelo ORM de usuario con campos mínimos (id, email, password_hash, timestamps)
- [x] 2.4 Implementar inicialización de tablas en arranque controlado por entorno de desarrollo

## 3. Endpoints de autenticación básica

- [x] 3.1 Crear esquemas Pydantic para registro, login y respuestas de usuario
- [x] 3.2 Implementar servicio de hash y verificación de contraseña
- [x] 3.3 Implementar lógica de registro con validación de correo duplicado
- [x] 3.4 Implementar lógica de login con validación de credenciales y emisión de token
- [x] 3.5 Implementar servicio de validación de token (firma, expiración y extracción de identidad)
- [x] 3.6 Proteger GET /auth/me con validación de Bearer token
- [x] 3.7 Exponer endpoints GET /health, POST /auth/register, POST /auth/login, GET /auth/me y GET /users/{id}
- [x] 3.8 Estandarizar errores HTTP (401, 404, 409, 422) con mensajes explícitos

## 4. Pruebas unitarias mínimas

- [x] 4.1 Configurar pytest para servicio1 con fixtures básicas y cliente de pruebas
- [x] 4.2 Crear test unitario para GET /health con respuesta exitosa
- [x] 4.3 Crear test unitario para login exitoso con emisión de token
- [x] 4.4 Crear test unitario para endpoint protegido con token válido
- [x] 4.5 Crear test unitario para token inválido o ausente con respuesta 401
- [x] 4.6 Crear test unitario para caso inválido (correo duplicado o credenciales incorrectas)

## 5. Docker y Docker Compose

- [x] 5.1 Actualizar Dockerfile de servicio1 para ejecución CI-friendly sin autoreload
- [x] 5.2 Ajustar docker-compose para incluir PostgreSQL y variables de entorno de servicio1
- [x] 5.3 Verificar que compose levanta servicio1 conectado a PostgreSQL y healthcheck operativo

## 6. Jenkins CI/CD local

- [x] 6.1 Crear o actualizar Jenkinsfile declarativo con stages checkout, install, test, build y deploy
- [x] 6.2 Configurar stage test para ejecutar pytest de servicio1 y fallar ante errores
- [x] 6.3 Configurar stage build para construir imagen Docker de servicio1
- [x] 6.4 Configurar stage deploy para ejecutar despliegue local con Docker Compose

## 7. Validación final y documentación mínima

- [x] 7.1 Ejecutar validación local completa (pytest + docker compose up)
- [x] 7.2 Confirmar que endpoints requeridos responden en Swagger/OpenAPI
- [x] 7.3 Actualizar README con comandos de ejecución, pruebas y pipeline Jenkins
