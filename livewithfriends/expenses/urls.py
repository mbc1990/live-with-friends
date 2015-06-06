from django.conf.urls import include, url
from django.contrib import admin
from views import HouseView

urlpatterns = [
    url(r'^house/', HouseView.as_view(), name='house'),
]
