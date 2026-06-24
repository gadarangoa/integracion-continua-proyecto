"""Unit tests for auth and health endpoints."""

from __future__ import annotations


def test_health_ok(client):
    """Health endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_login_returns_token(client):
    """Valid credentials produce a bearer token."""
    register_response = client.post(
        "/auth/register",
        json={"email": "user1@example.com", "password": "secret123"},
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/auth/login",
        json={"email": "user1@example.com", "password": "secret123"},
    )
    assert login_response.status_code == 200
    body = login_response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_protected_endpoint_with_valid_token(client):
    """Authenticated user can access /auth/me with valid token."""
    client.post("/auth/register", json={"email": "user2@example.com", "password": "secret123"})
    login_response = client.post(
        "/auth/login",
        json={"email": "user2@example.com", "password": "secret123"},
    )
    token = login_response.json()["access_token"]

    me_response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "user2@example.com"


def test_protected_endpoint_with_invalid_or_missing_token(client):
    """Protected endpoint rejects missing or invalid tokens."""
    missing_token_response = client.get("/auth/me")
    assert missing_token_response.status_code == 401

    invalid_token_response = client.get(
        "/auth/me",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert invalid_token_response.status_code == 401


def test_login_invalid_credentials_returns_401(client):
    """Login with invalid credentials must return unauthorized."""
    client.post("/auth/register", json={"email": "user3@example.com", "password": "secret123"})
    response = client.post(
        "/auth/login",
        json={"email": "user3@example.com", "password": "wrong-password"},
    )
    assert response.status_code == 401


def test_register_duplicate_email_returns_conflict(client):
    """Registering an existing email returns conflict error."""
    payload = {"email": "user4@example.com", "password": "secret123"}
    first = client.post("/auth/register", json=payload)
    second = client.post("/auth/register", json=payload)
    assert first.status_code == 201
    assert second.status_code == 409
