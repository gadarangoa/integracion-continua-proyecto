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
├── docs/
│   └── entrega1/
├── docker/
│   ├── servicio1/
│   │   └── Dockerfile
│   └── servicio2/
│       └── Dockerfile
```

---

## 🚀 Entregas

### Entrega 1 - Semana 3
- [ ] Proyecto creado en GitHub
- [ ] Construcción de dos contenedores Docker
- [ ] Comunicación entre contenedores

### Entrega 2 - Semana 5
- [ ] Implementación de Jenkins como gestor de operaciones
- [ ] Documento con características de la implementación

### Entrega 3 y Sustentación - Semanas 7 y 8
- [ ] Integración completa con contenedores, Jenkins, Travis CI y Codeship
- [ ] Historial de cambios consolidado
- [ ] Documento con responsabilidades y conclusiones

---

## 🐳 Cómo levantar los contenedores (Entrega 1)

```bash
# Construir imagen servicio 1
docker build -t servicio1 ./docker/servicio1

# Construir imagen servicio 2
docker build -t servicio2 ./docker/servicio2

# Verificar contenedores activos
docker ps
```

---

## 👥 Integrantes

| Nombre | GitHub |
|--------|--------|
| (Pendiente) | - |

---

## 📚 Referencias

- Docker. (s.f.). *Get started*. https://docs.docker.com/get-started/part1
- Politécnico Grancolombiano. (2017). *Máquinas virtuales y Dockers para construcción de ambientes*. Unidad 2, Escenario 3.
