from django.contrib import admin
from .models import *
# Register your models here.


class ComplaintAdmin(admin.ModelAdmin):
    list_display=['user','title','news',]
admin.site.register(VerifyNews,ComplaintAdmin)

admin.site.register(complaintss)