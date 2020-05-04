# core/urls.py

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import homepage

STATIC_URL = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
MEDIA_URL = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('restricted/admin/', admin.site.urls),
    path('', homepage, name='homepage'),
] + MEDIA_URL



