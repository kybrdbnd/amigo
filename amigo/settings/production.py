from django.conf import settings
import dj_database_url
import os

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = settings.DATABASES
STATICFILES_STORAGE = settings.STATICFILES_STORAGE

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
