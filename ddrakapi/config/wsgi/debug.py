import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddrakapi.config.settings.debug')

application = get_wsgi_application()
