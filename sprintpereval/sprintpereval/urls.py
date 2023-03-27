from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from pereval.views import SubmitDataDetailView, SubmitDataUpdateView, SubmitDataListView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger First Blog ",
        default_version='v1',
        description="Test Swagger First Blog",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swaggerBlog.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pereval.urls")),
    path('api/v1/submit-data', include('pereval.urls')),
    path('api/v1/submit-data/1/', SubmitDataDetailView.as_view(), name='submit-data-detail'),
    path('api/v1/submit-data/1/', SubmitDataUpdateView.as_view(), name='submit-data-update'),
    path('api/v1/submit-data', SubmitDataListView.as_view(), name='submit-data-list'),
    path('swagger-ui', TemplateView.as_view(template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path('openapi-schema/', get_schema_view(title='OPENAPI schema', description='Guide'), name='api_schema'),
    ]


