from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import joblib
import pytz

app = FastAPI()

# Loading the model
model = joblib.load("modelo.joblib")

# Set the desired timezone to São Paulo
desired_timezone = 'America/Sao_Paulo'

# Function to further connect to the database

# Define the file and function for dealing with the logs
log_filename = "log.txt"
def log(data):
    with open(log_filename, "a") as log_file:
        log_file.write(data + "\n")

# CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

last_id = 1

# Route for the POST method
@app.post('/predict')
def predict(request_data: dict):

    # Update the last id (using the auto-increment from SQLite)

    # Get the current time in São Paulo timezone in isoformat
    current_time = datetime.datetime.now(pytz.timezone(desired_timezone)).isoformat()

    try:
        # Request data
        feature_1 = float(request_data['feature_1'])
        feature_2 = float(request_data['feature_2'])

        # Model prediction
        prediction = model.predict([[feature_1, feature_2]])[0]

        # Generating the JSON response
        response = {
            "data": current_time,
            "predicao": round(prediction, 5),
            "id": 1#last_id
        }

        # Saving the success log
        log(f"status: 200, id: {last_id}, data: {response['data']}, feature_1: {feature_1}, feature_2: {feature_2}, predição: {prediction}")

        return response

    except Exception as e:
        # Dealing with errors
        error_message = f"Request error: {str(e)}"

        # Saving the error log
        log(f"status: 400, id: {last_id}, data: {current_time}, mensagem de erro: {error_message}")

        raise HTTPException(status_code=400, detail={"error": error_message})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)