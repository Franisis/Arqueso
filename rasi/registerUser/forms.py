from django import forms
from .models import RegisterUser
class registerUserForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = [
            
        ]