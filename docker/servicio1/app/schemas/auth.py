"""Pydantic schemas for authentication and user payloads."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegisterRequest(BaseModel):
    """Input schema for user registration."""

    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class UserLoginRequest(BaseModel):
    """Input schema for user login."""

    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class UserResponse(BaseModel):
    """User data returned by API endpoints."""

    id: int
    email: EmailStr
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    """Access token payload for authentication responses."""

    access_token: str
    token_type: str = "bearer"


class TokenValidationRequest(BaseModel):
    """Input schema for internal token validation requests."""

    token: str = Field(min_length=1)


class TokenValidationResponse(BaseModel):
    """Binary token validation result for internal service-to-service checks."""

    valid: bool
    detail: str | None = None
