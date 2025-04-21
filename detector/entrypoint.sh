#!/bin/bash
set -e

echo "🕒 Esperando a que Kafka esté disponible..."

while ! nc -z kafka 29092; do
  echo "❌ Kafka no está listo, esperando 2 segundos..."
  sleep 2
done

echo "✅ Kafka está listo, arrancando la aplicación detector..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
