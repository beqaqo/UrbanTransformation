from flask_restx import Resource

from src.models.member import Member
from src.models.activity import Activity
from src.models.slider import Slider
from src.ext import api
from src.endpoints.models import activity_model, slider_model

ns_members = api.namespace("members", path="/api/members")
ns_activities = api.namespace("activities", path="/api/activities")
ns_slider = api.namespace("slider", path="/api/slider")

@ns_members.route("/")
class MemberList(Resource):
    def get(self):
        members = Member.query.all()
        return [
            {
                "id": m.id,
                "name": m.name,
                "surname": m.surname,
                "role": m.role,
                "academical_degree": m.academical_degree,
                "contribution": m.contribution,
                "image": m.image,
                "email": m.email
            } for m in members
        ]


@ns_members.route("/<int:id>")
class MemberDetail(Resource):
    def get(self, id):
        m = Member.query.get_or_404(id)
        return {
            "id": m.id,
            "name": m.name,
            "surname": m.surname,
            "role": m.role,
            "academical_degree": m.academical_degree,
            "contribution": m.contribution,
            "image": m.image,
            "email": m.email
        }


@ns_activities.route("/")
class ActivityList(Resource):
    @ns_activities.marshal_with(activity_model)
    def get(self):
        activities = Activity.query.all()
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
