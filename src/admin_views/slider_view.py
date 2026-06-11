from flask_admin.form.upload import ImageUploadField
from src.admin_views.base import SecureModelView
from flask import current_app
from uuid import uuid4
import os

class SliderView(SecureModelView):
    form_overrides = {
        "img": ImageUploadField
    }

    form_args = {
        "img": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }