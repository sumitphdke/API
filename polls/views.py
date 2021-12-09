from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from polls.Serializers import *#importing the serializers
from .models import *#importtng models
class MgViewset(viewsets.ModelViewSet):
    queryset=mg.objects.all()
    serializer_class=mgserializer
class ssviewset(viewsets.ModelViewSet):
    queryset=ss.objects.all()
    serializer_class=ssserializer
    