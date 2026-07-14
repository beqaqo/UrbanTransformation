from src.ext import db

class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    role_title = db.Column(db.String)
    role = db.Column(db.String)
    academical_rank = db.Column(db.String)
    contribution = db.Column(db.Text)
    img = db.Column(db.String)
    email = db.Column(db.String, unique=True)

def __repr__(self):
    return self.name, self.surname
