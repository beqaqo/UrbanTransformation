from src.ext import db
from src.models.base import BaseModel

class Activity(BaseModel):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    img = db.Column(db.String, nullable = False)
    link = db.Column(db.String, nullable = True)

    translations = db.relationship(
        'ActivityTranslation',
        back_populates='activity',
    )

class ActivityTranslation(BaseModel):
    __tablename__ = 'activity_translations'

    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable=False)
    activity = db.relationship('Activity', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    title = db.Column(db.String)
    description = db.Column(db.Text)
    author_name = db.Column(db.String)
    author_profession = db.Column(db.String)
    author_biography = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint('activity_id', 'lang', name='uq_activity_lang'),
    )