from sqlalchemy.orm import Session
import models, schemas

def create_sensor_data(db: Session, data: schemas.SensorDataCreate):
    sensor_data = models.SensorData(**data.dict())
    db.add(sensor_data)
    db.commit()
    db.refresh(sensor_data)
    return sensor_data

def get_sensor_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SensorData).offset(skip).limit(limit).all()


def create_sensor_status(db: Session, data: schemas.SensorStatusCreate):
    sensor_status = models.SensorStatus(**data.dict())
    db.add(sensor_status)
    db.commit()
    db.refresh(sensor_status)
    return sensor_status

def get_sensor_status(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SensorStatus).offset(skip).limit(limit).all()

def create_raw_sensor_data(db: Session, data: schemas.RawSensorDataCreate):
    raw_data = models.RawSensorData(**data.dict())
    db.add(raw_data)
    db.commit()
    db.refresh(raw_data)
    return raw_data

def get_raw_sensor_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.RawSensorData).offset(skip).limit(limit).all()
