from django.shortcuts import render
from .forms import productdata
from .models import productItems
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy


class ProductCreateView(CreateView):
    model = productItems
    form_class = productdata
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_list')


class ProductListView(ListView):
    model = productItems
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = productItems
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = productItems
    form_class = productdata
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = productItems
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')