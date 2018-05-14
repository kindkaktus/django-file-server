"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(PROJECT_ROOT, ...)
import os

# Build paths inside the project like this: os.path.join(PROJECT_ROOT, ...)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-q@x+fbn4vl-+qs!*a=+(u%j1w76z_(7re-1*b+yb&a+rj=-&+'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'file_list',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# We do not set SECURE_SSL_REDIRECT because our front-end server handles redirect to ssl
SECURE_SSL_REDIRECT = False
# Suppress warnings about not setting SECURE_SSL_REDIRECT for 'manage.py check --deploy' checks
SILENCED_SYSTEM_CHECKS = ["security.W008"]

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'

# Add this to tell Django where to redirect after
# successful login
LIST_FILES_URL = '/list/'
LOGIN_REDIRECT_URL = LIST_FILES_URL

ROOT_URLCONF = 'django_file_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'intermediate': {
            'format': '%(asctime)s %(name)s <%(process)d> [%(levelname)s] "%(funcName)s() %(message)s"'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django-file-server/error.log',
            'formatter': 'intermediate',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'file_list': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'login': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

WSGI_APPLICATION = 'django_file_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/var/lib/django-file-server', 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'

#
# Handling medial files
#
# User requests file download under MEDIA_URL
#    -> django backend authenticates this request and returns back to the front-end webserver (nginx) with an internal request to SENDFILE_URL
#        -> nginx maps this request to the local file under SENDFILE_ROOT and gives it back to the user
# The reason to involve front-end webserver is efficiency (django can't efficiently serve large files)
#
# IMPORTANT: KEEP THESE 3 VALUES IN SYNC WITH YOUR FRONT-END WEBSERVER
# https://pypi.python.org/pypi/django-sendfile/
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_URL = '/media'
SENDFILE_ROOT = '/var/lib/django-file-server/media'

MEDIA_URL = '/download/'
# media files will be uploaded here
MEDIA_ROOT = SENDFILE_ROOT

#
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
#

# Input location of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
]
# Static files should be copied here to be served by the webserver
STATIC_ROOT = '/var/lib/django-file-server/static'
# URL of static files
STATIC_URL = '/static/'
