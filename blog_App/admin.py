from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') # campos de solo lectura

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated') # campos de solo lectura

admin.site.register(Categoria,CategoriaAdmin) # se registra en el panel de administración
admin.site.register(Post, PostAdmin) # se registra en el panel de administración
 