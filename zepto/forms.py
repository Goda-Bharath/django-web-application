from django import forms
from .models import players,stadium
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class playersfroms(forms.ModelForm):
    class Meta:
        model = players
        fields = ["name","country","age","role","nationality","franchise"]
        

class StadiumForm(forms.ModelForm):
    class Meta:
        model = stadium
        fields = "__all__"  # or list your fields explicitly

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register Stadium'))