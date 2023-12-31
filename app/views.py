from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Features(BaseModel):
    feature_1: float
    feature_2: float

# Route for the POST method
@router.post('/predict')
async def predict(features: Features):
    return features