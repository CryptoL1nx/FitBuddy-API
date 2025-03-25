from sqlalchemy import create_engine, Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models.config import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, index=True)
    timestamp = Column(DateTime)
    acceleration_x = Column(Float)
    acceleration_y = Column(Float)
    acceleration_z = Column(Float)
    repetitions = Column(Integer)
    series_time = Column(Float)
    rest_time = Column(Float)
    asymmetry = Column(Float, nullable=True) 

Base.metadata.create_all(bind=engine)
