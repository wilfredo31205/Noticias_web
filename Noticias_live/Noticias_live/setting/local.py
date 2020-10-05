

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


import dj_database_url
from decouple import config 
from .base import * 
#from django.conf import settings

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES ={
    'default': dj_database_url.config(
        default =config('DATABASE_URL')
    )
}