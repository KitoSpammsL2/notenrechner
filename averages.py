from flask import Blueprint, render_template

bp = Blueprint("averages", __name__)


@bp.route("/schnitt")
def index():
    return render_template("averages.html")
