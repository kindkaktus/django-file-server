from .settings_base import *

DEBUG = True


STATIC_ROOT = './var/lib/django-file-server/static'
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
#@todo or just log to stdout/stderr
# LOGGING['handlers']['file']['filename'] = os.path.join(MEDIA_ROOT, 'test.log')
DATABASES['default']['NAME'] = ':memory:'
#@todo test with --settings=django_file_server.settings_test manually (not only in tests)