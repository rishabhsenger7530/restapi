from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TestModel
from .serializers import TestSerializers
from rest_framework.views import APIView

# from testapp import serializers


# Create your views here.

class Home(APIView):

    def post(self, request):
        serializers = TestSerializers(data= request.data)
        print("fdsfds")
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return HttpResponse("success: data saved successfully")
        else:
            return HttpResponse("error: data not saved")

    def get(self,request):
        content = TestModel.objects.all()
        return JsonResponse({"data":TestSerializers(content,many=True).data})
    
