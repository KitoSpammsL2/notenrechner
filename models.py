from database import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    grades = db.relationship(
        "Grade", back_populates="subject", cascade="all, delete-orphan"
    )


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False, default=1.0)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    subject = db.relationship("Subject", back_populates="grades")
