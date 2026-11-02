import os

from sqlalchemy.engine import URL


def database_uri():
    """Liefert die Datenbank-Verbindung passend zur Umgebung."""
    azure = os.environ.get("AZURE_POSTGRESQL_CONNECTIONSTRING")
    if azure:
        parts = dict(part.split("=", 1) for part in azure.split())
        url = URL.create(
            "postgresql+psycopg2",
            username=parts["user"],
            password=parts["password"],
            host=parts["host"],
            port=int(parts.get("port", 5432)),
            database=parts["dbname"],
            query={"sslmode": parts.get("sslmode", "require")},
        )
        return url.render_as_string(hide_password=False)
    return os.environ.get("DATABASE_URL", "sqlite:///notenrechner.db")
