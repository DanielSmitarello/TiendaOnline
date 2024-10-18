from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') # campos de solo lectura

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated') # campos de solo lectura

admin.site.register(CategoriaProd,CategoriaAdmin) # se registra en el panel de administración
admin.site.register(Producto, ProductoAdmin) # se registra en el panel de administración
