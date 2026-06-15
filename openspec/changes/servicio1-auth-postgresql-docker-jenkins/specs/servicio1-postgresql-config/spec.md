## ADDED Requirements

### Requirement: Configuración de base de datos por variables de entorno
El sistema MUST construir la conexión a PostgreSQL a partir de variables de entorno y no SHALL hardcodear credenciales en el código fuente.

#### Scenario: Variables completas en entorno
- **WHEN** existen variables de host, puerto, base, usuario y contraseña de PostgreSQL
- **THEN** el sistema inicializa correctamente la conexión y permite operaciones de persistencia

#### Scenario: Variables faltantes
- **WHEN** falta una variable requerida para la conexión
- **THEN** el sistema MUST fallar en arranque con mensaje de configuración inválida

### Requirement: Persistencia de usuarios en PostgreSQL
El sistema SHALL almacenar y consultar usuarios en PostgreSQL mediante capa ORM consistente con el modelo de dominio de autenticación.

#### Scenario: Guardado de nuevo usuario
- **WHEN** el endpoint de registro crea un usuario válido
- **THEN** el registro queda persistido en PostgreSQL con campos esperados y password en hash

#### Scenario: Lectura de usuario para autenticación
- **WHEN** el endpoint de login valida credenciales
- **THEN** el sistema consulta PostgreSQL para recuperar usuario y verificar hash de contraseña