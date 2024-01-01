from fastapi import FastAPI
from app.views import router as predict_router

app = FastAPI()

app.include_router(predict_router)







