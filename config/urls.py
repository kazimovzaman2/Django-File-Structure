from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "api/jwt/blacklist/",
        TokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
    # DRF Spectacular UIs:
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # DRF Spectacular UIs:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
