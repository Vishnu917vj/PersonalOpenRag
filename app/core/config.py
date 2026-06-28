from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    # -------------------------
    # App
    # -------------------------
    APP_NAME: str = "OpenRAG"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # -------------------------
    # OpenRouter
    # -------------------------
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str = "openrouter/free"

    # -------------------------
    # Embedding Service
    # -------------------------
    EMBEDDING_API: str

    # -------------------------
    # Pinecone
    # -------------------------
    PINECONE_API_KEY: str
    PINECONE_INDEX: str
    PINECONE_CLOUD: str = "aws"
    PINECONE_REGION: str = "us-east-1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()