from django.shortcuts import render

from .serializers import TestSerializers
from .models import TestModel
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here




class Home(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializers

class HomeUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializers
    