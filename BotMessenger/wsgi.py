"""
WSGI config for BotMessenger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BotMessenger.settings")

# application = Cling(get_wsgi_application())
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
