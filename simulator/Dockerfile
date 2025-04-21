FROM python:3.11-slim

WORKDIR /app

COPY sensor_simulator.py .

RUN pip install kafka-python

CMD ["python", "sensor_simulator.py"]
