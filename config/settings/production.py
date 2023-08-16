from config.settings.base import *

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

ADMIN_URL = config("DJANGO_ADMIN_URL")
