from flask import Blueprint, Response

bp = Blueprint("export", __name__)


@bp.route("/export.csv")
def index():
    return Response(
        "Fach,Note,Gewichtung\n",
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=noten.csv"},
    )
