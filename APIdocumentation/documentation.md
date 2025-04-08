# 📡 FitBuddy FastAPI – Sensor Data Collection API

This FastAPI project serves as the backend service for collecting and managing fitness sensor data from IoT devices, with MQTT integration, Dockerized deployment, and PostgreSQL support.

---

## 🔧 Architecture Overview

- **FastAPI** RESTful API for data processing  
- **AWS Lambda** for serverless API hosting
- **AWS API Gateway** for HTTP endpoints exposure
- **PostgreSQL (AWS RDS)** for persistent storage  
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

## ☁️ AWS Lambda Integration

### Why Serverless with AWS Lambda?

In this project, **AWS Lambda** was chosen to deploy the FastAPI application in a serverless architecture, in order to:

- **Eliminate server management**: No need to manage EC2 instances or Docker containers in production.
- **Enable automatic scaling**: Lambda scales automatically based on traffic load.
- **Pay-as-you-go**: Costs only incur when the function is invoked.
- **Simple API Exposure**: With **API Gateway**, it's straightforward to expose Lambda functions to the web.

### AWS Architecture Components

| Component                  | Description |
|---------------------------|-------------|
| **AWS Lambda**             | Runs the FastAPI app serverless. Entry point: `main.handler`. |
| **API Gateway**            | HTTP API that triggers the Lambda function upon request. |
| **RDS (PostgreSQL)**       | Cloud database storing sensor and status data. |
| **VPC**                    | Lambda is attached to the same Virtual Private Cloud as RDS to allow secure private communication. |
| **IAM Role**               | Lambda role with permissions to access network interfaces and CloudWatch logs. |
| **CloudWatch Logs**        | Monitoring and debugging of Lambda executions. |
| **MQTT Broker** (optional) | Still used for IoT data ingestion. |

### Execution Flow

1. **HTTP Request**  
   A user (or IoT device, or tester) sends an HTTP request to an API Gateway endpoint.

2. **API Gateway triggers Lambda**  
   API Gateway forwards the request to the Lambda function (`main.handler`).

3. **Lambda Executes FastAPI**  
   FastAPI processes the request, and depending on the route (`/sensor/`, `/status/`, `/raw/`), it performs validations and DB operations.

4. **Database Access via VPC**  
   Lambda securely connects to the PostgreSQL database in RDS using the VPC configuration to read/write data.

5. **Response to Client**  
   Lambda sends API response back through API Gateway.

6. **Logs available in CloudWatch**  
   Useful for monitoring and debugging.

### Lambda Configuration Details

- **Handler:** `main.handler`
- **Runtime:** Python 3.9
- **Environment Variables:**
  - `DATABASE_URL` : PostgreSQL connection string
  - `MQTT_BROKER` : MQTT broker IP
  - `MQTT_PORT` : MQTT broker port

- **Timeout:** 30s (HTTP API limitation)
- **Memory:** Adjustable depending on expected load
- **VPC Configuration:**
  - Subnets from the same VPC as RDS
  - Security Group allowing port 5432 access (Postgres)
- **IAM Role:**  
  Lambda uses a custom role with:
  - Basic Lambda execution permissions
  - VPC access permissions (CreateNetworkInterface, etc.)
- **Security:**
  - HTTPS enforced via API Gateway
  - RDS database access limited to Lambda
  - IAM roles follow principle of least privilege
  - TLS enabled on PostgreSQL connection (default AWS RDS)


### Security Best Practices

- API Gateway exposes only **HTTPS endpoints**.
- Lambda function runs in a **private VPC**, isolated from the public internet.
- **No public access** to RDS except from trusted sources (via security groups).
- **CloudWatch** enabled for monitoring.
- **IAM Role** restricts Lambda to only necessary permissions (`AWSLambdaBasicExecutionRole` + `EC2 network interface permissions`).
- Future improvement: add **API Key / Cognito Auth** for public endpoints.
- Future improvement: **CORS** configuration for web clients.


### Challenges and Solutions

| Challenge | Solution |
|-----------|-----------|
| Lambda could not connect to RDS | Attached Lambda to the same VPC and configured correct Security Groups (Ingress/Egress on port 5432). |
| "No log streams" error | Fixed by adding `AWSLambdaBasicExecutionRole` for CloudWatch logs. |
| API Gateway 404 / Not Found | Made sure that FastAPI paths match API Gateway routes, and re-deployed correctly with `serverless deploy`. |
| "Internal Server Error" | Debugged Lambda logs in CloudWatch to fix environment variables and connection handling. |
| CORS issues | Pending step: enable CORS in API Gateway for web clients. |

### Deployment Steps

1. Make sure `.env` is correctly configured locally:
   ```env
   DATABASE_URL=postgresql+psycopg2://username:password@host:port/dbname
   MQTT_BROKER=<broker-ip>
   MQTT_PORT=1883

2. Deploy to AWS:
```bash
serverless deploy
```

3. Monitor logs:
```bash
serverless logs -f app -s dev
```

4. Test endpoints
Create sensor data :
```bash
curl -X POST https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/sensor/ \
-H "Content-Type: application/json" \
-d '{
  "sensor_id": 1,
  "repetitions": 10,
  "duration": 60.5,
  "difficulty": 3.5,
  "speed": 1.2,
  "amplitude": 20.3,
  "left_side_force": 15.5,
  "right_side_force": 16.0,
  "imbalance_percentage": 2.5
}'

```

Get all sensor data
```bash
curl -X GET https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/sensor/
```

Create status data
```bash
curl -X POST https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/status/ \
-H "Content-Type: application/json" \
-d '{
  "sensor_id": 1,
  "battery_level": 87.5,
  "firmware_version": "1.2.3",
  "is_functional": true
}'

```

Get all status data
```bash
curl -X GET https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/status/
```

Create raw sensor data
```bash
curl -X GET https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/raw/ \
-H "Content-Type: application/json" \
-d '{
  "accelerometer": "0.01,0.02,0.03",
  "gyroscope": "0.05,0.06,0.07",
  "magnetometer": "0.09,0.10,0.11"
}'
```

Get all raw sensor data
```bash
curl -X GET https://87xm72mkca.execute-api.eu-north-1.amazonaws.com/raw/
```


### Benefits of Lambda for this project

- **Scalability:** automatic scaling without manual intervention.
- **Cost efficiency:** pay-per-use, ideal for IoT systems with irregular data loads.
- **Maintainability:** deploy new versions easily with Serverless.
- **Security:** isolated in VPC, integrates AWS IAM for access control.


---

## Future Integration
This API is designed to be queried by a mobile application (via NFC/QR scan), which retrieves:

-  Real-time status
-  Latest session metrics
-  Movement analysis (asymmetry)

