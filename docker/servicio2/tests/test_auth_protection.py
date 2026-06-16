"""Tests for token protection behavior in servicio2."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient


class _MockResponse:
    """Simple response stub for async HTTP calls."""

    def __init__(self, status_code: int, payload: dict[str, object]):
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict[str, object]:
        """Returns the mocked JSON body."""
        return self._payload


class _MockAsyncClient:
    """Async context manager stub for outbound HTTP requests."""

    post_response: _MockResponse = _MockResponse(200, {"valid": True})
    raise_on_post: bool = False

    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.get("timeout")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def post(self, *args, **kwargs):
        if self.raise_on_post:
            raise httpx.ConnectError("service unavailable")
        return self.post_response


@pytest.fixture
def client(monkeypatch) -> TestClient:
    """Provides a test client with patched HTTP client for token validation calls."""
    service2_dir = Path(__file__).resolve().parents[1]
    if str(service2_dir) not in sys.path:
        sys.path.insert(0, str(service2_dir))

    import main as servicio2_main

    importlib.reload(servicio2_main)
    monkeypatch.setattr(servicio2_main.httpx, "AsyncClient", _MockAsyncClient)
    with TestClient(servicio2_main.app) as test_client:
        yield test_client


def test_health_is_public(client: TestClient):
    """Health endpoint stays public and does not require a token."""
    response = client.get("/health")
    assert response.status_code == 200


def test_root_allows_access_with_valid_token(client: TestClient):
    """Protected root endpoint allows request when token is valid."""
    _MockAsyncClient.post_response = _MockResponse(200, {"valid": True})
    _MockAsyncClient.raise_on_post = False

    response = client.get("/", headers={"Authorization": "Bearer valid-token"})
    assert response.status_code == 200


def test_root_rejects_when_token_missing(client: TestClient):
    """Protected endpoint returns 401 if Authorization header is missing."""
    response = client.get("/")
    assert response.status_code == 401


def test_root_rejects_when_token_invalid(client: TestClient):
    """Protected endpoint returns 401 when servicio1 reports invalid token."""
    _MockAsyncClient.post_response = _MockResponse(200, {"valid": False, "detail": "invalid_or_expired_token"})
    _MockAsyncClient.raise_on_post = False

    response = client.get("/", headers={"Authorization": "Bearer invalid-token"})
    assert response.status_code == 401


def test_root_rejects_when_validation_service_unavailable(client: TestClient):
    """Protected endpoint fails closed with 401 when servicio1 is unavailable."""
    _MockAsyncClient.raise_on_post = True

    response = client.get("/", headers={"Authorization": "Bearer any-token"})
    assert response.status_code == 401

    _MockAsyncClient.raise_on_post = False
