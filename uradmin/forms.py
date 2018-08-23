# Author:Sunny Liu
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    userpswd = forms.CharField(max_length=50)