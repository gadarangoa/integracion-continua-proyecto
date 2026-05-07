# Servicio 2 - (definir tipo de servicio)
# Imagen base
FROM ubuntu:22.04

# Mantenedor
LABEL maintainer="gadarangoa"

# Actualizar paquetes
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Puerto expuesto
EXPOSE 4000

# Comando por defecto
CMD ["bash"]
