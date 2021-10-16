from .base import *
import json

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug["django"]["allowed_hosts"]

WSGI_APPLICATION = "ddrakapi.config.wsgi.debug.application"