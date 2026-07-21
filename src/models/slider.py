from src.ext import db
from src.models.base import BaseModel

class Slider(db.Model):
    __tablename__ = 'sliders'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String, nullable = False)
    translations = db.relationship('SliderTranslation', back_populates='slider')
    show = db.Column(db.Boolean, default = True)

class SliderTranslation(BaseModel):
    __tablename__ = 'sliders_translations'

    id = db.Column(db.Integer, primary_key=True)
    slider_id = db.Column(db.Integer, db.ForeignKey('sliders.id'))
    slider = db.relationship('Slider', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    alt = db.Column(db.String, nullable = False)

    __table_args__ = (
        db.UniqueConstraint('slider_id', 'lang', name='uq_slider_lang'),
    )