import os

from sqlalchemy.engine import URL


def database_uri():
    """Liefert die Datenbank-Verbindung passend zur Umgebung."""
    host = os.environ.get("DBHOST")
    if host:
        url = URL.create(
            "postgresql+psycopg2",
            username=os.environ["DBUSER"],
            password=os.environ["DBPASS"],
            host=host,
            database=os.environ["DBNAME"],
            query={"sslmode": "require"},
        )
        return url.render_as_string(hide_password=False)
    return os.environ.get("DATABASE_URL", "sqlite:///notenrechner.db")
