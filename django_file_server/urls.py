# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views
from login.forms import LoginForm
from django.views.generic import RedirectView
from django.conf import settings


urlpatterns = [
    url(r'^(list|media)/', include('file_list.urls')),
    url(r'^$', RedirectView.as_view(url='/list/', permanent=True)),
    url(r'^login/$', views.login, {'template_name': 'login.html',
                                   'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
