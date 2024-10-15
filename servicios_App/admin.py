from django.contrib import admin
from .models import Servicios


# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicios, ServicioAdmin)

# Pone titulos en el panel de administración...

admin.site.site_header = "Panel de Administración de la Tienda Online" # titulo de la cabecera
admin.site.site_title = "Admin Tienda Tatito" # titulo 
admin.site.index_title = "Admin de la tienda Tatito" # titulo de pestaña

