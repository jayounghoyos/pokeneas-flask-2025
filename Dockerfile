FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer puerto 5000
EXPOSE 5000

# Variables de entorno por defecto
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]