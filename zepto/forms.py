from django import forms
from .models import players,stadium
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import profilepic
from django.contrib.auth.models import User

class playersfroms(forms.ModelForm):
    class Meta:
        model = players
        fields = ["name","country","age","role","nationality","franchise"]
        

class StadiumForm(forms.ModelForm):
    class Meta:
        model = stadium
        fields = "__all__" 

    def __init__(self, args, kwargs):
        super().__init__(args, kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register Stadium'))
        
class UserRegisterfrom(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    conform_password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
       model = User
       fields = ["username","email","password","conform_password"]
    
class profileForm(forms.ModelForm):
    class Meta:
        model = profilepic
        fields = ["phone_number","address","profile_picture"]
        
