from pymongo import MongoClient
from influxdb import InfluxDBClient
import os

# --- MongoDB ---
mongo_client = MongoClient(os.getenv("MONGODB_URI", "mongodb://mongo:27017"))
db_mongo = mongo_client["caidas"]
coleccion = db_mongo["eventos"]

def guardar_evento(data):
    coleccion.insert_one(data)
    print("💾 Evento guardado en MongoDB")

# --- InfluxDB ---
influx_client = InfluxDBClient(
    host=os.getenv("INFLUXDB_HOST", "influxdb"),
    port=int(os.getenv("INFLUXDB_PORT", 8086))
)

influx_db_name = "caidas"
influx_client.create_database(influx_db_name)
influx_client.switch_database(influx_db_name)

def guardar_en_influx(data):
    punto = [{
        "measurement": "aceleracion",
        "tags": {
            "paciente": data["id"]
        },
        "fields": {
            "acceleration": float(data["acceleration"])
        },
        "time": int(data["timestamp"] * 1_000_000_000)  # nanosegundos
    }]
    influx_client.write_points(punto)
    print("📊 Evento guardado en InfluxDB")
