# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from file_list import views as file_views
from login.forms import LoginForm
from django.views.generic import RedirectView


urlpatterns = [
    # list files
    url(r'^{}/$'.format(settings.LIST_FILES_URL.strip('/')),
        file_views.list,
        name='list'),
    # download file
    url(r'^{}/(?P<file_id>\d+)$'.format(settings.MEDIA_URL.strip('/')),
        file_views.download_media,
        name='media'),
    # root /
    url(r'^$',
        RedirectView.as_view(url=settings.LIST_FILES_URL,
            permanent=True)),
    # login
    url(r'^{}/$'.format(settings.LOGIN_URL.strip('/')),
        auth_views.login,
        {'template_name': 'login.html', 'authentication_form': LoginForm},
        name='login'),
    # logout
    url(r'^logout/$',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL.strip('/')}),
]
