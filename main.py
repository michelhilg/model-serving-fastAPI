from fastapi import FastAPI
from app.router import router as predict_router

# Create an instance of the FastAPI application

app = FastAPI()

app.include_router(predict_router)
