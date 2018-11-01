from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^show', views.showAll),
    url(r'^show/(?P<user_id>\d+)', views.showOne),
    url(r'^editUser/(?P<user_name>\d+)', views.editUser),
]