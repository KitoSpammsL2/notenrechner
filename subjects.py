from flask import Blueprint, render_template

from models import Subject

bp = Blueprint("subjects", __name__)


@bp.route("/")
def index():
    subjects = Subject.query.order_by(Subject.name).all()
    return render_template("subjects.html", subjects=subjects)
