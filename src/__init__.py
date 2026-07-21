from flask import Flask, g, abort
from src.ext import db, migrate, login_manager, admin, api, babel
from src.config import Config
from src.commands import init_db, populate_db
from src.models import Activity, ActivityTranslation, Member, User, Slider, Media
from src.admin_views.base import SecureIndexView
from src.endpoints import MemberList, ActivityList, ActivityDetail, SliderList, MediaList, MediaDetail
from src.views import auth_blueprint
from src.admin_views import add_admin_views


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
    add_admin_views(admin, db)

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

    @app.url_value_preprocessor
    def pull_lang_code(endpoint, values):
        if values is None:
            return
        lang = values.pop('lang', None)
        if lang is None:
            return  # route without a <lang> segment, nothing to do
        if lang not in Config.SUPPORTED_LANGS:
            abort(404)
        g.lang = lang

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app