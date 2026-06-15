## ADDED Requirements

### Requirement: Docker de servicio1 para ejecución reproducible
El sistema SHALL incluir configuración Docker de servicio1 apta para entorno local y CI, sin modo autoreload en ejecución orientada a pipeline.

#### Scenario: Build de imagen exitoso
- **WHEN** se ejecuta build de Docker para servicio1 con dependencias declaradas
- **THEN** se genera imagen funcional que inicia FastAPI en el puerto configurado

#### Scenario: Arranque con Docker Compose
- **WHEN** se levanta la orquestación local con servicio1 y PostgreSQL
- **THEN** servicio1 inicia, se conecta a la base de datos y expone endpoint de health operativo

### Requirement: Pipeline Jenkins con etapas explícitas
El sistema MUST definir un Jenkinsfile declarativo con etapas checkout, install, test, build y deploy para validar cambios de forma repetible.

#### Scenario: Etapa test en pipeline
- **WHEN** Jenkins ejecuta la etapa de test
- **THEN** el pipeline corre pruebas automatizadas de servicio1 y falla si alguna prueba no pasa

#### Scenario: Etapa build y deploy local
- **WHEN** las etapas previas finalizan correctamente
- **THEN** Jenkins construye la imagen Docker y ejecuta despliegue local con Docker o Docker Compose

### Requirement: Pruebas unitarias mínimas de servicio1
El sistema SHALL incluir pruebas unitarias mínimas para validar salud del servicio y comportamientos críticos de autenticación.

#### Scenario: Ejecución de suite mínima
- **WHEN** se ejecuta pytest en servicio1
- **THEN** se validan al menos healthcheck, login con emisión de token y rechazo de acceso con token inválido o ausente

#### Scenario: Validación de token en pipeline
- **WHEN** Jenkins ejecuta la etapa test
- **THEN** la suite MUST incluir al menos un caso de token válido y un caso de token inválido en endpoint protegido