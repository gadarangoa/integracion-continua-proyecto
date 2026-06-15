"""Authentication business logic for users."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import UserLoginRequest, UserRegisterRequest
from app.services.security import hash_password, verify_password
from app.services.token_service import create_access_token


def get_user_by_email(db: Session, email: str) -> User | None:
    """Fetches a user by email address."""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, payload: UserRegisterRequest) -> User:
    """Creates a new user with a securely hashed password."""
    user = User(email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, payload: UserLoginRequest) -> str | None:
    """Validates credentials and returns an access token on success."""
    user = get_user_by_email(db, payload.email)
    if not user:
        return None
    if not verify_password(payload.password, user.password_hash):
        return None
    return create_access_token(str(user.id))
