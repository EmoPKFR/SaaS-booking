from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Business
from .serializers import BusinessSerializer
from .permissions import IsBusinessOwner


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsBusinessOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)