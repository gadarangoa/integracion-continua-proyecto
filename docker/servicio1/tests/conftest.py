"""Test fixtures for servicio1 API tests."""

from __future__ import annotations

import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("DATABASE_URL", "sqlite:///./test_servicio1.db")
os.environ.setdefault("DB_INIT_ON_STARTUP", "false")
os.environ.setdefault("JWT_SECRET_KEY", "test-secret")
os.environ.setdefault("JWT_EXPIRE_MINUTES", "60")

from app.db.database import Base, SessionLocal, engine
from app.main import app


@pytest.fixture(autouse=True)
def reset_db() -> Generator[None, None, None]:
    """Recreates tables for each test for deterministic behavior."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        yield
    finally:
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """Provides an API client for tests."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def db_session() -> Generator:
    """Provides direct DB session access for test setup."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
