import paho.mqtt.client as mqtt
import json
import time
import random
import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "fastapi-mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC = "status/data"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

for _ in range(5):
    data = {
        "sensor_id": random.randint(1, 5),
        "battery_level": round(random.uniform(10.0, 100.0), 1),
        "firmware_version": "1.0.0",
        "is_functional": random.choice([True, False])
    }
    client.publish("status/data", json.dumps(data))
    print("Published Sensor Status:", data)
    time.sleep(1)

client.disconnect()
