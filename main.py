from fastapi import FastAPI
from app.views import router as predict_router 

app = FastAPI()

# Include routes from views
app.include_router(predict_router)
