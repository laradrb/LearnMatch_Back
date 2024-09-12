from django.shortcuts import render
from rest_framework import viewsets
from .serializer import LevelSerializer
from .models import Level


# Create your views here.
class LevelView(viewsets.ModelViewSet):
	serializer_class = LevelSerializer


	queryset = Level.objects.all()