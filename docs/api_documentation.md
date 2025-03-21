# Documentation API

## Raspberry Pi
Le Raspberry PI envoie les données au cloud via MQTT/AWS IoT Core
__Il faut installer requests sur le Raspberry Pi__
```sh
pip install requests
```
__Puis il faut utiliser ce script sur le RaspPi :__
```python
import requests
import json
from datetime import datetime

# URL de ton API hébergée sur AWS
API_URL = "https://your-api-gateway-url.execute-api.your-region.amazonaws.com/prod/data"

# Récupérer un token JWT
auth_response = requests.post("https://your-api-gateway-url.execute-api.your-region.amazonaws.com/prod/auth/login", json={"device_id": "raspberry1", "password": "password123"})
token = auth_response.json()["token"]

# Simuler des données capteurs
sensor_data = {
    "machine_id": 1,
    "timestamp": datetime.utcnow().isoformat(),
    "acceleration_x": 1.2,
    "acceleration_y": 0.5,
    "acceleration_z": -9.81,
    "repetitions": 10,
    "series_time": 30.5,
    "rest_time": 60.0
}

# Envoyer les données à l’API
headers = {"token": token, "Content-Type": "application/json"}
response = requests.post(API_URL, json=sensor_data, headers=headers)

print(response.status_code, response.json())

```


## Base de donnée
Les données sont stockées dans une base de données PostgreSQL sur AWS RDS/Aurora
Check out les docs :
* config.py
* database.py
* sensor_routes.py pour le stockage des données dans RDS

## API RESTful
Une API RESTful est une interface qui permet à des applications de communiquer entre elles via le protocole HTTP, en respectant les principes REST (Representational State Transfer).
#### 💡 Exemple de flux de requête API :
1️⃣ Un utilisateur envoie une requête HTTP (GET /users) à API Gateway.
2️⃣ API Gateway reçoit la requête et applique des règles (authentification, logs, etc.).
3️⃣ Il transmet la requête au backend (ex. : une fonction AWS Lambda ou une base de données).
4️⃣ Le backend traite la requête et renvoie une réponse à API Gateway.
5️⃣ API Gateway envoie la réponse finale à l’utilisateur.

## Sécuriser l'API (à faire encore)
1️⃣ Activer HTTPS avec un certificat SSL sur AWS
--> Utiliser AWS Certificate Manager (ACM) et API Gateway pour sécuriser l’API avec HTTPS.
2️⃣ Protéger PostgreSQL avec les IAM Roles
--> Limiter l’accès à ton API uniquement avec un VPC privé.
3️⃣ Ajouter JWT pour protéger les requêtes
--> Chaque Raspberry Pi doit utiliser un token JWT pour envoyer les données.