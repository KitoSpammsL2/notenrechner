import pytest

from database import db
from models import Grade, Subject


@pytest.mark.parametrize("path", ["/", "/schnitt", "/export.csv"])
def test_pages_load(client, path):
    assert client.get(path).status_code == 200


def test_subject_is_saved_with_its_grades(app):
    # Given: a subject with one grade
    subject = Subject(name="Mathematik")
    subject.grades.append(Grade(value=5.5, weight=2.0))
    # When: it is saved
    db.session.add(subject)
    db.session.commit()
    # Then: it can be read back from the database
    saved = Subject.query.filter_by(name="Mathematik").one()
    assert saved.grades[0].value == 5.5
    assert saved.grades[0].weight == 2.0


def test_subject_appears_on_home_page(client, app):
    # Given: a saved subject
    db.session.add(Subject(name="Informatik"))
    db.session.commit()
    # When: the home page is opened
    response = client.get("/")
    # Then: the subject is listed
    assert "Informatik" in response.get_data(as_text=True)
