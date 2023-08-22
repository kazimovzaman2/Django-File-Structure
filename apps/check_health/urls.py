from django.urls import path
from apps.check_health.views import check_health

urlpatterns = [path("", check_health)]
