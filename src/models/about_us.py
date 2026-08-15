from src.ext import db
from src.models.base import BaseModel

class AboutUs(BaseModel):
    __tablename__ = 'about_us'

    id = db.Column(db.Integer, primary_key=True)
    title_img = db.Column(db.String)
    mission_img = db.Column(db.String)

    translations = db.relationship(
        'AboutUsTranslation',
        back_populates='about_us',
    )

class AboutUsTranslation(BaseModel):
    __tablename__ = 'about_us_translations'

    id = db.Column(db.Integer, primary_key=True)
    about_us_id = db.Column(db.Integer, db.ForeignKey('about_us.id'), nullable=False)
    about_us = db.relationship('AboutUs', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    title_text = db.Column(db.Text())
    about_the_laboratory_text = db.Column(db.Text())
    our_collection_text = db.Column(db.Text())
    our_mission_text = db.Column(db.Text())

    __table_args__ = (
        db.UniqueConstraint('about_us_id', 'lang', name='uq_about_us_lang'),
    )