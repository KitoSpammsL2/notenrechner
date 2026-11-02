import csv
import io

from models import Subject


def test_subject_and_grades_appear_in_average_and_csv(client):
    response = client.post(
        "/subjects", data={"name": "Mathematik"}, follow_redirects=True
    )
    assert response.status_code == 200
    assert "Mathematik" in response.get_data(as_text=True)
    subject = Subject.query.filter_by(name="Mathematik").one()

    for value, weight in [("5.0", "1.0"), ("4.0", "2.0")]:
        response = client.post(
            f"/subjects/{subject.id}/grades",
            data={"value": value, "weight": weight},
            follow_redirects=True,
        )
        assert response.status_code == 200

    response = client.get("/schnitt")
    assert response.status_code == 200
    page = " ".join(response.get_data(as_text=True).split())
    assert "<td>Mathematik</td> <td>4.5</td>" in page
    assert "Gesamtschnitt: 4.50" in page

    response = client.get("/export.csv")
    assert response.status_code == 200
    assert response.mimetype == "text/csv"
    rows = list(csv.reader(io.StringIO(response.get_data(as_text=True))))
    assert rows == [
        ["Fach", "Note", "Gewichtung"],
        ["Mathematik", "5.0", "1.0"],
        ["Mathematik", "4.0", "2.0"],
    ]
