from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # MySQL Configuration
    # =========================
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_database: str = "jobscout_db"
    mysql_user: str = "root"
    mysql_password: str = ""

    # =========================
    # Email Configuration
    # =========================
    email: str = ""
    email_password: str = ""

    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587

    # =========================
    # Application Configuration
    # =========================
    check_interval: int = 24
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()