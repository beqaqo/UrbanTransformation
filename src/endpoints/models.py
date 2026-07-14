from flask_restx import fields

from src.ext import api

member_model = api.model('member',
                         {
                             "id": fields.Integer,
                             "name": fields.String,
                             "surname": fields.String,
                             "role_title": fields.String,
                             "role": fields.String,
                             "academical_rank": fields.String,
                             "contribution": fields.String,
                             "img": fields.String,
                             "email": fields.String
                         })
slider_model = api.model('slider',
                         {
                             'id': fields.Integer,
                             'alt': fields.String,
                             'img': fields.String})
activities_model = api.model('activities',
                             {
                                 'id': fields.Integer,
                                 'title': fields.String,
                                 'datetime': fields.DateTime,
                                 'img': fields.String,
                                 'description': fields.String,
                             })

activity_model = api.model('activity',
                           {
                               'id': fields.Integer,
                               'description': fields.String,
                               'title': fields.String,
                               'datetime': fields.DateTime,
                               'img': fields.String,
                               'link': fields.String,
                               'author_name': fields.String,
                               'author_profession': fields.String,
                               'author_image': fields.String,
                               'author_biography': fields.String,
                           })

media_model = api.model('media',
                        {
                            'id': fields.Integer,
                            'title': fields.String,
                            'datetime': fields.DateTime,
                            'img': fields.String,
                            'description': fields.String,
                            'link': fields.String,
                        })
