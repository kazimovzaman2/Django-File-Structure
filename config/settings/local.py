from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DOMAIN = "localhost"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
