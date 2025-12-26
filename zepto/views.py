from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Welcome to zepto website")

def reister (request):
    return render(request,'reg.html')

def login (request):
    return render(request,'Login.html')