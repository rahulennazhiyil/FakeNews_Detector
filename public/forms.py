
from django import forms
from .models import *
from django.contrib.auth.models import User




class ComplaintForm(forms.ModelForm):
    class Meta:
        model=VerifyNews
        fields=('title','news',)

