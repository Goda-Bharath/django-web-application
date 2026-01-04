from django import forms
from .models import players


class playersfroms(forms.ModelForm):
    class Meta:
        model = players
        fields = ["name","country","age","role","nationality","franchise"]