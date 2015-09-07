from django.conf.urls import include, url
from django.contrib import admin
from views import HouseView, DashboardView

urlpatterns = [
    url(r'^dashboard$', DashboardView.as_view(), name='dashboard'),
    url(r'^house/(?P<pk>\d+)/$', HouseView.as_view(), name='house'),
]
