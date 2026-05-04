from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str = ""
    SECRET_KEY: str = "dev-secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200  # 30 дней

    class Config:
        env_file = ".env"


settings = Settings()
