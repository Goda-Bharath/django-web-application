from django.urls import path
from . import views

urlpatterns = [
   path('product/add/',views.productcreatview.as_view(),name='adding_product'),
   path('products/',views.productlistview.as_view(),name='product_list'),   
   path('product/<int:pk>/',views.productdetailview.as_view(),name='product_detail'),
]
