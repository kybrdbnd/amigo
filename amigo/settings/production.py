from django.conf import settings
import dj_database_url
import os

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = settings.DATABASES
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']