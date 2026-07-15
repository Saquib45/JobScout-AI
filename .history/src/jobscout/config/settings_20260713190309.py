from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    email: str = ""
    email_password: str = ""

    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587

    check_interval: int = 24

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()