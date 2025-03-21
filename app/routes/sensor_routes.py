#routes pour les données capteurs

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, SensorData
from app.models.auth import verify_token
from app.models.sensor_data import SensorData as SensorDataModel

router = APIRouter(prefix="/data", tags=["Sensors"])

# Dépendance pour récupérer la session PostgreSQL
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def receive_data(sensor_data: SensorDataModel, token: str = Header(None), db: Session = Depends(get_db)):
    device_id = verify_token(token)
    db_entry = SensorData(**sensor_data.dict())
    db.add(db_entry)
    db.commit()
    return {"message": "Données stockées dans AWS RDS", "device": device_id}
