from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, services
from database import engine, get_db
import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv
from database import SessionLocal


load_dotenv()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    db = SessionLocal()

    if "repetitions" in data:  # Check if it's sensor data
        services.create_sensor_data(db, schemas.SensorDataCreate(**data))
    elif "battery_level" in data:  # Check if it's sensor status
        services.create_sensor_status(db, schemas.SensorStatusCreate(**data))
    elif "accelerometer" in data:  # Check if it's raw sensor data
        services.create_raw_sensor_data(db, schemas.RawSensorDataCreate(**data))
    db.close()
    print("MQTT Data Received:", data)

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe("sensor/data")
mqtt_client.subscribe("status/data")
mqtt_client.subscribe("raw/data")
mqtt_client.loop_start()

#sensor
@app.post("/sensor/", response_model=schemas.SensorDataResponse)
def create_sensor(data: schemas.SensorDataCreate, db: Session = Depends(get_db)):
    return services.create_sensor_data(db, data)

@app.get("/sensor/", response_model=list[schemas.SensorDataResponse])
def get_sensors(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return services.get_sensor_data(db, skip, limit)

#status
@app.post("/status/", response_model=schemas.SensorStatusResponse)
def create_status(data: schemas.SensorStatusCreate, db: Session = Depends(get_db)):
    return services.create_sensor_status(db, data)

@app.get("/status/", response_model=list[schemas.SensorStatusResponse])
def get_status(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return services.get_sensor_status(db, skip, limit)
#raw
@app.post("/raw/", response_model=schemas.RawSensorDataResponse)
def create_raw_data(data: schemas.RawSensorDataCreate, db: Session = Depends(get_db)):
    return services.create_raw_sensor_data(db, data)

@app.get("/raw/", response_model=list[schemas.RawSensorDataResponse])
def get_raw_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_raw_sensor_data(db, skip, limit)
