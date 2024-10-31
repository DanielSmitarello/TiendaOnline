# from django.shortcuts import render
# from .carro import Carro
# from tienda_App.models import Producto
# from django.shortcuts import redirect

# # Create your views here.

# def agregar_producto(request, producto_id):
#     carro=Carro(request)
#     producto=Producto.objects.get(id=producto_id)
#     carro.agregar(producto=producto)
#     return redirect('tienda')

# def restar_producto(request,producto_id):
#     carro=Carro(request)
#     producto=Producto.objects.get(id=producto_id)
#     carro.restar_producto_carro(producto=producto)
#     return redirect('tienda')

# def eliminar_producto(request,producto_id):
#     carro=Carro(request)
#     producto=Producto.objects.get(id=producto_id)
#     carro.eliminar_carro(producto=producto_id)
#     return redirect('tienda')

# def limpiar_carro(request, producto_id):
#     carro=Carro(request)
#     carro.limpiar_carro()
#     return redirect('tienda')

from django.shortcuts import render  # Importa la función render para renderizar templates
from .carro import Carro  # Importa la clase Carro desde el archivo carro.py
from tienda_App.models import Producto  # Importa el modelo Producto desde la aplicación tienda_App
from django.shortcuts import redirect  # Importa la función redirect para redirigir a una URL

# Crear tus vistas aquí

def agregar_producto(request, producto_id):
    carro = Carro(request)  # Inicializa el carrito con la sesión del request
    producto = Producto.objects.get(id=producto_id)  # Obtiene el producto con el ID proporcionado
    carro.agregar(producto=producto)  # Agrega el producto al carrito
    return redirect('tienda')  # Redirige a la vista 'tienda'

def restar_producto(request, producto_id):
    carro = Carro(request)  # Inicializa el carrito con la sesión del request
    producto = Producto.objects.get(id=producto_id)  # Obtiene el producto con el ID proporcionado
    carro.restar_producto_carro(producto=producto)  # Resta una unidad del producto en el carrito
    return redirect('tienda')  # Redirige a la vista 'tienda'

def eliminar_producto(request, producto_id):
    carro = Carro(request)  # Inicializa el carrito con la sesión del request
    producto = Producto.objects.get(id=producto_id)  # Obtiene el producto con el ID proporcionado
    carro.eliminar_carro(producto=producto)  # Elimina el producto del carrito
    return redirect('tienda')  # Redirige a la vista 'tienda'

def limpiar_carro(request):
    carro=Carro(request)  # Inicializa el carrito con la sesión del request
    carro.limpiar_carro()  # Limpia todo el contenido del carrito
    return redirect('tienda')  # Redirige a la vista 'tienda'
