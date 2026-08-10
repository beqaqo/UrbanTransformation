from src.ext import db
from src.models.base import BaseModel

class Blog(BaseModel):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    img = db.Column(db.String, nullable = False)
    link = db.Column(db.String, nullable = True)

    translations = db.relationship('BlogTranslation', back_populates='blog')

class BlogTranslation(BaseModel):
    __tablename__ = 'blog_translations'

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(5), nullable = False)
    title = db.Column(db.String)
    description = db.Column(db.Text)

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable = False)
    blog = db.relationship('Blog', back_populates='translations')

    __table_args__ = (
        db.UniqueConstraint('blog_id', 'lang', name='uq_blog_lang'),
    )