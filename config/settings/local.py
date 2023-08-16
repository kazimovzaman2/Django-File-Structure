from config.settings.base import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DEBUG = True


# JWT
# ------------------------------------------------------------------------------
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest
SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] = timedelta(days=1)  # noqa: F405
SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"] = timedelta(days=7)  # noqa: F405

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
