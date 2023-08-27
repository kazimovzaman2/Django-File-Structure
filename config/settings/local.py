from config.settings.base import *

DATABASES = {
    "default": config(
        "DATABASE_URL",
        cast=db_url,
    )
}


ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1", "localhost"]

# JWT
# ------------------------------------------------------------------------------
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest
SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] = timedelta(days=1)  # noqa: F405
SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"] = timedelta(days=7)  # noqa: F405

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
