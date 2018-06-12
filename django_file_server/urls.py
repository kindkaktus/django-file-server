"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.generic import RedirectView

from login.forms import LoginForm
from file_list import views as file_views

urlpatterns = [
    # list files
    path('{}/'.format(settings.LIST_FILES_URL.strip('/')),
        file_views.list,
        name='list'),
    # download file
    path('{}/<int:file_id>'.format(settings.MEDIA_URL.strip('/')),
        file_views.download_media,
        name='media'),
    # root /
    path('',
         RedirectView.as_view(url=settings.LIST_FILES_URL,
             permanent=True)),
    # login
    path('{}/'.format(settings.LOGIN_URL.strip('/')),
        auth_views.login,
        {'template_name': 'login.html', 'authentication_form': LoginForm},
        name='login'),
    # logout
    path('logout/',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL.strip('/')}),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
