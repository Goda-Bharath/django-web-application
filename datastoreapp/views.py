from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from .forms import productdata
from .models import productItems


class ProductCreateView(CreateView):
    model = productItems
    form_class = productdata
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        return super().form_valid(form)


class ProductListView(ListView):
    model = productItems
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10   

    def get_queryset(self):
        return productItems.objects.all().order_by('-id')  


class ProductDetailView(DetailView):
    model = productItems
    template_name = 'products/product_details.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = productItems
    form_class = productdata
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = productItems
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('product_list')
    