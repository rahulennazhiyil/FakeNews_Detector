from django.contrib import admin
from .models import *
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['user','phone','image','user_type']
admin.site.register(Register,RegisterAdmin)






    