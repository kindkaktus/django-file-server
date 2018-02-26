# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^list(/)?$', views.list, name='list'),
    # url(r'^media$', views.download_media),
    url(r'^$', views.list, name='list'),
]
