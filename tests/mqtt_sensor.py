# test_mqtt_sensor_data.py
import paho.mqtt.client as mqtt
import json
import time
import random
import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "fastapi-mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC = "sensor/data"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

for _ in range(5):
    payload = {
        "repetitions": random.randint(5, 20),
        "duration": round(random.uniform(20.0, 30.0), 1),
        "difficulty": round(random.uniform(0.5, 2.0), 1),
        "speed": round(random.uniform(2.0, 5.0), 1),
        "amplitude": round(random.uniform(1.0, 3.0), 1),
        "left_side_force": round(random.uniform(10.0, 30.0), 2),
        "right_side_force": round(random.uniform(10.0, 30.0), 2),
        "imbalance_percentage": round(random.uniform(0.0, 10.0), 2)
    }

    print("Sending Sensor Data:", payload)
    client.publish(TOPIC, json.dumps(payload))
    time.sleep(1)

client.disconnect()
