# -*- coding: UTF-8 -*-

"""
Django settings for askMathPlus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import sys
from imp import reload

reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.utils.translation import ugettext_lazy as _
import os
from django.conf import global_settings

from .site_info import *
from .social import *
from .components_metro import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hb@jze2=jvslsc%p8g&u88dhn0d3=fm!)f^o-=w=yj9)woag6x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.askmath.quixada.ufc.br']
# ALLOWED_HOSTS = ['localhost']

# Application definition

# Apps
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
    'nocaptcha_recaptcha',
    'social.apps.django_app.default',  # ERROR ImportError: No module named parse
)
LOCAL_APPS = (
    'askmath',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }, 'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'askmath',
        'USER': 'postgres',
        'PASSWORD': 'macacoaranha',
        'HOST': '200.129.39.113',
        'PORT': '6969',
    }, 'local': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'askmath',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Templates
TEMPLATE_DIRS = (
    'askmath/templates',
    'nocaptcha_recaptcha/templates',
)
# TEMPLATE_CONTEXT
TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'askmath.context_processors.accessibility',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

# Keep templates in memory
# TEMPLATE_LOAFAjango.template.loaders.app_directories.Loader',
#     )),
# )


# Middleware
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

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'askMathPlus.urls'

WSGI_APPLICATION = 'askMathPlus.wsgi.application'

AUTH_USER_MODEL = 'askmath.Person'

LOGIN_URL = '/authentication/options/'
LOGOUT_URL = '/authentication/logout/'

# Recaptca
NORECAPTCHA_SITE_KEY = "6LdVnQ0TAAAAAAwnuLsezpZwIRFhdqs-yrwdmG3n"
NORECAPTCHA_SECRET_KEY = "6LdVnQ0TAAAAAGtLXaOALJ6KTM4XvUF_bUg8enIc"

# Admin
ADMINS = ((u'Ciano Saraiva', u'saraiva.ufc@gmail.com'),)

# EMAIL
EMAIL_ADMINS = [u'saraiva.ufc@gmail.com', u'askmathplus@gmail.com']
DEFAULT_FROM_EMAIL = u'askmathplus@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = u'askmathplus@gmail.com'
EMAIL_HOST_PASSWORD = u'macacoaranha'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Social Auth
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USER_MODEL = 'askmath.Person'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['first_name', 'last_name', 'email']
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, '../askmath/locale'),
    '/var/local/translations/locale',
)

LANGUAGES = (
    ('pt_BR', _('Brazilian Portuguese')),
    ('en', _('English')),
    ('es', _('Spanish')),
)

LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../askmath/static'),)


STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/askmath.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'myapp': {
            'handlers': ['logfile'],
            'level': 'DEBUG',  # Or maybe INFO or WARNING
            'propagate': False
        },
    },
}
