import os
import time
import random
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# Esperar antes de intentar conectar
time.sleep(10)

for i in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka:9092"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("✅ Conectado a Kafka")
        break
    except NoBrokersAvailable:
        print(f"⏳ Intento {i+1}/10: Kafka no disponible aún...")
        time.sleep(5)
else:
    print("❌ No se pudo conectar a Kafka después de varios intentos.")
    exit(1)

while True:
    evento = {
        "id": "paciente_01",
        "timestamp": time.time(),
        "acceleration": round(random.uniform(0.1, 1.2), 2)
    }
    producer.send('fall-data', evento)
    print(f"[✔️ Enviado] {evento}")
    time.sleep(1)
