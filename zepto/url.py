from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('reg/',views.reister,name='reister'),
   path('login/',views.login,name='login')
]