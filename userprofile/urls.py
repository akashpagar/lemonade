from django.conf.urls import url

from userprofile.api import login, logoutsession, GetProfile

urlpatterns = [
    url(r'^login/$', login, name='login_api'),
    url(r'^logout/$', logoutsession, name='logout_api'),
    url(r'^getprofiledetails/(?P<id>[-\w]+)/', GetProfile.as_view(), name='get_profile'),
]
