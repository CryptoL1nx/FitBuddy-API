#tests unitaires pour l'authentification

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_valid():
    response = client.post("/auth/login", json={"device_id": "raspberry1", "password": "password123"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_invalid():
    response = client.post("/auth/login", json={"device_id": "raspberry1", "password": "wrongpassword"})
    assert response.status_code == 403
