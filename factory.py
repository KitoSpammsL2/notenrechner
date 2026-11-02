import os

from dotenv import load_dotenv
from flask import Flask

import averages
import export
import subjects
from config import database_uri
from database import db


def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri()
    app.config.update(test_config or {})

    db.init_app(app)
    app.register_blueprint(subjects.bp)
    app.register_blueprint(averages.bp)
    app.register_blueprint(export.bp)

    with app.app_context():
        db.create_all()

    return app
