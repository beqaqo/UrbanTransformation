from src.ext import db

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    time = db.Column(db.Time)
    img = db.Column(db.String, nullable = False)
    link = db.Column(db.String, nullable = True)

def __repr__(self):
    return self.title