from fastapi import APIRouter, HTTPException
from .api_models import Features, PredictionResponse
import datetime
import pytz
import joblib
from config import get_settings
from .extensions import setup_logging
import logging

router = APIRouter()
logger = setup_logging(get_settings().log_path)
last_id =1

# Configure logging to save messages to a file

@router.post('/predict', response_model=PredictionResponse)
async def predict(features: Features):

    current_time = datetime.datetime.now().isoformat()
    model = joblib.load(get_settings().path_model)

    try:
        feature_1 = float(features.feature_1)
        feature_2 = float(features.feature_2)

        prediction = model.predict([[feature_1, feature_2]])[0]

        response = {
            "data": current_time,
            "predicao": round(prediction, 5),
            "id": last_id
        }

        # Saving the success log
        logger.info(f"status: 200, id: {1}, feature_1: {feature_1}, feature_2: {feature_2}, predição: {prediction}")

        return response

    except ValueError as ve:
        # Handling value errors caused by invalid input data
        error_message = f" Incorrect Value: {str(ve)}"
        logger.error(f"status: 400, id: {last_id}, mensagem de erro: {error_message}")
        raise HTTPException(status_code=400, detail={"error": error_message})
    
    except Exception as e:
        # Handling unexpected errors
        error_message = f"Unexpected error: {str(e)}"
        logger.error(f"status: 500, id: {last_id}, mensagem de erro: {error_message}")
        raise HTTPException(status_code=500, detail={"error": error_message})
