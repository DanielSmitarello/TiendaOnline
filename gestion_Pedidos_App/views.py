from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'gestion_Pedidos_App_Templates/home.html')


def tienda(request):
    return render(request,'gestion_Pedidos_App_Templates/tienda.html')

def contacto(request):
    return render(request,'gestion_Pedidos_App_Templates/contacto.html')