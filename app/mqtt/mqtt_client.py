# client mqtt pour recevoir les données
# but : simuler la reception des données du capteur
# Nous allons utiliser Mosquitto en local pour recevoir les messages MQTT comme AWS IoT Core.

import paho.mqtt.client as mqtt
import json
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, SensorData
from app.models.config import config

# Configuration du broker
MQTT_BROKER = config.MQTT_BROKER
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "fitbuddy/sensors"

def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    db: Session = SessionLocal()
    sensor_data = SensorData(**payload)
    db.add(sensor_data)
    db.commit()
    db.close()
    print(f"Données reçues et stockées : {payload}")

client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)
client.loop_start()
