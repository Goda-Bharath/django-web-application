from django import forms
from .models import productItems

class productdata(forms.ModelForm):
    class Meta:
        model = productItems
        fields = '__all__'