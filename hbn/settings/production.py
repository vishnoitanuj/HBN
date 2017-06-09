# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True

DATABSES = settings.DATABASES

import dj_database_url
DATABSES['default'] = dj_database_url.config()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

ALLOWED_HOSTS = ['*']