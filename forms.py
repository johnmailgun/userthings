from django import forms
from django.forms import PasswordInput
from .models import UserProfile

class RegisterForm(forms.Form):
    username = forms.CharField(label='your username')
    email = forms.CharField(label="real email")
    password1 = forms.CharField(label="strong password", widget=PasswordInput())
    password2 = forms.CharField(label="check password spell", widget=PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(label="your username")
    password1 = forms.CharField(label="strong password", widget=PasswordInput())

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_profile','image_profile']
        widgets = {'user_profile': forms.HiddenInput()}
    