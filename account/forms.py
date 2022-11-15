
from datetime import date
from django import forms
from django.forms.widgets import PasswordInput, SelectDateWidget, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=('phone','image')

class UpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=('phone','image')



