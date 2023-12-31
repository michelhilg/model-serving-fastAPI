from fastapi import APIRouter, HTTPException
from .api_models import Features, PredictionResponse
import datetime
import pytz
import joblib


router = APIRouter()

# Route for the POST method
@router.post('/predict', response_model=PredictionResponse)
async def predict(features: Features):

    current_time = datetime.datetime.now().isoformat()
    model = joblib.load("modelo.joblib")

    try:
        feature_1 = float(features.feature_1)
        feature_2 = float(features.feature_2)

        prediction = model.predict([[feature_1, feature_2]])[0]

        response = {
            "data": current_time,
            "predicao": round(prediction, 5),
            "id": 1#last_id
        }

        # Saving the success log
        #log(f"status: 200, id: {last_id}, data: {response['data']}, feature_1: {feature_1}, feature_2: {feature_2}, predição: {prediction}")

        return response

    except Exception as e:
        # Dealing with errors
        error_message = f"Request error: {str(e)}"

        # Saving the error log
        #log(f"status: 400, id: {last_id}, data: {current_time}, mensagem de erro: {error_message}")

        raise HTTPException(status_code=400, detail={"error": error_message})
