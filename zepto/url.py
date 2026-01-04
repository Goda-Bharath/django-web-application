from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('reg/',views.reister,name='reister'),
   path('login/',views.login,name='login'),
   path('franc/',views.franchise_list,name="franchise_list"),
   path('franch/',views.franchiseee_list,name='franchise_lists'),
   path('franchdata/<int:id>/',views.franchise_data,name='franchise_data'),
   path("updatefranch/<int:id>/",views.update_franchies,name="update_franchies"),
   path("deletefrach/<int:id>/", views.delete_franchies,name="delete_franchies"),
   path("newplayers/",views.regisetr_players,name="register_players"),
   path("playerslist/",views.player_list,name="players_lists"),
   path("updateplayer/<int:id>/",views.update_players,name="update_players"),
   path("deleteplayer/<int:id>/",views.delete_players,name="delete_players")
]
