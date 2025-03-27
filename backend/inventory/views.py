from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Lead
from .serializers import CarSerializer, LeadSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


