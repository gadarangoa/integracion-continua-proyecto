## ADDED Requirements

### Requirement: Protección de endpoints en servicio2 con validación de token
El sistema MUST proteger los endpoints definidos de servicio2 exigiendo un token Bearer válido, verificado contra servicio1 dentro de la red interna.

#### Scenario: Endpoint público de salud
- **WHEN** el cliente invoca `/health` en servicio2 sin token
- **THEN** servicio2 MUST permitir la respuesta normal del endpoint

#### Scenario: Acceso autorizado con token válido
- **WHEN** el cliente invoca un endpoint protegido de servicio2 con un Bearer token válido
- **THEN** servicio2 permite el acceso al endpoint y continúa la ejecución normal

#### Scenario: Rechazo por token ausente
- **WHEN** el cliente invoca un endpoint protegido de servicio2 sin encabezado Authorization
- **THEN** servicio2 MUST responder con estado 401 y mensaje de autenticación requerida

#### Scenario: Rechazo por token inválido o expirado
- **WHEN** el cliente invoca un endpoint protegido de servicio2 con un token inválido, malformado o expirado
- **THEN** servicio2 MUST responder con estado 401 y no exponer información sensible del recurso

### Requirement: Integración interna de servicio2 con endpoint de validación de servicio1
El sistema SHALL consultar un endpoint interno de validación en servicio1 para decidir la autenticación de solicitudes protegidas en servicio2.

#### Scenario: Validación interna exitosa
- **WHEN** servicio2 envía el token recibido al endpoint interno de validación de servicio1 y obtiene resultado válido
- **THEN** servicio2 MUST tratar la solicitud como autenticada

#### Scenario: Error de comunicación con servicio1
- **WHEN** servicio2 no puede comunicarse con servicio1 durante la validación interna
- **THEN** servicio2 MUST rechazar la solicitud protegida con estado 401 bajo política de fallo cerrado

### Requirement: Validación binaria sin propagación de claims en servicio2
El sistema SHALL basar la autenticación en un resultado binario de validación (`válido/inválido`) sin requerir propagación de claims del token al contexto de servicio2.

#### Scenario: Solicitud autenticada por validación binaria
- **WHEN** servicio2 recibe confirmación de token válido desde servicio1
- **THEN** servicio2 MUST permitir la solicitud sin depender de claims del token