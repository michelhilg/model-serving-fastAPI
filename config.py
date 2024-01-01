from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuration settings for the application via .env file and backup via setting class."""
    env_name: str = "Development"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./db.sqlt3"
    log_path: str = "log/log.txt"
    path_model: str = "model/modelo.joblib"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    """
    Get the application settings.

    Returns:
        Settings: An instance of the Settings class containing the application configuration.
    """
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
