# forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

#extend AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))