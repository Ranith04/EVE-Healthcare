from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    WEBHOOK_SECRET: str
    LOG_LEVEL: str
    PAYMENT_SIMULATION_MODE: str
    RATE_LIMIT_ENABLED: bool
    RATE_LIMIT_LOGIN: str
    RATE_LIMIT_PAYMENTS: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
