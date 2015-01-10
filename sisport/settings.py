# -*- encoding: utf-8 -*-
from spirit.settings import *
from django.utils.translation import ugettext_lazy as _

"""
Django settings for sisport project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p7+r3m2ohqy@1(6g33od-cux$3%!)&@l9**7-eq7d2r&%57=+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition


INSTALLED_APPS += (
    'spirit_user_profile',
    'ask',
    'django.contrib.webdesign',
)

TEMPLATE_DIRS = (
    'ask/templates',
)

ROOT_URLCONF = 'sisport.urls'

WSGI_APPLICATION = 'sisport.wsgi.application'

ST_RATELIMIT_ENABLE = True
ST_RATELIMIT_CACHE_PREFIX = 'srl'
ST_RATELIMIT_CACHE = 'default'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'SQLite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default' : {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'askmath',                      
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'localhost',
    }
    
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'ask_cache',
    },
}

CACHES.update({
    'djconfig': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
})


ADMINS = ( ('Ciano','saraiva.ufc@gmail.com'), )


DEFAULT_FROM_EMAIL= 'saraiva.ufc@gmail.com'


FORMAT_MODULE_PATH = 'ask.formats'

LANGUAGE_CODE = 'pt'

LANGUAGES = (
    ('pt', _('Português')),
    ('en', _('Inglês')),
    ('es', _('Espanhol')),
)

TIME_ZONE = 'America/Fortaleza'

AUTH_USER_MODEL = 'spirit_user_profile.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

PROJECT_DIR = os.path.dirname(__file__)

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../ask/static'),os.path.join(PROJECT_DIR, '../spirit/'),)

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')

STATIC_URL = '/static/'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
