from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomeUserForm(UserCreationForm):
    """docstring for CustomeUserForm"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']