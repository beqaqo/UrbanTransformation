from flask_admin.form import ImageUploadField
from flask_admin.model.form import InlineFormAdmin
from flask import current_app
from markupsafe import Markup
from wtforms import SelectField
from uuid import uuid4
import os

from src.admin_views.base import SecureModelView
from src.admin_views.utils import _image_formatter
from src.config import Config
from src.models import AboutUsTranslation

class AboutUsTranslationInline(InlineFormAdmin):
    form_overrides = {
        'lang': SelectField
    }
    form_args = {
        'lang': {
            'label': 'Language',
            'choices': [(l, l) for l in Config.SUPPORTED_LANGS],  # choices, not options
        }
    }

class AboutUsView(SecureModelView):
    form_overrides = {
        "title_img": ImageUploadField,
        "mission_img": ImageUploadField
    }

    form_args = {
        "title_img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        },
        "mission_img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'title_img': lambda s,c,m,n: Markup(f'<img src="/static/{m.title_img}" width="100">'),
                         'mission_img': lambda s,c,m,n: Markup(f'<img src="/static/{m.mission_img}" width="100">')}

    inline_models = [AboutUsTranslationInline(AboutUsTranslation),]