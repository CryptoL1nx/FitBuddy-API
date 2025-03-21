#point d'entrée de l'API FastAPI

from fastapi import FastAPI
from app.routes import auth_routes, sensor_routes, status_routes

app = FastAPI(title="Fit Buddy API", description="API pour la collecte des données des capteurs", version="1.0.0")

# Inclusion des routes
tags_metadata = [
    {"name": "Auth", "description": "Authentification des Raspberry Pi"},
    {"name": "Sensors", "description": "Collecte des données des capteurs"},
    {"name": "Status", "description": "État et diagnostic des capteurs"}
]

app.include_router(auth_routes.router, tags=["Auth"])
app.include_router(sensor_routes.router, tags=["Sensors"])
app.include_router(status_routes.router, tags=["Status"])