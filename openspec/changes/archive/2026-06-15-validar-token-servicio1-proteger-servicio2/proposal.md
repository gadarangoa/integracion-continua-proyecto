## Why

Actualmente el token JWT se emite en servicio1, pero no existe un endpoint explícito para validarlo de forma centralizada ni un mecanismo uniforme en servicio2 para rechazar tokens inválidos. Esto deja a servicio2 sin una política clara de autenticación y dificulta la evolución de la seguridad entre microservicios.

## What Changes

- Agregar en servicio1 un endpoint para validar si un token JWT es válido (firma, formato y vigencia).
- Definir la respuesta del endpoint de validación para uso interno entre servicios en la misma red.
- Proteger los endpoints de servicio2 usando middleware o dependencia `Depends` que verifique el token recibido.
- Estandarizar respuestas de error de autenticación en servicio2 (401 para token ausente/inválido/expirado).
- Mantener el enfoque simple y demostrable, sin incorporar autorización por roles en esta iteración.

## Capabilities

### New Capabilities
- `servicio2-token-protection`: Protección de endpoints de servicio2 mediante validación de token proveniente de servicio1.

### Modified Capabilities
- `servicio1-basic-auth`: Se amplían los requisitos para incluir un endpoint de validación de token para consumo interno.

## Non-goals

- No implementar autorización por roles/permisos.
- No introducir mTLS, service mesh ni firma asimétrica de tokens.
- No exponer este flujo como autenticación pública para clientes externos.
- No rediseñar completamente la arquitectura de seguridad existente.

## Impact

- Código afectado en servicio1: rutas de autenticación y servicio de tokens.
- Código afectado en servicio2: middleware o dependencia de autenticación en endpoints protegidos.
- APIs afectadas: nuevos contratos HTTP de validación interna y respuestas 401 estandarizadas.
- Pruebas: se requieren tests unitarios/integración para validación de token y protección de endpoints.
- Operación: dependencia de conectividad interna de red entre servicio2 y servicio1 para validar token.