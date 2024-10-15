# from django.contrib import admin
from django.urls import path
from servicios_App import views

urlpatterns = [
   
    path('',views.servicios,name='Servicios'),
    
]