from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': os.environ.get("DB_NAME"),
        'USER': 'admin',
        'PASSWORD': os.environ.get("DB_PASSWORD")
    }
}

WSGI_APPLICATION = "ddrakapi.config.wsgi.deploy.application"