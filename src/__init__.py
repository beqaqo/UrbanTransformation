from flask import Flask
from src.ext import db, migrate, login_manager, admin, api, babel
from src.config import Config
from src.commands import init_db, populate_db
from src.models import Activity, Member, User, Slider, Media
from src.admin_views.base import SecureModelView, SecureIndexView
from src.endpoints import MemberList, ActivityList, ActivityDetail, SliderList, MediaList, MediaDetail
from src.views import auth_blueprint
from src.admin_views import ActivityView, MemberView, SliderView, MediaView


COMMANDS = [init_db, populate_db]
BLUEPRINTS = [auth_blueprint]


def register_extensions(app):
    db.init_app(app)
    babel.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    admin.__init__(app, name="UrbanTransformation Panel", index_view=SecureIndexView())
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(ActivityView(Activity, db.session))
    admin.add_view(MemberView(Member, db.session))
    admin.add_view(SliderView(Slider, db.session))
    admin.add_view(MediaView(Media, db.session))

    api.init_app(app)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app