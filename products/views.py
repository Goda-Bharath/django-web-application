from rest_framework.views import APIview
from rest_framework.response import Response
from rest_framework import status
from .models import productdata
from .seralizers import productserializer;


class productAPIS (APIview):
    def get(self,request):
        products = productdata.objects.all()
        serializer = productserializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = productserializer(data=request.data)
        
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=200)
        return Response(serializer.errors, status= 400)
    
