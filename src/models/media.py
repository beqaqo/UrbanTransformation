from src.ext import db
from src.models.base import BaseModel

class Media(BaseModel):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    img = db.Column(db.String, nullable = False)
    link = db.Column(db.String, nullable = True)

    translations = db.relationship('MediaTranslation', back_populates='media')

class MediaTranslation(BaseModel):
    __tablename__ = 'media_translation'

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(5), nullable = False)
    title = db.Column(db.String)
    description = db.Column(db.Text)

    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable = False)
    media = db.relationship('Media', back_populates='translations')

    __table_args__ = (
        db.UniqueConstraint('media_id', 'lang', name='uq_media_lang'),
    )