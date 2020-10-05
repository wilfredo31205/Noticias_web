

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


import dj_database_url
from decouple import config 
from .base import * 
from django.conf import settings
settings = load_settings()

DEBUG = False

ALLOWED_HOSTS = []

DATABASES ={

    'default': dj_database_url.config(

        default =config('DATABASE_URL')
    )


 )






}

#DATABASES = {
    #'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'prueba.sqlite3'),
    #}
#}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


