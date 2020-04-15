from django.conf.urls import url

from inventory.api import CreateItem, ListItem, RetrieveItem, DeleteItemAPI

urlpatterns = [
    url(r'^create/$', CreateItem.as_view(), name='create_item'),
    url(r'^list/$', ListItem.as_view(), name='list_item'),
    url(r'^retrieve/(?P<item_name>[-\w]+)/$', RetrieveItem.as_view(), name='retrieve'),
    url(r'^delete/(?P<item_name>[-\w]+)/', DeleteItemAPI.as_view(), name='delete'),
]
