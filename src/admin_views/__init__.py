from src.admin_views.activity_view import ActivityView
from src.admin_views.member_view import MemberView
from src.admin_views.slider_view import SliderView
from src.admin_views.media_view import MediaView
from src.models import User, Activity, Member, Slider, Media
from src.admin_views.base import SecureModelView

def add_admin_views(admin, db):
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(ActivityView(Activity, db.session))
    admin.add_view(MemberView(Member, db.session))
    admin.add_view(SliderView(Slider, db.session))
    admin.add_view(MediaView(Media, db.session))