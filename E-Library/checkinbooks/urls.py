from django.urls import include, re_path
from . import views

app_name = 'checkinbooks'

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
]