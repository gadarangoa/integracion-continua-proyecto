## 1. Preparación de estructura y dependencias

- [ ] 1.1 Crear estructura base en servicio1: app/main, api, models, schemas, services, db y tests
- [ ] 1.2 Agregar dependencias de autenticación, firma/validación de token, PostgreSQL y testing en requirements de servicio1
- [ ] 1.3 Definir archivo de configuración de entorno (.env.example) con variables requeridas para app y base de datos

## 2. Configuración de base de datos PostgreSQL

- [ ] 2.1 Implementar módulo de configuración para leer variables de entorno y construir DATABASE_URL
- [ ] 2.2 Implementar sesión y engine de SQLAlchemy para PostgreSQL
- [ ] 2.3 Crear modelo ORM de usuario con campos mínimos (id, email, password_hash, timestamps)
- [ ] 2.4 Implementar inicialización de tablas en arranque controlado por entorno de desarrollo

## 3. Endpoints de autenticación básica

- [ ] 3.1 Crear esquemas Pydantic para registro, login y respuestas de usuario
- [ ] 3.2 Implementar servicio de hash y verificación de contraseña
- [ ] 3.3 Implementar lógica de registro con validación de correo duplicado
- [ ] 3.4 Implementar lógica de login con validación de credenciales y emisión de token
- [ ] 3.5 Implementar servicio de validación de token (firma, expiración y extracción de identidad)
- [ ] 3.6 Proteger GET /auth/me con validación de Bearer token
- [ ] 3.7 Exponer endpoints GET /health, POST /auth/register, POST /auth/login, GET /auth/me y GET /users/{id}
- [ ] 3.8 Estandarizar errores HTTP (401, 404, 409, 422) con mensajes explícitos

## 4. Pruebas unitarias mínimas

- [ ] 4.1 Configurar pytest para servicio1 con fixtures básicas y cliente de pruebas
- [ ] 4.2 Crear test unitario para GET /health con respuesta exitosa
- [ ] 4.3 Crear test unitario para login exitoso con emisión de token
- [ ] 4.4 Crear test unitario para endpoint protegido con token válido
- [ ] 4.5 Crear test unitario para token inválido o ausente con respuesta 401
- [ ] 4.6 Crear test unitario para caso inválido (correo duplicado o credenciales incorrectas)

## 5. Docker y Docker Compose

- [ ] 5.1 Actualizar Dockerfile de servicio1 para ejecución CI-friendly sin autoreload
- [ ] 5.2 Ajustar docker-compose para incluir PostgreSQL y variables de entorno de servicio1
- [ ] 5.3 Verificar que compose levanta servicio1 conectado a PostgreSQL y healthcheck operativo

## 6. Jenkins CI/CD local

- [ ] 6.1 Crear o actualizar Jenkinsfile declarativo con stages checkout, install, test, build y deploy
- [ ] 6.2 Configurar stage test para ejecutar pytest de servicio1 y fallar ante errores
- [ ] 6.3 Configurar stage build para construir imagen Docker de servicio1
- [ ] 6.4 Configurar stage deploy para ejecutar despliegue local con Docker Compose

## 7. Validación final y documentación mínima

- [ ] 7.1 Ejecutar validación local completa (pytest + docker compose up)
- [ ] 7.2 Confirmar que endpoints requeridos responden en Swagger/OpenAPI
- [ ] 7.3 Actualizar README con comandos de ejecución, pruebas y pipeline Jenkins