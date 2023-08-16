from config.settings.base import *

SECRET_KEY = config("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

ADMIN_URL = config("DJANGO_ADMIN_URL")
