from sqlalchemy.engine import make_url

from config import database_uri


def test_falls_back_to_sqlite(monkeypatch):
    monkeypatch.delenv("DBHOST", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert database_uri() == "sqlite:///notenrechner.db"


def test_uses_database_url(monkeypatch):
    monkeypatch.delenv("DBHOST", raising=False)
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://u:p@localhost/test")
    assert database_uri() == "postgresql+psycopg2://u:p@localhost/test"


def test_builds_azure_connection_from_settings(monkeypatch):
    monkeypatch.setenv("DBHOST", "db.example.com")
    monkeypatch.setenv("DBNAME", "noten")
    monkeypatch.setenv("DBUSER", "admin")
    monkeypatch.setenv("DBPASS", "a/b@c")
    url = make_url(database_uri())
    assert url.host == "db.example.com"
    assert url.database == "noten"
    assert url.username == "admin"
    assert url.password == "a/b@c"
    assert url.query["sslmode"] == "require"
