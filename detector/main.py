from fastapi import FastAPI
from kafka_consumer import start_kafka_consumer
import threading

app = FastAPI()

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_kafka_consumer)
    thread.daemon = True
    thread.start()
