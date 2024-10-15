from django.urls import path
from contacto_App import views

urlpatterns = [
    
    path('',views.contacto,name='Contacto'),    
]