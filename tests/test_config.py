from sqlalchemy.engine import make_url

from config import database_uri


def test_falls_back_to_sqlite(monkeypatch):
    monkeypatch.delenv("AZURE_POSTGRESQL_CONNECTIONSTRING", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert database_uri() == "sqlite:///notenrechner.db"


def test_uses_database_url(monkeypatch):
    monkeypatch.delenv("AZURE_POSTGRESQL_CONNECTIONSTRING", raising=False)
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg2://u:p@localhost/test")
    assert database_uri() == "postgresql+psycopg2://u:p@localhost/test"


def test_reads_azure_connection_string(monkeypatch):
    monkeypatch.setenv(
        "AZURE_POSTGRESQL_CONNECTIONSTRING",
        "dbname=noten host=db.example.com port=5432 sslmode=require "
        "user=admin password=a/b@c",
    )
    url = make_url(database_uri())
    assert url.host == "db.example.com"
    assert url.database == "noten"
    assert url.username == "admin"
    assert url.password == "a/b@c"
    assert url.query["sslmode"] == "require"
