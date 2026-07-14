from markupsafe import Markup

def _image_formatter(self, context, model, name):
    if model.img:
        return Markup(f'<img src="/static/{model.img}" width="100">')

    return ""