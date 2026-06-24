## Context

servicio1 ya emite tokens JWT para autenticación local, pero servicio2 no tiene una política uniforme para exigir y validar esos tokens en sus endpoints. Al ser microservicios en la misma red de Docker Compose, necesitamos un mecanismo simple y explícito para validación centralizada en servicio1 y enforcement en servicio2 sin introducir complejidad adicional de malla de servicios o autorización avanzada.

Actores principales:
- Cliente que consume endpoints protegidos de servicio2.
- servicio2 como consumidor interno del endpoint de validación en servicio1.
- servicio1 como autoridad de validación de tokens emitidos.

## Goals / Non-Goals

**Goals:**
- Exponer en servicio1 un endpoint interno para validar token y responder si es válido.
- Proteger endpoints de servicio2 con middleware o `Depends` que obligue token válido.
- Estandarizar errores 401 en servicio2 para token ausente, inválido o expirado.
- Mantener implementación mínima, clara y demostrable para CI local.

**Non-Goals:**
- Autorización por roles/permisos.
- mTLS entre servicios, API Gateway o service mesh.
- Rotación avanzada de claves y firma asimétrica.

## Decisions

1. **Validación centralizada en servicio1 mediante endpoint HTTP interno**
Rationale: evita duplicar lógica de validación en varios servicios y permite evolución futura de reglas en un único punto.
Alternativas:
- Validar JWT localmente también en servicio2: más acoplamiento y duplicación.
- Compartir librería común de seguridad: útil a futuro, pero innecesario para alcance actual.

2. **Protección de servicio2 usando `Depends` en endpoints protegidos**
Rationale: `Depends` es idiomático en FastAPI y facilita aplicar protección de forma explícita por ruta, manteniendo `/health` como endpoint público para pruebas.
Alternativas:
- Middleware global: protege todo por defecto, pero puede requerir excepciones adicionales para rutas públicas.

3. **Contrato de validación interno simple (`valid: true/false` + motivo opcional)**
Rationale: simplifica integración y pruebas, manteniendo semántica clara para decisiones de acceso en servicio2.
Alternativas:
- Devolver payload completo del token: mayor superficie de datos sin necesidad inmediata.

4. **Fallo cerrado en servicio2 con respuesta 401**
Rationale: si servicio1 no es alcanzable o responde error, servicio2 debe rechazar acceso protegido con 401 para no abrir endpoints por error y mantener un comportamiento uniforme de autenticación.
Alternativas:
- Permitir acceso temporal en fallo de red: reduce seguridad y no aplica para este alcance.

5. **Validación binaria sin propagación de claims a servicio2**
Rationale: para esta iteración se prioriza simplicidad; servicio2 solo necesita saber si el token es válido.
Alternativas:
- Propagar claims mínimos al contexto de request: útil para autorización futura, fuera de alcance actual.

## Risks / Trade-offs

- [Dependencia de red interna entre servicios] → Mitigation: usar hostname de Compose, timeout corto y manejo explícito de errores.
- [Latencia adicional por llamada de validación] → Mitigation: limitar validación a endpoints protegidos y mantener endpoint de validación liviano.
- [Inconsistencias de formato de Authorization header] → Mitigation: normalizar parsing `Bearer <token>` y cubrir con tests.
- [Protección parcial por omisión de rutas] → Mitigation: listar explícitamente rutas protegidas y agregar tests de cobertura de seguridad.

## Migration Plan

1. Agregar endpoint de validación en servicio1 y sus pruebas unitarias/integración.
2. Implementar dependencia/middleware de autenticación en servicio2 apuntando a servicio1.
3. Aplicar protección a endpoints objetivo de servicio2 y definir exclusiones públicas.
4. Ejecutar pruebas en ambos servicios y validar docker-compose local.
5. Despliegue incremental en entorno local/CI.

Rollback:
- Revertir protección en servicio2 y retirar el endpoint de validación si se detecta regresión crítica.
- Mantener endpoints previos de servicio1 sin cambios para minimizar impacto.

## Open Questions

No hay preguntas abiertas para esta iteración. Decisiones cerradas:
- Respuesta 401 en servicio2 cuando servicio1 no responde durante validación interna.
- Solo `/health` queda público en servicio2 para pruebas iniciales.
- Se usa validación binaria (válido/inválido) sin propagación de claims.