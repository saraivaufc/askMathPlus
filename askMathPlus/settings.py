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
from .components_metro import *

#import hide
from .hide import site_config as SITE_CONFIG
from .hide import database_config  as DATABASE_CONFIG
from .hide import email_config as EMAIL_CONFIG
from .hide import social_config as SOCIAL_CONFIG
from .hide import recaptcha_config as RECAPTCHA_CONFIG

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SITE_CONFIG.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['www.askmath.quixada.ufc.br']

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
	'rest_framework',
	'nocaptcha_recaptcha',
	'djcelery',
	'mathfilters',
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
		'PASSWORD': 'postgres',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}

"""
Configurations of database to server
"""
if not DEBUG:
	DATABASES['default'] = {
		'ENGINE': DATABASE_CONFIG.DATABASE_ENGINE,
		'NAME': DATABASE_CONFIG.DATABASE_NAME,
		'USER': DATABASE_CONFIG.DATABASE_USER,
		'PASSWORD': DATABASE_CONFIG.DATABASE_PASSWORD,
		'HOST': DATABASE_CONFIG.DATABASE_HOST,
		'PORT': DATABASE_CONFIG.DATABASE_PORT,
	}

# Templates
TEMPLATE_DIRS = (
	'askmath/templates',
	'askmath/templates/authentication',
	'nocaptcha_recaptcha/templates',
)

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


# Social Auth
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USER_MODEL = 'askmath.Student'
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

FORMAT_MODULE_PATH = 'askMathPlus.formats'
from askMathPlus.formats.pt_BR.formats import * #GAMBI

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

ADMINS = (
	(u'Ciano Saraiva', u'saraiva.ufc@gmail.com'),
	(u'AskMath', u'askmathplus@gmail.com'),
)

MANAGERS = (
    ('George Harrison', 'gharrison@example.com'),
)

"""
Configurations of email
"""
EMAIL_ADMINS = EMAIL_CONFIG.EMAIL_ADMINS
DEFAULT_FROM_EMAIL = EMAIL_CONFIG.DEFAULT_FROM_EMAIL

EMAIL_HOST = EMAIL_CONFIG.EMAIL_HOST
EMAIL_HOST_USER = EMAIL_CONFIG.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_CONFIG.EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_CONFIG.EMAIL_PORT
EMAIL_USE_TLS = EMAIL_CONFIG.EMAIL_USE_TLS
EMAIL_BACKEND = EMAIL_CONFIG.EMAIL_BACKEND

"""
Configurations of recaptcha
"""
NORECAPTCHA_SITE_KEY = RECAPTCHA_CONFIG.SITE_KEY
NORECAPTCHA_SECRET_KEY = RECAPTCHA_CONFIG.SECRET_KEY

"""
Configurations of social
"""
SOCIAL_AUTH_FACEBOOK_KEY = SOCIAL_CONFIG.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET =SOCIAL_CONFIG.SOCIAL_AUTH_FACEBOOK_SECRET

SOCIAL_AUTH_TWITTER_KEY = SOCIAL_CONFIG.SOCIAL_AUTH_TWITTER_KEY
SOCIAL_AUTH_TWITTER_SECRET = SOCIAL_CONFIG.SOCIAL_AUTH_TWITTER_SECRET

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = SOCIAL_CONFIG.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = SOCIAL_CONFIG.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


# CELERY STUFF

BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
