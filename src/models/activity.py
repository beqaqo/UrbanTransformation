from src.ext import db
from src.models.base import BaseModel

class Activity(BaseModel):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    img = db.Column(db.String, nullable = False)
    link = db.Column(db.String, nullable = True)

    category_id = db.Column(db.Integer, db.ForeignKey('activity_categories.id', name='fk_activities_category_id'))
    category = db.relationship('ActivityCategory', back_populates='activities')

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

class ActivityCategory(BaseModel):
    __tablename__ = 'activity_categories'

    id = db.Column(db.Integer, primary_key=True)

    activities = db.relationship('Activity', back_populates='category')
    translations = db.relationship(
        'CategoryTranslation',
        back_populates='category',
    )

    def __repr__(self):
        return ', '.join(
            translation.category_name for translation in self.translations
        )

class CategoryTranslation(BaseModel):
    __tablename__ = 'category_translations'

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(5))
    category_name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('activity_categories.id', name='fk_translation_category_id'))
    category = db.relationship('ActivityCategory', back_populates='translations')