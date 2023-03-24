from django.shortcuts import render
from .models import PerevalAdded
from .serializers import PerevalSerializer, PerevalSubmitDataSerializer, PerevalSubmitDataUpdateSerializer
from rest_framework import generics, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response




class PerevalViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


class SubmitDataDetailView(RetrieveAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSubmitDataSerializer

class SubmitDataUpdateView(UpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSubmitDataUpdateSerializer

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()


        if submit_data.status != 'new':
            message = 'Данные не могут быть отредактированы, т.к. статус "new" не соответствует.'
            return Response({'state': 0, 'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(submit_data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1})