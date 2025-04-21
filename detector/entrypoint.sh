#!/bin/bash
set -e

echo "🕒 Waiting for Kafka to be available..."

while ! nc -z kafka 29092; do
  echo "❌ Kafka is not ready, waiting for 2s..."
  sleep 2
done

echo "✅ Kafka is ready, statrting Detector..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
