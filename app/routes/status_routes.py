#routes pour l'état des capteurs

from fastapi import APIRouter, Depends, Header
from datetime import datetime
from app.models.auth import verify_token

router = APIRouter(prefix="/status", tags=["Status"])

@router.get("/{machine_id}")
def get_sensor_status(machine_id: int, token: str = Header(None)):
    verify_token(token)
    status = {
        "machine_id": machine_id,
        "battery": "80%",
        "connection": "OK",
        "last_update": datetime.utcnow()
    }
    return status