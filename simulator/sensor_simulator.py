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
            bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka:29092"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Kafka connection established")
        break
    except NoBrokersAvailable:
        print(f"Try {i+1}/10: Kafka is not available yet...")
        time.sleep(5)
else:
    print("Not possible to connect to Kafka after multiple tries")
    exit(1)

while True:
    if random.random() < 0.01:
        aceleracion = round(random.uniform(2.0, 3.0), 2)# fall simulation
    else:
        aceleracion = round(random.uniform(0.2, 1.9), 2)  

    evento = {
        "id": f"patient_{random.randint(1, 3)}",
        "timestamp": time.time(),
        "acceleration": aceleracion
    }

    producer.send('falls', evento)
    print(f"[✔️Sent] {evento}")
    time.sleep(1)

