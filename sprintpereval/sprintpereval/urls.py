"""sprintpereval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from pereval.views import SubmitDataDetailView, SubmitDataUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/submit-data', include('pereval.urls')),
    path('api/v1/submit-data/1/', SubmitDataDetailView.as_view(), name='submit-data-detail'),
    path('api/v1/submit-data/1/', SubmitDataUpdateView.as_view(), name='submit-data-update'),
    ]
