from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Development"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./db.sqlt3"
    log_path: str = "log/log.txt"
    path_model: str = "model/modelo.joblib"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings