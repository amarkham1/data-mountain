SECRET_KEY='1c3-cr3am-he11o-b4by'

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogdb',
    }
}

DEBUG = False
