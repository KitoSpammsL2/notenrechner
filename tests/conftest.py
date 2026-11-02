import os

import pytest

from database import db
from factory import create_app


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": os.environ.get(
                "TEST_DATABASE_URL", "sqlite:///:memory:"
            ),
        }
    )
    with app.app_context():
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
