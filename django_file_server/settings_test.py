from .settings_base import *

DEBUG = True

_DEBUG_DIR = os.path.join(PROJECT_ROOT, 'debug')

LOGGING['handlers']['file']['filename'] = os.path.join(_DEBUG_DIR, 'test.log')
DATABASES['default']['NAME'] = os.path.join(_DEBUG_DIR, 'test.sqlite3')
MEDIA_ROOT = os.path.join(_DEBUG_DIR, 'media')
STATIC_ROOT = os.path.join(_DEBUG_DIR, 'static')
