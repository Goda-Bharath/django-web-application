from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import franchise

# Create your views here.
def home (request):
    return HttpResponse("Welcome to zepto website")

def reister (request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        return HttpResponse("User registered succeufully")
     else:  
        return render(request,'reg.html')

def login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        Conformpassword = request.POST.get('ConformPassword')
        print(username,password,Conformpassword)
        return HttpResponse('user is successfully logined')
    else:    
      return render(request,'Login.html')
    

def franchise_list (request):
    if request.method == 'POST':
        name = request.POST.get("name")
        short_name = request.POST.get("short_name")
        founded_year = request.POST.get("founded_year")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        logo_url = request.POST.get("logo_url")
        Add  = request.POST.get("Add")
        Trash = request.POST.get("Trash")

        franchise.objects.create (
        name=name,
        short_name=short_name,
        founded_year=founded_year,
        city=city,
        state=state,
        country=country,
        logo_url = logo_url,
        Add=Add,
        Trash=Trash,
     )
        return HttpResponse("franchise are added succesufuly")
    else:
        return render(request,"franchise.html")
    

def franchiseee_list(request):
    franchh = franchise.objects.all()
    return render(request,"franchisess_list.html",{'franchises': franchh})

def franchise_data(request,id):
    franch = franchise.objects.get(id=id)
    return render (request,"franchise_deatles.html",{"franchise":franch })

def update_franchies(request,id):
    franchii = franchise.objects.get(id=id)
    if request.method == 'POST':
            franchii.name = request.POST.get("name")
            franchii.short_name = request.POST.get("short_name")
            franchii.founded_year = request.POST.get("founded_year")
            franchii.city = request.POST.get("city")
            franchii.state = request.POST.get("state")
            franchii.country = request.POST.get("country")
          
            franchii.save()
            return redirect("franchise_list")
    else:
        return render(request,"updat_franchies.html",{"franchise":franchii})
    
def delete_franchies(request,id):
    franchiee = franchise.objects.get(id=id)
    
    if request.method == "POST":
        franchiee.delete()
        return redirect ("franchise_list")