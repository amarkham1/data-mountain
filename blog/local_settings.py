from settings import *
import os
import dj_database_url

DEBUG = TEMPLATE_DEBUG = False


SECRET_KEY='1c3-cr3am-b4by'
#ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#EMAIL_HOST = 'andrewjmarkham1@gmail.com'
#SERVER_EMAIL = 'andrewjmarkham1@gmail.com'

#DATABASES = {
#    'default': dj_database_url.config(default='postgres://amarkham:Amarkham1@localhost:5432/blogdb')
#}
ADMINS = (
    ('Andrew', 'andrewjmarkham1@gmail.com'),
)
DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}
#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'blogdb',
    #    'USER': 'amarkham',
     #   'PASSWORD': 'Amarkham1',
      #  'HOST': 'localhost',
       # 'PORT': '5432',
    #}
#}

