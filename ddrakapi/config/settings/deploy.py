from .base import *
import json

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_deploy["django"]["allowed_hosts"]

WSGI_APPLICATION = "ddrakapi.config.wsgi.deploy.application"