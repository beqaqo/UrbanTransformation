from flask_admin.model.form import InlineFormAdmin
from src.admin_views.base import SecureModelView
from wtforms import SelectField

from src.models import CategoryTranslation
from src.config import Config

class CategoryTranslationInline(InlineFormAdmin):
    form_overrides = {
        'lang': SelectField
    }
    form_args = {
        'lang': {
            'label': 'Language',
            'choices': [(l, l) for l in Config.SUPPORTED_LANGS],  # choices, not options
        }
    }

class CategoryView(SecureModelView):
    inline_models = [CategoryTranslationInline(CategoryTranslation),]

    column_list = ('id', 'translations')

    column_formatters = {
        'translations': lambda v, c, m, p: ', '.join(
            t.category_name for t in m.translations
        )
    }