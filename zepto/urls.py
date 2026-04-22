from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('franchises/', views.franchise_list, name='franchise_list'),
    path('franchises/<int:id>/', views.franchise_data, name='franchise_data'),
    path('franchises/update/<int:id>/', views.update_franchise, name='update_franchise'),
    path('franchises/delete/<int:id>/', views.delete_franchise, name='delete_franchise'),
    path('players/new/', views.register_player, name='register_player'),
    path('players/', views.player_list, name='player_list'),
    path('players/update/<int:id>/', views.update_player, name='update_player'),
    path('players/delete/<int:id>/', views.delete_player, name='delete_player'),
    path('stadium/new/', views.create_stadium, name='create_stadium'),
    path('stadium/', views.stadium_list, name='stadium_list'),
    path('users/register/', views.register_user, name='register_user'),
    path('profile/', views.profile, name='profile'),
]