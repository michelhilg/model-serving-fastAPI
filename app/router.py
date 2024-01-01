from fastapi import Depends, APIRouter, HTTPException
import datetime
import joblib
from config import get_settings
from sqlalchemy.orm import Session
from . import models, schemas
from database.database import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/prediction', 
             response_model=schemas.PredictionResponse, 
             tags=["Predictions"], 
             description="Handle a .JSON body request to return a .JSON with AI prediction.")
async def predict(features: schemas.Features, db: Session = Depends(get_db)):
    """
    Make predictions based on the provided features.

    :param features: Input features for prediction.
    :return: Prediction response.
    """

    current_time = datetime.datetime.now().isoformat()
    model = joblib.load(get_settings().path_model)

    try:
        prediction = model.predict([[features.feature_1, features.feature_2]])[0]

        pred = models.Prediction(feature_1=features.feature_1, feature_2=features.feature_1, predicao=prediction)
        db.add(pred)
        db.commit()

        response = {
            "data": current_time,
            "predicao": round(prediction, 5),
            "id": pred.id
        }

        return response
    
    except Exception as e:
        # Handling unexpected errors
        error_message = f"Unexpected error: {str(e)}"
        raise HTTPException(status_code=500, detail={"error": error_message})
