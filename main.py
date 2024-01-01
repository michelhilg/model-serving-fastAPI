from fastapi import FastAPI
from app.router import router as predict_router

app = FastAPI()

app.include_router(predict_router)







