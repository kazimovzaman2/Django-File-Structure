from config.settings.base import *

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())
