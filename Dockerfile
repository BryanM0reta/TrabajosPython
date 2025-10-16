# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Instala dependencias (si tienes un archivo requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando por defecto para ejecutar tu aplicación
# (reemplaza "main.py" por el nombre de tu script principal)
CMD ["python", "main.py"]
