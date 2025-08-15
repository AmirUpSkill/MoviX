# Configuration module for application settings

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Manages application settings using Pydantic.
    Loads environment variables from .env file and system environment.
    """
    # Database settings
    DATABASE_URL: str  # PostgreSQL connection string

    # Pydantic configuration
    model_config = SettingsConfigDict(env_file=".env")  # Load settings from .env file

# Global settings instance
settings = Settings()
