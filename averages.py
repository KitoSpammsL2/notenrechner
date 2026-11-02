import math

from flask import Blueprint, render_template

bp = Blueprint("averages", __name__)


def weighted_average(grades):
    if not grades:
        return None
    return sum(value * weight for value, weight in grades) / sum(
        weight for _, weight in grades
    )


def round_to_half(value):
    return math.floor(value * 2 + 0.5) / 2


@bp.route("/schnitt")
def index():
    return render_template("averages.html")
