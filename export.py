import csv
import io

from flask import Blueprint, Response

from database import db
from models import Grade, Subject

bp = Blueprint("export", __name__)


@bp.route("/export.csv")
def index():
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Fach", "Note", "Gewichtung"])
    grades = db.session.execute(
        db.select(Grade).join(Subject).order_by(Subject.name, Grade.id)
    ).scalars()
    for grade in grades:
        writer.writerow([grade.subject.name, grade.value, grade.weight])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=noten.csv"},
    )
