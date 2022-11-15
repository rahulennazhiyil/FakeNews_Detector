from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

public='public'
staff='staff'
user_types=[(staff,'staff'),(public,'public')]



class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField(blank=True)
    image=models.ImageField(upload_to='images',default='default.jpg')
    user_type=CharField(max_length=20,choices=user_types,default=public)


    def __str__(self):
        return str(self.user.username)


