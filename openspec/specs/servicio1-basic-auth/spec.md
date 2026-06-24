## ADDED Requirements

### Requirement: Endpoints de autenticación básica
El sistema SHALL exponer endpoints HTTP para registro de usuarios, inicio de sesión y obtención del perfil autenticado, con contratos de entrada/salida definidos en esquemas de FastAPI.

#### Scenario: Registro exitoso
- **WHEN** el cliente envía un correo no registrado y contraseña válida al endpoint de registro
- **THEN** el sistema crea el usuario, almacena la contraseña hasheada y retorna respuesta de éxito con identificador del usuario

#### Scenario: Registro con correo duplicado
- **WHEN** el cliente intenta registrar un correo ya existente
- **THEN** el sistema MUST responder con error de conflicto y no crear un nuevo usuario

### Requirement: Validación de credenciales en login
El sistema MUST validar credenciales contra datos persistidos y rechazar accesos con credenciales inválidas.

#### Scenario: Login exitoso
- **WHEN** el cliente envía credenciales correctas al endpoint de login
- **THEN** el sistema retorna una respuesta de autenticación exitosa para ese usuario incluyendo token de acceso firmado

#### Scenario: Login fallido
- **WHEN** el cliente envía contraseña incorrecta o usuario inexistente
- **THEN** el sistema MUST responder con error de autenticación sin revelar detalles sensibles

### Requirement: Validación de token para endpoints protegidos
El sistema MUST validar firma, formato y expiración del token de acceso antes de permitir acceso a endpoints autenticados y SHALL exponer un endpoint interno para validar tokens emitidos para consumo entre microservicios en la misma red.

#### Scenario: Token válido
- **WHEN** el cliente envía un Bearer token válido y no expirado a un endpoint protegido
- **THEN** el sistema permite el acceso y resuelve la identidad del usuario autenticado

#### Scenario: Token ausente
- **WHEN** el cliente invoca un endpoint protegido sin token
- **THEN** el sistema MUST responder con error 401 de autenticación requerida

#### Scenario: Token inválido o expirado
- **WHEN** el cliente envía un token con firma inválida o expirado
- **THEN** el sistema MUST responder con error 401 y no exponer datos de usuario

#### Scenario: Validación interna de token por servicio2
- **WHEN** servicio2 solicita la validación de un token emitido a través del endpoint interno de servicio1
- **THEN** servicio1 MUST responder si el token es válido o inválido según firma, formato y expiración

### Requirement: Consulta de perfil y usuario por identificador
El sistema SHALL permitir consultar el usuario autenticado mediante endpoint dedicado protegido por token y recuperar un usuario por id cuando exista.

#### Scenario: Consulta de perfil autenticado
- **WHEN** un usuario autenticado invoca el endpoint de perfil
- **THEN** el sistema retorna los datos del usuario autenticado según el esquema de respuesta

#### Scenario: Usuario por id no encontrado
- **WHEN** se consulta un id de usuario inexistente
- **THEN** el sistema MUST responder con error 404 y mensaje explícito de recurso no encontrado