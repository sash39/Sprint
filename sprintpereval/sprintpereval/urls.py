from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from pereval.views import SubmitDataDetailView, SubmitDataUpdateView, SubmitDataListView
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/submit-data', include('pereval.urls')),
    path('api/v1/submit-data/1/', SubmitDataDetailView.as_view(), name='submit-data-detail'),
    path('api/v1/submit-data/1/', SubmitDataUpdateView.as_view(), name='submit-data-update'),
    path('api/v1/submit-data', SubmitDataListView.as_view(), name='submit-data-list'),
    path('openapi-schema/', schema_view.as_view(), name='schema_url'),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html', extra_context={'schema_url':'schema_url'}), name='swagger-ui'),
    path('', include("pereval.urls")),
    ]




