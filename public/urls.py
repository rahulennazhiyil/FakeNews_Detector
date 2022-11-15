from django.urls import path
from .import views

urlpatterns=[
   
    path('complaint/',views.complaint,name='complaint'),
    path('all_complaint/',views.view_complaints,name='all_complaint'),
    path('addcomplaint/',views.addcomplaint,name='addcomplaint'),



    
]