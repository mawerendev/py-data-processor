# 1. Imagen base oficial de Python ligera
FROM python:3.11-slim

# 2. Configurar variables de entorno para evitar búferes de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar e instalar dependencias primero (aprovecha la caché de capas de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código fuente al contenedor
COPY . .

# 6. Exponer el puerto del servidor web
EXPOSE 8000

# 7. Ejecutar FastAPI con Uvicorn escuchando en todas las interfaces de red (0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]