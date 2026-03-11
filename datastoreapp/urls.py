from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]