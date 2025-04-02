# 📡 FitBuddy FastAPI – Sensor Data Collection API

This FastAPI project serves as the backend service for collecting and managing fitness sensor data from IoT devices, with MQTT integration, Dockerized deployment, and PostgreSQL support.

---

## 🔧 Architecture Overview

- **FastAPI** RESTful API for data processing  
- **PostgreSQL** for persistent storage  
- **Eclipse Mosquitto (MQTT)** for sensor data simulation  
- **Docker** for environment portability and orchestration  
- **pgAdmin / psql** for database inspection  
- **Swagger UI (`/docs`)** for API testing and live documentation  

---

## 📚 API Endpoints

### 🔹 `/sensor/` - Processed Sensor Data

| Method | Endpoint    | Description              |
|--------|-------------|--------------------------|
| `POST` | `/sensor/`  | Create new sensor record |
| `GET`  | `/sensor/`  | Retrieve sensor records  |

**Fields:**
- `repetitions`: int  
- `duration`: float  
- `difficulty`: float  
- `speed`: float  
- `amplitude`: float  

---

### 🔹 `/status/` - Sensor Status

| Method | Endpoint    | Description              |
|--------|-------------|--------------------------|
| `POST` | `/status/`  | Submit status of sensor  |
| `GET`  | `/status/`  | Fetch all statuses       |

**Fields:**
- `battery`: float  
- `connected`: bool  
- `errors`: Optional[str]  

---

### 🔹 `/asymmetry/` - Movement Asymmetry

| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| `POST` | `/asymmetry/`  | Submit asymmetry data    |
| `GET`  | `/asymmetry/`  | Get asymmetry history    |

**Fields:**
- `left`: float  
- `right`: float  
- `difference`: float  

---

### 🔹 `/raw/` - Raw Sensor Data

| Method | Endpoint | Description            |
|--------|----------|------------------------|
| `POST` | `/raw/`  | Insert raw sensor data |
| `GET`  | `/raw/`  | Fetch raw sensor logs  |

**Fields:**
- `accelerometer`: str  
- `gyroscope`: str  
- `magnetometer`: str  

---

## 🧪 Testing MQTT Integration

Simulate incoming data from MQTT using the scripts in `/tests/`:

- `mqtt_sensor.py`: sends processed data  
- `mqtt_status.py`: sends status data  
- `mqtt_asymmetry.py`: sends asymmetry metrics
- `mqtt_raw.py`: sends raw data

Make sure to install dependencies and run your local broker (`eclipse-mosquitto`) via Docker.

---

## 📦 Docker Stack

```bash
docker-compose up --build
```
### Services:

- fastapi-api - app logic
- fastapi-postgres - PostgreSQL 17 DB
- fastapi-mosquitto - MQTT broker
- pgAdmin (optional) - admin GUI

---

## 🗄 PostgreSQL Tables Overview
|Table Name             | Purpose                       |
|-----------------------|-------------------------------|
| raw_sensor_data       | Accelerometer, gyroscope, etc.|
| sensor_data	          | Processed data: reps, speed...|
| sensor_status	        | Battery, connectivity,...     |
| asymmetry_data        | Left vs. right differences    |

Each table includes:
-  id (Primary Key)
-  timestamp (datetime)

---

## Future Integration
This API is designed to be queried by a mobile application (via NFC/QR scan), which retrieves:

-  Real-time status
-  Latest session metrics
-  Movement analysis (asymmetry)

