from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "id": "Email"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username", "id": "Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password", "id": "password1"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":" Confirm Password", "id": "password2"}))
    class Meta:
        model = User
        fields = ['email', 'username']


