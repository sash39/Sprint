from django.shortcuts import render
from .models import PerevalAdded
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import PerevalSerializer

class PerevalViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer