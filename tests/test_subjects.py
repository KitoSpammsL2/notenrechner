import pytest

from database import db
from models import Grade, Subject


def add_subject(name="Mathematik"):
    subject = Subject(name=name)
    db.session.add(subject)
    db.session.commit()
    return subject


def test_new_subject_appears_in_list(client):
    # When: I submit a new subject
    response = client.post(
        "/subjects", data={"name": "  Informatik "}, follow_redirects=True
    )
    # Then: it is saved without the extra spaces and listed
    assert Subject.query.filter_by(name="Informatik").count() == 1
    assert "Informatik" in response.get_data(as_text=True)


@pytest.mark.parametrize("name", ["", "   ", "x" * 101])
def test_invalid_subject_name_is_rejected(client, name):
    # When: I submit an invalid name
    response = client.post("/subjects", data={"name": name}, follow_redirects=True)
    # Then: nothing is saved and I see a message
    assert Subject.query.count() == 0
    assert "höchstens 100 Zeichen" in response.get_data(as_text=True)


def test_duplicate_subject_is_rejected(client):
    # Given: a subject already exists
    add_subject("Englisch")
    # When: I submit the same name again
    response = client.post(
        "/subjects", data={"name": "Englisch"}, follow_redirects=True
    )
    # Then: there is still only one and I see a message
    assert Subject.query.filter_by(name="Englisch").count() == 1
    assert "gibt es schon" in response.get_data(as_text=True)


def test_grade_is_saved_and_shown(client):
    # Given: a subject exists
    subject = add_subject()
    # When: I submit a grade with a weight
    response = client.post(
        f"/subjects/{subject.id}/grades",
        data={"value": "5.5", "weight": "2"},
        follow_redirects=True,
    )
    # Then: it is saved for this subject and shown
    grade = Grade.query.one()
    assert grade.subject_id == subject.id
    assert grade.value == 5.5
    assert grade.weight == 2.0
    assert "5.5" in response.get_data(as_text=True)


def test_grade_accepts_decimal_comma(client):
    subject = add_subject()
    client.post(f"/subjects/{subject.id}/grades", data={"value": "4,5", "weight": "1"})
    assert Grade.query.one().value == 4.5


@pytest.mark.parametrize("value", ["1.0", "6.0"])
def test_grade_limits_are_allowed(client, value):
    subject = add_subject()
    client.post(f"/subjects/{subject.id}/grades", data={"value": value, "weight": "1"})
    assert Grade.query.one().value == float(value)


@pytest.mark.parametrize("value", ["0.9", "6.1", "abc", "", "nan", "inf"])
def test_invalid_grade_is_rejected(client, value):
    # Given: a subject exists
    subject = add_subject()
    # When: I submit an invalid grade
    response = client.post(
        f"/subjects/{subject.id}/grades",
        data={"value": value, "weight": "1"},
        follow_redirects=True,
    )
    # Then: nothing is saved and I see a message
    assert Grade.query.count() == 0
    assert "zwischen 1.0 und 6.0" in response.get_data(as_text=True)


@pytest.mark.parametrize("weight", ["0", "-1", "abc", "", "nan", "inf"])
def test_invalid_weight_is_rejected(client, weight):
    subject = add_subject()
    response = client.post(
        f"/subjects/{subject.id}/grades",
        data={"value": "5", "weight": weight},
        follow_redirects=True,
    )
    assert Grade.query.count() == 0
    assert "grösser als 0" in response.get_data(as_text=True)


def test_grade_for_unknown_subject_returns_404(client):
    response = client.post("/subjects/999/grades", data={"value": "5", "weight": "1"})
    assert response.status_code == 404
