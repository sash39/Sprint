from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pereval.views import PerevalViewSet

router = routers.SimpleRouter()
router.register(r'pereval', PerevalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)