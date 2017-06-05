from django.contrib.auth.forms import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    contact = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','contact', 'password']
