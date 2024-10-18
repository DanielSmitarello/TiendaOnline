from django.urls import path
from gestion_Pedidos_App import views

urlpatterns = [

    path('',views.home,name='Home'),
    
]