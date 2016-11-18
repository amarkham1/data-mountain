"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

sys.stdout = sys.stderr
import django.core.wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")


from dj_static import Cling
application = Cling(get_wsgi_application())
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
