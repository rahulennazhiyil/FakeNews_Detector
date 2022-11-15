from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from account.models import *
from django.utils import timezone


from django.urls import reverse


# Create your models here.


   
class VerifyNews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=30)
    news=models.TextField()

    def __sre__(self):
        return str(self.title)



class complaintss(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=30)
    phoneno=models.CharField(max_length=20,blank=True,null=True)
    complaint=models.TextField()

    def __sre__(self):
        return str(self.name)