# test pour l'état des capteurs

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_sensor_status():
    response = client.get("/status/1", headers={"token": "invalid_token"})
    assert response.status_code == 401  # Vérifie qu'un token invalide est rejeté
