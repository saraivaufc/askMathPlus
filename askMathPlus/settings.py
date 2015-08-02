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

from .components_metro import *
from .email_info import *
from .site_info import *
import database_info

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb@jze2=jvslsc%p8g&u88dhn0d3=fm!)f^o-=w=yj9)woag6x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
                 
]


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
)

LOCAL_APPS = (
    'askmath',
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

ROOT_URLCONF = 'askMathPlus.urls'

WSGI_APPLICATION = 'askMathPlus.wsgi.application'

AUTH_USER_MODEL = 'askmath.Person'

LOGIN_URL = '/authentication/login/'
LOGOUT_URL = '/authentication/logout/'

ADMINS = ( ('Ciano Saraiva','saraiva.ufc@gmail.com'), )
DEFAULT_FROM_EMAIL= 'saraiva.ufc@gmail.com'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres' : {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': database_info.NAME,                      
       'USER': database_info.USER,
       'PASSWORD': database_info.PASSWORD,
       'HOST': database_info.HOST,
       'PORT': database_info.PORT,
       
    }
}

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, '../askmath/locale'),
    '/var/local/translations/locale',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
     ('pt', _('Portuguese')),
     ('en', _('English')),
     ('es', _('Spanish')),
)

LANGUAGE_CODE = 'en'

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'