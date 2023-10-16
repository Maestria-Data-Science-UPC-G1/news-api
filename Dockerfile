# Imagen base
FROM python:3.9-slim-buster

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
COPY app.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
