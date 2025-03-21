#routes pour l'authentification

from fastapi import APIRouter, HTTPException, Header
from app.models.auth import create_jwt_token, verify_token
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

# Modèle de requête pour l'authentification
class AuthRequest(BaseModel):
    device_id: str
    password: str

# Liste des Raspberry Pi autorisés (peut être remplacée par une base de données)
AUTHORIZED_DEVICES = {"raspberry1": "password123", "raspberry2": "securepass"}

@router.post("/login")
def login(auth: AuthRequest):
    if auth.device_id in AUTHORIZED_DEVICES and AUTHORIZED_DEVICES[auth.device_id] == auth.password:
        return {"token": create_jwt_token(auth.device_id)}
    raise HTTPException(status_code=403, detail="Identifiants invalides")