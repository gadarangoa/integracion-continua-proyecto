# Integración Continua - Proyecto Grupal

**Módulo:** Énfasis Profesional I - Integración Continua  
**Institución:** Politécnico Grancolombiano  
**Tipo de entrega:** Proyecto Grupal  

---

## 📋 Descripción

Este repositorio contiene el proyecto grupal del módulo de Integración Continua, desarrollado en tres entregas progresivas que integran herramientas como **GitHub**, **Docker**, **Jenkins**, **Travis CI** y **Codeship**.

---

## 🗂️ Estructura del proyecto

```
integracion-continua-proyecto/
├── README.md
├── .gitignore
├── docker-compose.yml
├── docs/
│   └── entrega1/
└── docker/
    ├── servicio1/
    │   └── Dockerfile
    └── servicio2/
        └── Dockerfile
```

---

## 🚀 Entregas

### Entrega 1 - Semana 3
- [x] Proyecto creado en GitHub
- [x] Construcción de dos contenedores Docker
- [x] Comunicación entre contenedores via Docker Compose

### Entrega 2 - Semana 5
- [ ] Implementación de Jenkins como gestor de operaciones
- [ ] Documento con características de la implementación

### Entrega 3 y Sustentación - Semanas 7 y 8
- [ ] Integración completa con contenedores, Jenkins, Travis CI y Codeship
- [ ] Historial de cambios consolidado
- [ ] Documento con responsabilidades y conclusiones

---

## 🐳 Cómo levantar los contenedores

### ✅ Opción recomendada: Docker Compose

Levanta ambos contenedores conectados en la misma red con un solo comando:

```bash
# Construir y levantar ambos servicios
docker-compose up --build

# Levantar en segundo plano
docker-compose up --build -d

# Detener los servicios
docker-compose down
```

### Probar comunicación entre contenedores

```bash
# Verificar que contenedor2 puede comunicarse con contenedor1
docker exec -it contenedor2 curl http://contenedor1:3000
```

Los contenedores se comunican a través de la red interna `red-ic` y se reconocen por nombre.

---

### Opción manual: Docker sin Compose

```bash
# Crear la red compartida
docker network create red-ic

# Construir imágenes
docker build -t servicio1 ./docker/servicio1
docker build -t servicio2 ./docker/servicio2

# Levantar contenedores en la red
docker run -d --name contenedor1 --network red-ic -p 3000:3000 servicio1
docker run -d --name contenedor2 --network red-ic -p 4000:4000 servicio2

# Verificar contenedores activos
docker ps
```

---

## 🌐 Puertos expuestos

| Servicio | Puerto local | Puerto contenedor |
|----------|-------------|-------------------|
| servicio1 | 3000 | 3000 |
| servicio2 | 4000 | 4000 |

---

## 👥 Integrantes

| Nombre | GitHub |
|--------|--------|
| (Pendiente) | - |

---

## 📚 Referencias

- Docker. (s.f.). *Get started*. https://docs.docker.com/get-started/part1
- Docker. (s.f.). *Docker Compose overview*. https://docs.docker.com/compose/
- Politécnico Grancolombiano. (2017). *Máquinas virtuales y Dockers para construcción de ambientes*. Unidad 2, Escenario 3.
