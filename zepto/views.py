from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import playersfroms,players,StadiumForm,stadium,profilepic,UserRegisterfrom
from .models import franchise
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View;
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
    

def regisetr_players(request):
    if request.method == "POST":
        form = playersfroms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Register players succefully") 
        else:
            return HttpResponse("Invalide data entered",satus=400)
    else:
       form = playersfroms()
       return render(request,"register_player.html",{"form":form})


def player_list(request):
    playerss = players.objects.all()
    return render (request,"players_list.html",{"players":playerss})

def update_players(request,id):
   playerss = players.objects.get(id=id)
   if request.method == "POST":
       playerss.name = request.POST.get("name")
       playerss.country = request.POST.get("country")
       playerss.age = request.POST.get("age")
       playerss.role = request.POST.get("role")
       playerss.nationality = request.POST.get("nationality")
       playerss.franchise = request.POST.get("franchise")
       
       playerss.save()
       return redirect("players_lists")
   else:
        return render(request,"updated_players.html",{"players":playerss})
       
    
def delete_players(request,id):
    playersss = players.objects.get(id=id)
    
    if request.method == "POST":
        playersss.delete()
        return redirect ("players_lists")

def stidume_ground(request):
    if request.method == "POST":
        form = StadiumForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("stadium_listed ") 
        else:
            return HttpResponse("invalide data")
    else:
        form = StadiumForm()

    return render(request, "stidum_reg.html", {"form": form})


def stadium_list(request):
    staidmuss = stadium.objects.all()
    return render(request, "stadium_list.html",{"staidums":staidmuss})

def reg_user(request):
    if request.method == 'POST':
      user_deatils = UserRegisterfrom(request.POST)
      profile_form = profilepic(request.POST,request.FILES)
      if user_deatils.is_valid() and profile_form.is_valid():
          user = user_deatils.save(commit=False)
          user.set_password(user_deatils.cleaned_data['password'])
          user.save()
          

          profile = profile_form.save(commit=False)
          profile.user = user
          profile.save()
          return HttpResponse("Profil pic is updated succefully");
    else:
      user_deatils = UserRegisterfrom()
      profile_form = profilepic()
    return render(
    request,
    'regis_user.html',
    {
        'user_deatils': user_deatils,
        'profile_form': profile_form
    }
)

def Login_users(request):
    if request.method == 'POST':
       login_form  = AuthenticationForm(request,data=request.POST)
       if login_form.is_valid():
          username = login_form.cleaned_data['username']
          password = login_form.cleaned_data['password']
       
          user = authenticate(request,username=username, password=password)
          
          if user is not None:
                login(request, user)
                return HttpResponse("You have successfuly logged in!")
          else:
                return HttpResponse ("Incorrect username or password")            
    else:
      return render(
    request,
    'profileuser.html',
    {
        'login_form':login_form
    }
)



