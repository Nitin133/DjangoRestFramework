from django.shortcuts import render
import io
import requests
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerialzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
def student_api(request):
    if  request.method =='GET':
        json_data= request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser.parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerialzer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='aplication/json')
        stu-Student.objects.all()
        serializer=StudentSerialzer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='aplication/json')
        


