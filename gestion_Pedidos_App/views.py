from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'gestion_Pedidos_App_Templates/home.html')