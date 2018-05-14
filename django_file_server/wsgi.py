"""
WSGI config for django_file_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# Uncomment to enable debugging
# os.environ['DJANGO_SETTINGS_MODULE'] = 'django_file_server.settings_devel'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_file_server.settings_production")

application = get_wsgi_application()
