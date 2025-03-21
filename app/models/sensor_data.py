#Définition des modèles de données

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorData(BaseModel):
    machine_id: int
    timestamp: datetime
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    repetitions: int
    series_time: float
    rest_time: float
    asymmetry: Optional[float] = None