from kafka import KafkaConsumer
from alert import enviar_alerta_correo, enviar_alerta_sms
from database import save_event, save_influx
import json
import os
import time

def start_kafka_consumer():
    consumer = None

    for intento in range(10):  # Reintenta 10 veces
        try:
            print(f"🔄 Trying to connect to Kafka: {intento+1}/10")
            consumer = KafkaConsumer(
                'falls',
                bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka:29092"),
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                auto_offset_reset='latest',
                group_id='fall-detector'
            )
            print("✅ Kafka connection established")
            break
        except Exception as e:
            print(f"❌ Is not possible to connect to Kafka: {e}")
            time.sleep(5)

    if consumer is None:
        print("Connection to Kafka failed after multiple tries")
        return

    print("🟢 Listening events...")

    for message in consumer:
        data = message.value
        print(f"📥 Message received: {data}")
        save_event(data)
        save_influx(data)
        
        if float(data["acceleration"]) > 2.0:
            print("🚨 Fall detected, sending SMS alert...")
            enviar_alerta_correo(data["id"], data["acceleration"])
            enviar_alerta_sms(data["id"], data["acceleration"])
