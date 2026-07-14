from src.ext import db

class Slider(db.Model):
    __tablename__ = 'sliders'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String, nullable = False)
    alt = db.Column(db.String, nullable=False)
    show = db.Column(db.Boolean, default = True)