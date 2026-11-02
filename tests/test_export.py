import csv
import io

from database import db
from models import Grade, Subject


def read_rows(response):
    return list(csv.reader(io.StringIO(response.get_data(as_text=True))))


def test_export_without_grades(client):
    response = client.get("/export.csv")

    assert response.status_code == 200
    assert response.mimetype == "text/csv"
    assert response.headers["Content-Disposition"] == "attachment; filename=noten.csv"
    assert response.get_data(as_text=True) == "Fach,Note,Gewichtung\n"
    assert read_rows(response) == [["Fach", "Note", "Gewichtung"]]


def test_export_all_grades_sorted_by_subject(client):
    mathematik = Subject(name="Mathematik")
    mathematik.grades.extend(
        [Grade(value=5.0, weight=1.0), Grade(value=4.5, weight=2.0)]
    )
    deutsch = Subject(name="Deutsch")
    deutsch.grades.append(Grade(value=5.5, weight=0.5))
    db.session.add_all([mathematik, deutsch, Subject(name="Englisch")])
    db.session.commit()

    response = client.get("/export.csv")

    assert read_rows(response) == [
        ["Fach", "Note", "Gewichtung"],
        ["Deutsch", "5.5", "0.5"],
        ["Mathematik", "5.0", "1.0"],
        ["Mathematik", "4.5", "2.0"],
    ]
    assert "\r" not in response.get_data(as_text=True)


def test_export_subject_with_comma(client):
    subject = Subject(name="Mathematik, Niveau A")
    subject.grades.append(Grade(value=5.0, weight=1.0))
    db.session.add(subject)
    db.session.commit()

    response = client.get("/export.csv")

    assert read_rows(response) == [
        ["Fach", "Note", "Gewichtung"],
        ["Mathematik, Niveau A", "5.0", "1.0"],
    ]
    assert '"Mathematik, Niveau A"' in response.get_data(as_text=True)
