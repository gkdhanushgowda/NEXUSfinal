from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='USN')  # Change label as per your requirement
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')  # PasswordInput for hiding input
