from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    titulo=models.CharField(max_length=50)
    # contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    precio=models.FloatField(max_length=10)
    # autor=models.ForeignKey(User, on_delete=models.CASCADE) # Relación Uno a Muchas. 
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) # Relación Muchos a Muchos. Permite borrar de todas las categorias.
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.titulo