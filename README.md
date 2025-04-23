# 🧠 Real-Time Fall Detection System – Cloud Computing Project

This project implements a real-time fall detection system using simulated IoT sensor data. The system detects possible falls and sends alerts via email and SMS. It is fully deployed on a Google Cloud **Compute Engine** virtual machine using Docker and multiple containers.

## 🏗️ System Architecture

- **Sensor Simulator**: Sends JSON-formatted acceleration data to Kafka.
- **Kafka + Zookeeper**: Handles message delivery and coordination.
- **FastAPI Fall Detector**: Analyzes the incoming data to detect falls using rule-based logic.
- **MongoDB**: Stores structured alert/event data.
- **InfluxDB + Grafana**: Stores and visualizes time-series sensor data in real time.
- **Twilio / SMTP**: Sends alerts to caregivers via SMS and email.
- **Google Cloud VM**: All services run on a single virtual machine using Docker Compose.

## 📦 Technologies Used

- **Python 3.11**
- **FastAPI**
- **Kafka + Zookeeper**
- **MongoDB**
- **InfluxDB**
- **Grafana**
- **Docker & Docker Compose**
- **Twilio API** and **SMTP for email**
- **Google Cloud Platform (GCP)**

## 🚀 Deployment

To deploy locally or on a VM:

```bash
git clone https://github.com/anamaria-st/cloud-computing-project.git
cd cloud-computing-project
docker-compose up --build
