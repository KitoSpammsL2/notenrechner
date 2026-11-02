import pytest

from averages import round_to_half, weighted_average
from database import db
from models import Grade, Subject


def test_weighted_average():
    result = weighted_average([(5.0, 1.0), (4.0, 2.0)])
    assert result == pytest.approx(4.33, abs=0.005)


def test_weighted_average_without_grades():
    assert weighted_average([]) is None


@pytest.mark.parametrize("value, expected", [(4.25, 4.5), (4.24, 4.0), (5.75, 6.0)])
def test_round_to_half(value, expected):
    assert round_to_half(value) == expected


def test_schnitt_shows_rounded_subject_averages_and_overall(client, app):
    mathematics = Subject(name="Mathematik")
    mathematics.grades.extend(
        [Grade(value=5.0, weight=1.0), Grade(value=4.0, weight=2.0)]
    )
    english = Subject(name="Englisch")
    english.grades.append(Grade(value=5.75, weight=1.0))
    db.session.add_all([mathematics, english])
    db.session.commit()

    response = client.get("/schnitt")
    assert response.status_code == 200
    page = " ".join(response.get_data(as_text=True).split())
    assert "<td>Mathematik</td> <td>4.5</td>" in page
    assert "<td>Englisch</td> <td>6.0</td>" in page
    # The overall average uses the rounded subjects: (4.5 + 6.0) / 2.
    assert "Gesamtschnitt: 5.25" in page


def test_schnitt_excludes_subject_without_grades_from_overall(client, app):
    mathematics = Subject(name="Mathematik")
    mathematics.grades.append(Grade(value=5.0, weight=1.0))
    db.session.add_all([mathematics, Subject(name="Sport")])
    db.session.commit()

    page = " ".join(client.get("/schnitt").get_data(as_text=True).split())
    assert "<td>Sport</td> <td>–</td>" in page
    assert "Gesamtschnitt: 5.00" in page


@pytest.mark.parametrize("with_empty_subject", [False, True])
def test_schnitt_without_any_grades(client, app, with_empty_subject):
    if with_empty_subject:
        db.session.add(Subject(name="Sport"))
        db.session.commit()

    response = client.get("/schnitt")
    assert response.status_code == 200
    page = " ".join(response.get_data(as_text=True).split())
    assert "Gesamtschnitt: –" in page
    if with_empty_subject:
        assert "<td>Sport</td> <td>–</td>" in page
