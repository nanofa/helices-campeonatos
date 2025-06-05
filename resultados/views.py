from django.shortcuts import render
from rest_framework import viewsets
from .models import Tiro
from .serializers import TiroSerializer

class TiroViewSet(viewsets.ModelViewSet):
    queryset = Tiro.objects.all()
    serializer_class = TiroSerializer

# Create your views here.
