from django.shortcuts import render, get_object_or_404
from tienda_App.models import CategoriaProd, Producto

# Create your views here.

def tienda(request, categoria_id=None):
    categorias=CategoriaProd.objects.all()

    if categoria_id:
        categoria=get_object_or_404(CategoriaProd,id=categoria_id)
        productos=Producto.objects.filter(categoria=categoria)
    else:
        productos=Producto.objects.all()
    
    return render(request,'tienda/tienda.html',{'categoria':categoria if categoria_id else None,'productos':productos,'categorias':categorias})