from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('reg/',views.reister,name='reister'),
   path('login/',views.login,name='login'),
   path('franc/',views.franchise_list,name="franchise_list"),
   path('franch/',views.franchiseee_list,name='franchise_list'),
   path('franchdata/<int:id>/',views.franchise_data,name='franchise_data'),
   path("updatefranch/<int:id>/",views.update_franchies,name="update_franchies"),
   path("deletefrach/<int:id>/", views.delete_franchies,name="delete_franchies")
]
