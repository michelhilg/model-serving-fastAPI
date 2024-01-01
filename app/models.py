from database.database import Base
from sqlalchemy import Column, Integer, DateTime, Float
import datetime

class Prediction(Base):
    """Create the model for the prediction table in the database."""
    __tablename__ = "prediction"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), default=datetime.datetime.now())
    feature_1 = Column(Float, unique=False)
    feature_2 = Column(Float, unique=False)
    predicao = Column(Float, unique=False)
    