import math

from flask import Blueprint, flash, redirect, render_template, request, url_for

from database import db
from models import Grade, Subject

bp = Blueprint("subjects", __name__)


def parse_number(text):
    try:
        number = float(text.replace(",", "."))
    except ValueError:
        return None
    return number if math.isfinite(number) else None


@bp.route("/")
def index():
    subjects = Subject.query.order_by(Subject.name).all()
    return render_template("subjects.html", subjects=subjects)


@bp.route("/subjects", methods=["POST"])
def add_subject():
    name = request.form.get("name", "").strip()
    if not name or len(name) > 100:
        flash("Bitte gib einen Fachnamen mit höchstens 100 Zeichen ein.")
    elif Subject.query.filter_by(name=name).first():
        flash(f"Das Fach {name} gibt es schon.")
    else:
        db.session.add(Subject(name=name))
        db.session.commit()
    return redirect(url_for("subjects.index"))


@bp.route("/subjects/<int:subject_id>/grades", methods=["POST"])
def add_grade(subject_id):
    subject = db.get_or_404(Subject, subject_id)
    value = parse_number(request.form.get("value", ""))
    weight = parse_number(request.form.get("weight", ""))
    if value is None or not 1.0 <= value <= 6.0:
        flash("Die Note muss zwischen 1.0 und 6.0 liegen.")
    elif weight is None or weight <= 0:
        flash("Die Gewichtung muss grösser als 0 sein.")
    else:
        subject.grades.append(Grade(value=value, weight=weight))
        db.session.commit()
    return redirect(url_for("subjects.index"))
