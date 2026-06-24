## MODIFIED Requirements

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