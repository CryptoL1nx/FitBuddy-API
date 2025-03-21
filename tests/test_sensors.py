#tests pour la réception des capteurs

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def valid_token():
    response = client.post("/auth/login", json={"device_id": "raspberry1", "password": "password123"})
    return response.json()["token"]

def test_send_sensor_data(valid_token):
    response = client.post("/data/", 
                           json={
                               "machine_id": 1, 
                               "timestamp": "2025-03-18T14:30:00Z", 
                               "acceleration_x": 1.2, 
                               "acceleration_y": 0.5, 
                               "acceleration_z": -9.81, 
                               "repetitions": 10, 
                               "series_time": 30.5, 
                               "rest_time": 60.0
                           },
                           headers={"token": valid_token})
    assert response.status_code == 200
    assert response.json()["message"] == "Données reçues"
