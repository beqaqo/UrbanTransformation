from flask_admin.form import ImageUploadField
from flask_admin.model.form import InlineFormAdmin
from flask import current_app
from markupsafe import Markup
from wtforms import SelectField
from uuid import uuid4
import os

from src.admin_views.base import SecureModelView
from src.config import Config
from src.models import ResultTranslation, TimelineTranslation, Timeline


class TimelineTranslationInline(InlineFormAdmin):
    form_overrides = {
        'lang': SelectField
    }
    form_args = {
        'lang': {
            'label': 'Language',
            'choices': [(l, l) for l in Config.SUPPORTED_LANGS],  # choices, not options
        }
    }


class TimelineInline(InlineFormAdmin):
    form_overrides = {
        "img": ImageUploadField,
    }

    form_args = {
        "img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        },
    }

    column_formatters = {'img': lambda v, c, m, n: Markup(f'<img src="/static/{m.img}" width="100">'),}

    inline_models = [TimelineTranslationInline(TimelineTranslation),]

class TimelineView(SecureModelView):
    form_overrides = {
        "img": ImageUploadField,
    }

    form_args = {
        "img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        },
    }

    column_formatters = {'img': lambda v,c, m, n: Markup(f'<img src="/static/{m.img}" width="100">'), }

    inline_models = [TimelineTranslationInline(TimelineTranslation), ]

class ResultTranslationInline(InlineFormAdmin):
    form_overrides = {
        'lang': SelectField
    }
    form_args = {
        'lang': {
            'label': 'Language',
            'choices': [(l, l) for l in Config.SUPPORTED_LANGS],  # choices, not options
        }
    }

class ResultView(SecureModelView):
    inline_models = [ResultTranslationInline(ResultTranslation),TimelineInline(Timeline),]