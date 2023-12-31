from pydantic import BaseModel
from datetime import datetime

class PredictionResponse(BaseModel):
    data: datetime  
    predicao: float
    id: int  

class Features(BaseModel):
    feature_1: float
    feature_2: float
