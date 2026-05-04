from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str = ""
    SECRET_KEY: str = "dev-secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 720
    ALLOWED_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:5174", "http://localhost:5175"]
    FRONTEND_URL: str | None = None  # устанавливается на Railway → Vercel URL
    DEBUG: bool = False

    @field_validator("DATABASE_URL")
    @classmethod
    def fix_db_url(cls, v: str) -> str:
        # Railway даёт postgres:// или postgresql:// — приводим к postgresql+psycopg://
        if v.startswith("postgres://"):
            return v.replace("postgres://", "postgresql+psycopg://", 1)
        if v.startswith("postgresql://"):
            return v.replace("postgresql://", "postgresql+psycopg://", 1)
        return v

    @property
    def cors_origins(self) -> list[str]:
        origins = list(self.ALLOWED_ORIGINS)
        if self.FRONTEND_URL:
            origins.append(self.FRONTEND_URL)
        return origins

    class Config:
        env_file = ".env"


settings = Settings()
