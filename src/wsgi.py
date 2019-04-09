"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# load environment variables from an optional .env file
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

environment = os.environ.get('ENVIRONMENT', 'production')
if environment == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "src.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "src.settings.production")

application = get_wsgi_application()
