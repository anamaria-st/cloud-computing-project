FROM python:3.11-slim

# 1. Instala netcat para esperar Kafka
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# 2. Crea carpeta de trabajo
WORKDIR /app

# 3. Copia todo el código
COPY . /app

# 4. Instala dependencias
RUN pip install --no-cache-dir fastapi uvicorn kafka-python pymongo influxdb twilio

# 5. Da permisos de ejecución al script de arranque
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

# 7. Comando por defecto (pero lo va a ejecutar el entrypoint)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
