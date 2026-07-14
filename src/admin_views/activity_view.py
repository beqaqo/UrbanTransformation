from flask_admin.form import ImageUploadField
from flask import current_app
from markupsafe import Markup
from uuid import uuid4
import os

from src.admin_views.base import SecureModelView
from src.admin_views.utils import _image_formatter

class ActivityView(SecureModelView):
    def _author_image_formatter(self, context, model, name):
        if model.img:
            return Markup(f'<img src="/static/{model.author_image}" width="100">')

        return ""

    form_overrides = {
        "img": ImageUploadField,
        "author_image": ImageUploadField
    }

    form_args = {
        "img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        },
        "author_image": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'img': _image_formatter,
                         'author_image': _author_image_formatter}
