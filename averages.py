import math

from flask import Blueprint, render_template

from models import Subject

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
    subject_averages = []
    rounded_averages = []
    for subject in Subject.query.order_by(Subject.name).all():
        average = weighted_average(
            [(grade.value, grade.weight) for grade in subject.grades]
        )
        rounded = round_to_half(average) if average is not None else None
        subject_averages.append((subject.name, rounded))
        if rounded is not None:
            rounded_averages.append(rounded)

    overall_average = (
        sum(rounded_averages) / len(rounded_averages) if rounded_averages else None
    )
    return render_template(
        "averages.html",
        subject_averages=subject_averages,
        overall_average=overall_average,
    )
