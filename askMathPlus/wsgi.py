"""
WSGI config for askMathPlus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
import time
import traceback
import signal
from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "askMathPlus.settings"


try:
	application = get_wsgi_application()
	print 'WSGI without exception'
except Exception:
	print 'handling WSGI exception'
	# Error loading applications
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(), signal.SIGINT)
		time.sleep(2.5)

# from django.core.wsgi import get_wsgi_application
# import os

# os.environ["DJANGO_SETTINGS_MODULE"] = "askMathPlus.settings"

# application = get_wsgi_application()
