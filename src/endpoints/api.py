from flask_restx import Resource, reqparse
from flask import request

from src.models import Member, Activity, Slider, Media, ActivityCategory
from src.ext import api
from src.endpoints.models import activities_model, activity_model, slider_model, member_model, media_model, category_model

ns_members = api.namespace("members", path="/<lang>/api/members")
ns_activities = api.namespace("activities", path="/<lang>/api/activities")
ns_slider = api.namespace("slider", path="/<lang>/api/slider")
ns_media = api.namespace("media", path="/<lang>/api/media")

@ns_members.route("/")
class MemberList(Resource):
    @ns_members.marshal_with(member_model)
    def get(self):
        members = Member.query.all()
        return members

@ns_activities.route("/categories")
class CategoryList(Resource):
    @ns_activities.marshal_with(category_model)
    def get(self):
        categories = ActivityCategory.query.all()

        return categories

activities_parser = reqparse.RequestParser()
activities_parser.add_argument('category_id', type=int, location='args', required=False)

@ns_activities.route("/")
class ActivityList(Resource):

    @ns_activities.expect(activities_parser)
    @ns_activities.marshal_with(activities_model)
    def get(self):
        args = activities_parser.parse_args()
        category_id = args.get('category_id')

        query = Activity.query

        if category_id is not None:
            query = query.filter_by(category_id=category_id)

        activities = query.all()
        return activities


@ns_activities.route("/<int:id>")
class ActivityDetail(Resource):
    @ns_activities.marshal_with(activity_model)
    def get(self, id):
        a = Activity.query.get_or_404(id)
        return a


@ns_slider.route("/")
class SliderList(Resource):
    @ns_slider.marshal_with(slider_model)
    def get(self):
        sliders = Slider.query.filter_by(show=True).all()
        return sliders


@ns_media.route("/")
class MediaList(Resource):
    @ns_media.marshal_with(media_model)
    def get(self):
        media = Media.query.all()

        return media


@ns_media.route("/<int:id>")
class MediaDetail(Resource):
    def get(self, id):
        media = Media.query.get_or_404(id)
        if media:
            recents = Media.query.filter(Media.id != media.id).order_by(Media.datetime.desc()).limit(5).all()

        return_obj = [{
            "id": media.id,
            "title": media.title,
            "description": media.description,
            "link": media.link,
            "img": media.img,
            },
            {"recents": [{
                "id": recent.id,
                "title": recent.title,
                "description": recent.description,
                "link": recent.link,
                "img": recent.img,
            } for recent in recents
            ]},
        ]

        return return_obj
