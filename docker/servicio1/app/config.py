"""Application settings and environment parsing."""

from __future__ import annotations

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central settings object built from environment variables and .env files."""

    model_config = SettingsConfigDict(
        env_file=(".env", "docker/servicio1/.env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Servicio 1"
    app_version: str = "1.0.0"
    app_description: str = "Microservicio 1 - Proyecto Integracion Continua"

    service2_url: str = Field(default="http://contenedor2:4000", validation_alias="SERVICIO2_URL")

    jwt_secret_key: SecretStr = Field(default=SecretStr("dev-secret-key"), validation_alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", validation_alias="JWT_ALGORITHM")
    jwt_expire_minutes: int = Field(default=30, validation_alias="JWT_EXPIRE_MINUTES")

    db_init_on_startup: bool = Field(default=True, validation_alias="DB_INIT_ON_STARTUP")
    db_create_database_if_missing: bool = Field(
        default=True,
        validation_alias="DB_CREATE_DATABASE_IF_MISSING",
    )

    database_url_raw: str | None = Field(default=None, validation_alias="DATABASE_URL")
    db_host: str | None = Field(default=None, validation_alias="DB_HOST")
    db_port: int | None = Field(default=None, validation_alias="DB_PORT")
    db_name: str | None = Field(default=None, validation_alias="DB_NAME")
    db_user: str | None = Field(default=None, validation_alias="DB_USER")
    db_password: SecretStr | None = Field(default=None, validation_alias="DB_PASSWORD")

    @property
    def database_url(self) -> str:
        """Builds DATABASE_URL from environment and validates required fields."""
        if self.database_url_raw:
            return self.database_url_raw

        required = {
            "DB_HOST": self.db_host,
            "DB_PORT": self.db_port,
            "DB_NAME": self.db_name,
            "DB_USER": self.db_user,
            "DB_PASSWORD": self.db_password.get_secret_value() if self.db_password else None,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            missing_list = ", ".join(missing)
            raise RuntimeError(
                "Missing required database variables: "
                f"{missing_list}. "
                "Set DATABASE_URL or DB_HOST/DB_PORT/DB_NAME/DB_USER/DB_PASSWORD."
            )

        return (
            f"postgresql+psycopg2://{required['DB_USER']}:{required['DB_PASSWORD']}"
            f"@{required['DB_HOST']}:{required['DB_PORT']}/{required['DB_NAME']}"
        )


settings = Settings()
