import paho.mqtt.client as mqtt
import json
import time
import random
import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "fastapi-mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC = "raw/data"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

for _ in range(5):
    payload = {
        "accelerometer": f"{random.uniform(-2, 2):.2f},{random.uniform(-2, 2):.2f},{random.uniform(-2, 2):.2f}",
        "gyroscope": f"{random.uniform(-180, 180):.2f},{random.uniform(-180, 180):.2f},{random.uniform(-180, 180):.2f}",
        "magnetometer": f"{random.uniform(-50, 50):.2f},{random.uniform(-50, 50):.2f},{random.uniform(-50, 50):.2f}"
    }

    print("Sending Raw Sensor Data:", payload)
    client.publish(TOPIC, json.dumps(payload))
    time.sleep(1)

client.disconnect()
