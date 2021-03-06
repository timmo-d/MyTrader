# chat/urls_old.py
from django.conf.urls import url

from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]