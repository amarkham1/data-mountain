from settings import *

DEBUG = TEMPLATE_DEBUG = False

SECRET_KEY='1c3-cr3am-b4by'

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'production',
        'USER': 'app'
        'PASSWORD': 'letmein'
    }
}

DEBUG = False
