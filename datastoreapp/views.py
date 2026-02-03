from django.shortcuts import render
from froms import productdata
from models import productItems
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy


class productcreatview(CreateView):
    model = productItems
    form_class = productdata
    template_name  = 'add_product.html'
    success_url = reverse_lazy('product_list')


class productlistview(ListView):
    model = productItems
    template_name = 'product_list.html'
    context_object_name = 'products'
    
