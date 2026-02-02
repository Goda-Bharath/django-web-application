from django import forms;
from .models import productItems;

class productdata(forms.models):
    class meta:
       model = productItems
       fields = '__all__'
