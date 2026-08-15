from flask_restx import fields
from flask import g

from src.ext import api

def get_translated(field_name):
    def resolver(obj):
        lang = getattr(g, 'lang', 'ka')
        t = next((tr for tr in obj.translations if tr.lang == lang), None) \
            or next((tr for tr in obj.translations if tr.lang == 'ka'), None)
        return getattr(t, field_name, None) if t else None
    return resolver

member_model = api.model('member',{
    "id": fields.Integer,
    "name": fields.String(attribute=get_translated('name')),
    "surname": fields.String(attribute=get_translated('surname')),
    "role_title": fields.String(attribute=get_translated('role_title')),
    "role": fields.String(attribute=get_translated('role')),
    "academical_rank": fields.String(attribute=get_translated('academical_rank')),
    "contribution": fields.String(attribute=get_translated('contribution')),
    "img": fields.String,
    "email": fields.String
})
slider_model = api.model('slider',{
    'id': fields.Integer,
    'alt': fields.String(attribute=get_translated('alt')),
    'img': fields.String
})

category_model = api.model('category', {
    'id': fields.Integer,
    'category_name': fields.String(attribute=get_translated('category_name')),
})

activities_model = api.model('activities',{
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title')),
    'datetime': fields.DateTime,
    'img': fields.String,
    'description': fields.String(attribute=get_translated('description')),
    'category': fields.String(attribute=get_translated('category'))
})

activity_model = api.model('activity', {
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title')),
    'description': fields.String(attribute=get_translated('description')),
    'datetime': fields.DateTime,
    'img': fields.String,
    'link': fields.String,
    'author_name': fields.String(attribute=get_translated('author_name')),
    'author_profession': fields.String(attribute=get_translated('author_profession')),
    'author_image': fields.String,
    'author_biography': fields.String(attribute=get_translated('author_biography')),
})

media_model = api.model('media',{
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title')),
    'datetime': fields.DateTime,
    'img': fields.String,
    'description': fields.String(attribute=get_translated('description')),
    'link': fields.String,
})

blog_model = api.model('blog',{
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title')),
    'datetime': fields.DateTime,
    'img': fields.String,
    'description': fields.String(attribute=get_translated('description')),
    'link': fields.String,
})

about_us_model = api.model('about-us', {
    'id': fields.Integer,
    'title_img': fields.String,
    'title_text': fields.String(attribute=get_translated('title_text')),
    'about_the_laboratory_text': fields.String(attribute=get_translated('about_the_laboratory_text')),
    'our_collection_text': fields.String(attribute=get_translated('our_collection_text')),
    'mission_img': fields.String,
    'our_mission_text': fields.String(attribute=get_translated('our_mission_text')),
})

results_model = api.model('results', {
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title'))
})

timeline_model = api.model('timeline', {
    'id': fields.Integer,
    'img': fields.String,
    'year': fields.Integer(),
    'description': fields.String(attribute=get_translated('description'))
})

result_detail_model = api.model('results-detail', {
    'id': fields.Integer,
    'title': fields.String(attribute=get_translated('title')),
    'timelines': fields.List(fields.Nested(timeline_model)),
})