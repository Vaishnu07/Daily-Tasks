from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class userid(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")