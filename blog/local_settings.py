from settings import *
import os
import dj_database_url

DEBUG = TEMPLATE_DEBUG = False


SECRET_KEY='1c3-cr3am-b4by'
#ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['127.0.0.1', 'www.datamountain.ca']
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

