# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views
from login.forms import LoginForm
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^list/', include('file_list.urls')),
    url(r'^$', RedirectView.as_view(url='/list/', permanent=True)),
    url(r'^login/$', views.login, {'template_name': 'login.html',
                                   'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
