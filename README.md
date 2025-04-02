# 🏋️‍♂️ FitBuddy: FastAPI + MQTT + PostgreSQL in Docker

This project is a backend system for processing and storing movement data from connected fitness machines. It simulates receiving IoT sensor data, processes it via FastAPI, and stores it in PostgreSQL, all running inside Docker containers with MQTT integration.

---

## 📦 Features

- ⏱ Receives **sensor data** from IoT machines via MQTT (Mosquitto)
- 💾 Stores data in a **PostgreSQL** database (via Docker)
- ⚙️ Clean architecture using **FastAPI**, **SQLAlchemy**, and **Pydantic**
- 📊 Three dedicated tables:
  - `sensor_data` (repetitions, speed, etc.)
  - `asymmetry_data` (left/right side force, imbalance)
  - `sensor_status` (battery, firmware, health)
  - `raw_sensor_data` (accelerometer,gyroscope,magnetometer)
- 🐳 Containerized using **Docker + Docker Compose**
- ☁️ Prepares for **AWS migration** (API Gateway, RDS, IoT Core)

---


## 🚀 How to Run the Project Locally

### ✅ 1. Prerequisites

- Docker + Docker Compose installed
- Python 3.9+ 

---

### ✅ 2. Clone the Repository

```bash
git clone https://github.com/nassimlamnini/fitbuddy
cd fitbuddy
```

---

### ✅ 3. Launch Everything with Docker Compose
```bash
docker-compose up --build
```
After the build finishes, access the API docs here:

```bash
http://localhost:8000/docs
```
---

## Congratulations!

Now you have access to the FastAPI and you can run tests by launching the python files in tests folder

