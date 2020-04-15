from django.conf.urls import url

from productdetails.api import GetTaskDetails

urlpatterns = [
    url(r'^list/', GetTaskDetails.as_view(), name='task details'),]
