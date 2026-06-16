## 1. Endpoint de validación en servicio1

- [x] 1.1 Revisar rutas y esquemas actuales de auth en servicio1 para ubicar el nuevo endpoint interno
- [x] 1.2 Definir request/response schema mínimo para validación de token (`valid` y detalle opcional)
- [x] 1.3 Implementar endpoint de validación de token en servicio1 usando la lógica existente de verificación JWT
- [x] 1.4 Mapear errores de token inválido/expirado a respuesta consistente para consumo interno

## 2. Protección de endpoints en servicio2

- [x] 2.1 Crear dependencia `Depends` de autenticación en servicio2 que lea el header Authorization
- [x] 2.2 Implementar llamada HTTP interna desde servicio2 a servicio1 para validar token con timeout corto
- [x] 2.3 Aplicar protección a endpoints objetivo de servicio2 dejando solo `/health` como ruta pública
- [x] 2.4 Estandarizar respuestas 401 para token ausente, inválido o expirado

## 3. Configuración y resiliencia

- [x] 3.1 Agregar variables de entorno para URL interna de validación y timeout en servicio2
- [x] 3.2 Implementar política de fallo cerrado con respuesta 401 cuando servicio1 no responda en validación interna
- [x] 3.3 Verificar configuración de red entre servicios en docker-compose para resolución por hostname

## 4. Alcance funcional

- [x] 4.1 Confirmar validación binaria en servicio2 (sin propagación de claims al contexto)

## 5. Pruebas

- [x] 5.1 Agregar pruebas unitarias en servicio1 para token válido, inválido y expirado en el endpoint interno
- [x] 5.2 Agregar pruebas en servicio2 para acceso con token válido en endpoints protegidos
- [x] 5.3 Agregar pruebas en servicio2 para rechazo 401 sin token y con token inválido
- [x] 5.4 Agregar prueba de error de comunicación servicio2→servicio1 con respuesta 401 por fallo cerrado
- [x] 5.5 Agregar prueba de `/health` público sin token

## 6. Verificación final

- [x] 6.1 Ejecutar suite de pruebas de servicio1 y servicio2 en local
- [x] 6.2 Validar flujo manual con docker-compose: token emitido en servicio1 y acceso protegido en servicio2
- [x] 6.3 Actualizar documentación mínima de endpoints y variables de entorno nuevas