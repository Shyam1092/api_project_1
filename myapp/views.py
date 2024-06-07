from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from .serialization import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

def index(request):
    if request.method=='POST':
        newdata=bookform(request.POST)
        if newdata.is_valid():
            newdata.save()
            print("Your data has been saved!")
        else:
            print(newdata.errors)
    return render(request,'index.html')

@api_view(['GET'])
def getall(request):
    stdata=bookinfo.objects.all()
    serial=bookSerializer(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookSerializer(stid)
    return Response(data=serial.data)

@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        stid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=bookSerializer(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        bookinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serail=bookSerializer(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=bookSerializer(stid)
        return Response(data=serial.data)
    if request.method=='PUT':
        serail=bookSerializer(data=request.data,instance=stid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
def getal(request):
    url="http://127.0.0.1:8000/getall/"
    req=requests.get(url)
    data=req.json()
    #print(data)
    return render(request,'getal.html',{'data':data})