from flask_admin.form.upload import ImageUploadField
from flask_admin.model.form import InlineFormAdmin
from flask import current_app
from wtforms import SelectField
from uuid import uuid4
import os

from src.admin_views.base import SecureModelView
from src.config import Config
from src.models import MemberTranslation
from src.admin_views.utils import _image_formatter

class MemberTranslationInline(InlineFormAdmin):
    form_overrides = {
        'lang': SelectField
    }
    form_args = {
        'lang': {
            'label': 'Language',
            'choices': [(l, l) for l in Config.SUPPORTED_LANGS],
        }
    }

class MemberView(SecureModelView):
    form_overrides = {
        "img": ImageUploadField,
    }

    form_args = {
        "img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'img': _image_formatter}

    inline_models = [MemberTranslationInline(MemberTranslation)]