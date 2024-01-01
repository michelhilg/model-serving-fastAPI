from pydantic import BaseModel
from datetime import datetime

class PredictionResponse(BaseModel):
    """Define the model for the prediction response .JSON"""
    data: datetime  
    predicao: float
    id: int  

class Features(BaseModel):
    """Define the model for the features .JSON body"""
    feature_1: float
    feature_2: float
    