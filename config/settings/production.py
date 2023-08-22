from config.settings.base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", cast=Csv())

ADMIN_URL = config("DJANGO_ADMIN_URL")
