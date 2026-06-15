"""Database engine, session, and metadata setup."""

from __future__ import annotations

import time

import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

DATABASE_URL = settings.database_url
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, future=True, echo=False, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Yields a database session for request handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def ensure_database_exists() -> None:
    """Creates the target PostgreSQL database when it does not exist yet."""
    parsed_url = make_url(DATABASE_URL)
    if not parsed_url.drivername.startswith("postgresql"):
        return

    target_database = parsed_url.database
    if not target_database:
        raise RuntimeError("PostgreSQL URL must include a database name")

    connection_params = {
        "host": parsed_url.host,
        "port": parsed_url.port or 5432,
        "user": parsed_url.username,
        "password": parsed_url.password,
        "dbname": "postgres",
    }
    sslmode = parsed_url.query.get("sslmode")
    if sslmode:
        connection_params["sslmode"] = sslmode

    last_error: Exception | None = None
    for _ in range(30):
        try:
            conn = psycopg2.connect(**connection_params)
            conn.autocommit = True
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (target_database,))
                    exists = cursor.fetchone() is not None
                    if not exists:
                        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(target_database)))
                return
            finally:
                conn.close()
        except psycopg2.OperationalError as exc:
            last_error = exc
            time.sleep(1)

    raise RuntimeError("Could not connect to PostgreSQL to bootstrap database") from last_error


def create_db_and_tables() -> None:
    """Creates database tables from SQLAlchemy metadata."""
    Base.metadata.create_all(bind=engine)
