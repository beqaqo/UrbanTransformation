from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_restx import Api
from flask_cors import CORS

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(name="UrbanTransformation Panel")
api = Api(doc="/api/docs")
babel = Babel()
cors = CORS()