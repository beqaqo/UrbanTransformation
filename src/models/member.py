from src.ext import db
from src.models.base import BaseModel

class Member(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    translations = db.relationship('MemberTranslation', back_populates='member')

class MemberTranslation(BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    member = db.relationship('Member', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    name = db.Column(db.String)
    surname = db.Column(db.String)
    role_title = db.Column(db.String)
    role = db.Column(db.String)
    academical_rank = db.Column(db.String)
    contribution = db.Column(db.Text)

    __table_args__ = (
        db.UniqueConstraint('member_id', 'lang', name='uq_member_lang'),
    )