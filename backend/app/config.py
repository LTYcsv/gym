from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str = ""
    SECRET_KEY: str = "dev-secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 720  # 12 часов
    ALLOWED_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:5174"]
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
