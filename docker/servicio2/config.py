"""Application settings for servicio2."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central settings object built from environment variables and .env files."""

    model_config = SettingsConfigDict(
        env_file=(".env", "docker/servicio2/.env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    servicio1_url: str = Field(default="http://contenedor1:3000", validation_alias="SERVICIO1_URL")
    servicio1_validate_token_url: str | None = Field(
        default=None,
        validation_alias="SERVICIO1_VALIDATE_TOKEN_URL",
    )
    servicio1_validate_timeout: float = Field(default=2.0, validation_alias="SERVICIO1_VALIDATE_TIMEOUT")

    @property
    def validate_token_url(self) -> str:
        """Returns explicit validation URL or builds it from servicio1_url."""
        if self.servicio1_validate_token_url:
            return self.servicio1_validate_token_url
        return f"{self.servicio1_url}/auth/validate-token"


settings = Settings()
