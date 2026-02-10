from django.urls import path
from .views import productAPIS

urlpatterns = [
   path('products/',productAPIS.as_view()),
]