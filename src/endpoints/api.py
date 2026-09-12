from flask_restx import Resource, reqparse

from src.models import Member, Activity, Slider, Media, ActivityCategory, Blog, AboutUs, Result
from src.ext import api
from src.endpoints.models import activities_model, activity_model, slider_model, member_model, \
    media_model, media_detail, category_model, blog_model, blog_detail, about_us_model, \
    results_model, result_detail_model

ns_members = api.namespace("members", path="/<lang>/api/members")
ns_activities = api.namespace("activities", path="/<lang>/api/activities")
ns_slider = api.namespace("slider", path="/<lang>/api/slider")
ns_media = api.namespace("media", path="/<lang>/api/media")
ns_blog = api.namespace("blog", path="/<lang>/api/blog")
ns_about_us = api.namespace("about-us", path="/<lang>/api/about_us")
ns_results = api.namespace("results", path="/<lang>/api/results")

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

    @ns_media.marshal_with(media_detail)
    def get(self, id):
        media = Media.query.get_or_404(id)

        return media

@ns_blog.route("/")
class BlogList(Resource):
    @ns_media.marshal_with(blog_model)
    def get(self):
        blog = Blog.query.all()

        return blog


@ns_blog.route("/<int:id>")
class BlogDetail(Resource):

    @ns_blog.marshal_with(blog_detail)
    def get(self, id):
        blog = Blog.query.get_or_404(id)

        return blog

@ns_about_us.route("/")
class AboutUsPage(Resource):

    @ns_about_us.marshal_with(about_us_model)
    def get(self):
        about_us = AboutUs.query.first()

        return about_us

@ns_results.route('/')
class ResultsApi(Resource):

    @ns_results.marshal_with(results_model)
    def get(self):
        results = Result.query.all()

        return results

@ns_results.route('/<int:id>')
class ResultsDetail(Resource):
    @ns_results.marshal_with(result_detail_model)
    def get(self, id):
        result = Result.query.get_or_404(id)

        if result:
            return result