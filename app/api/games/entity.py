from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    size = db.Column(db.Double, nullable=False)
    publisher = db.Column(db.String(), nullable=False)