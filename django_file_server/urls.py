# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from file_list import views as file_views
from login.forms import LoginForm
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^list/$', file_views.list, name='list'),
    url(r'^list/(?P<file_id>\d+)/$', file_views.download_media, name='media'),
    url(r'^$', RedirectView.as_view(url='/list/', permanent=True)),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html',
                                   'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
]
