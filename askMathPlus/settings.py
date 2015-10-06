# -*- coding: UTF-8 -*-

"""
Django settings for askMathPlus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils.translation import ugettext_lazy as _
import os
from django.http import HttpRequest
import database_info
from django.conf import global_settings

from .components_metro import *
from .site_info import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb@jze2=jvslsc%p8g&u88dhn0d3=fm!)f^o-=w=yj9)woag6x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.syndication',
)

THIRD_PARTY_APPS = (
    'rosetta',
)



LOCAL_APPS = (
    'askmath',
    'captcha',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATE_DIRS = (
    'askmath/templates',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


#TEMPLATE_CONTEXT
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

# Keep templates in memory
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


ROOT_URLCONF = 'askMathPlus.urls'

WSGI_APPLICATION = 'askMathPlus.wsgi.application'

AUTH_USER_MODEL = 'askmath.Person'

LOGIN_URL = '/authentication/options/'
LOGOUT_URL = '/authentication/logout/'


#RECAPTCHA
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = "6LdVnQ0TAAAAAAwnuLsezpZwIRFhdqs-yrwdmG3n"
RECAPTCHA_PRIVATE_KEY = "6LdVnQ0TAAAAAGtLXaOALJ6KTM4XvUF_bUg8enIc"


ADMINS = ( ('Ciano Saraiva','saraiva.ufc@gmail.com'), )
DEFAULT_FROM_EMAIL= 'saraiva.ufc@gmail.com'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default' : {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': database_info.NAME,                      
       'USER': database_info.USER,
       'PASSWORD': database_info.PASSWORD,
       'HOST': database_info.HOST,
       'PORT': database_info.PORT,
       
    }
}
 

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, '../askmath/locale'),
    '/var/local/translations/locale',
)

LANGUAGES = (
     ('pt', _('Portuguese')),
     ('en', _('English')),
     ('es', _('Spanish')),
)

LANGUAGE_CODE = 'pt'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT= os.path.join(PROJECT_DIR, '../media')
MEDIA_URL='/media/'

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../askmath/static'),)

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')

STATIC_URL = '/static/'


#EMAIL
EMAIL_ADMINS = ['saraiva.ufc@gmail.com',]
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = True