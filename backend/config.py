from functools import lru_cache
from pathlib import Path
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application settings
    APP_NAME: str = "ScholarX Backend"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    OFFLINE_MODE: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    SESSION_SECRET: str = ""
    CORS_ORIGINS: str = ""

    # === Gemini API Configuration (Multi-Key) ===
    GEMINI_API_KEY_1: str = ""
    GEMINI_API_KEY_2: str = ""
    GEMINI_API_KEY_3: str = ""
    GEMINI_PRIMARY_MODEL: str = "gemini-flash-latest"
    GEMINI_FALLBACK_MODEL: str = "gemini-flash-latest"

    # === Groq API Configuration (Multi-Key) ===
    GROQ_API_KEY_1: str = ""
    GROQ_API_KEY_2: str = ""
    GROQ_API_KEY_3: str = ""
    GROQ_API_KEY_4: str = ""
    GROQ_API_KEY_5: str = ""
    GROQ_API_KEY_6: str = ""
    GROQ_API_KEY_7: str = ""
    GROQ_API_KEY_8: str = ""
    GROQ_API_KEY_9: str = ""
    GROQ_API_KEY_10: str = ""
    GROQ_API_KEY_11: str = ""
    GROQ_API_KEY_12: str = ""
    GROQ_API_KEY_13: str = ""
    GROQ_MODEL: str = "qwen/qwen3.8-27b"

    # === Tavily Search Configuration (Multi-Key) ===
    TAVILY_API_KEY_1: str = ""
    TAVILY_API_KEY_2: str = ""
    TAVILY_API_KEY_3: str = ""
    TAVILY_API_KEY_4: str = ""
    TAVILY_API_KEY_5: str = ""
    TAVILY_API_KEY_6: str = ""
    TAVILY_API_KEY_7: str = ""

    # === Firecrawl Configuration (Multi-Key) ===
    FIRECRAWL_API_KEY_1: str = ""
    FIRECRAWL_API_KEY_2: str = ""
    FIRECRAWL_API_KEY_3: str = ""
    FIRECRAWL_API_KEY_4: str = ""
    FIRECRAWL_API_KEY_5: str = ""
    FIRECRAWL_API_KEY_6: str = ""

    # === Jina Reader Configuration ===
    JINA_API_KEY: str = ""

    # === Local Database Settings ===
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "scholarx"
    POSTGRES_USER: str = "scholarx"
    POSTGRES_PASSWORD: str = "scholarx_local"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    CHROMADB_HOST: str = "localhost"
    CHROMADB_PORT: int = 8100

    SESSION_DB_PATH: str = str(DATA_DIR / "scholarx_sessions.db")

    @property
    def gemini_keys(self) -> List[str]:
        keys = [self.GEMINI_API_KEY_1, self.GEMINI_API_KEY_2, self.GEMINI_API_KEY_3]
        return [k.strip() for k in keys if k and k.strip() and not k.startswith("your_")]

    @property
    def groq_keys(self) -> List[str]:
        keys = [
            self.GROQ_API_KEY_1,
            self.GROQ_API_KEY_2,
            self.GROQ_API_KEY_3,
            self.GROQ_API_KEY_4,
            self.GROQ_API_KEY_5,
            self.GROQ_API_KEY_6,
            self.GROQ_API_KEY_7,
            self.GROQ_API_KEY_8,
            self.GROQ_API_KEY_9,
            self.GROQ_API_KEY_10,
            self.GROQ_API_KEY_11,
            self.GROQ_API_KEY_12,
            self.GROQ_API_KEY_13,
        ]
        return [k.strip() for k in keys if k and k.strip() and not k.startswith("your_")]

    @property
    def tavily_keys(self) -> List[str]:
        keys = [
            self.TAVILY_API_KEY_1,
            self.TAVILY_API_KEY_2,
            self.TAVILY_API_KEY_3,
            self.TAVILY_API_KEY_4,
            self.TAVILY_API_KEY_5,
            self.TAVILY_API_KEY_6,
            self.TAVILY_API_KEY_7,
        ]
        return [k.strip() for k in keys if k and k.strip() and not k.startswith("your_")]

    @property
    def firecrawl_keys(self) -> List[str]:
        keys = [
            self.FIRECRAWL_API_KEY_1,
            self.FIRECRAWL_API_KEY_2,
            self.FIRECRAWL_API_KEY_3,
            self.FIRECRAWL_API_KEY_4,
            self.FIRECRAWL_API_KEY_5,
            self.FIRECRAWL_API_KEY_6,
        ]
        return [k.strip() for k in keys if k and k.strip() and not k.startswith("your_")]

    def validate_startup_configuration(self) -> None:
        """
        Validates configuration consistency and warns or raises in production.
        """
        import logging
        cfg_logger = logging.getLogger("scholarx.config")
        if not (self.gemini_keys or self.groq_keys):
            msg = "ScholarX running without external LLM keys. Offline mode active."
            if self.ENVIRONMENT == "production" and not self.OFFLINE_MODE:
                raise ValueError(f"FATAL: {msg}")
            else:
                cfg_logger.info(f"Configuration notice: {msg}. Operating with deterministic offline intelligence.")

        if not self.SESSION_SECRET:
            if self.ENVIRONMENT == "production":
                raise ValueError("FATAL: SESSION_SECRET must be set in production environment.")
            else:
                cfg_logger.info("Using auto-generated ephemeral session signing secret for development.")

@lru_cache()
def get_settings() -> Settings:
    return Settings()
