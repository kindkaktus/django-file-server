from .settings_base import *

DEBUG = True
LOGGING['handlers']['file']['filename'] = 'test.log'

#@todo see STATIC_URL and MEDIA_URL in https://docs.djangoproject.com/en/2.0/howto/static-files/
# DATABASES['default']['NAME'] = 'test.sqlite3'
# SENDFILE_ROOT = './media'
# STATIC_ROOT = './static'
