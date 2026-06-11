from flask_restx import fields

from src.ext import api



slider_model = api.model('slider', {'id': fields.Integer, 'show': fields.Boolean, 'img': fields.String})
activity_model = api.model('activity', {'id': fields.Integer,
                                        'show': fields.Boolean,
                                        'datetime': fields.DateTime,
                                        'time': fields.String,
                                        'img': fields.String,
                                        'link': fields.String,})