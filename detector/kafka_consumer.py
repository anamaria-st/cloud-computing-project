from kafka import KafkaConsumer
from database import guardar_evento, guardar_en_influx
import json
import os
import time

def start_kafka_consumer():
    consumer = None

    for intento in range(10):  # Reintenta 10 veces
        try:
            print(f"🔄 Intentando conectar con Kafka... intento {intento+1}/10")
            consumer = KafkaConsumer(
                'caidas',
                bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka:29092"),
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                auto_offset_reset='latest',
                group_id='fall-detector'
            )
            print("✅ Conexión establecida con Kafka.")
            break
        except Exception as e:
            print(f"❌ No se pudo conectar a Kafka: {e}")
            time.sleep(5)

    if consumer is None:
        print("💀 No se logró conectar a Kafka después de varios intentos.")
        return

    print("🟢 Escuchando eventos...")

    for message in consumer:
        data = message.value
        print(f"📥 Mensaje recibido: {data}")
        guardar_evento(data)
        guardar_en_influx(data)
