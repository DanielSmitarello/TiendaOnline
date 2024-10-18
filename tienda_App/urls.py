from django.urls import path
from tienda_App import views # . es una importanción relativa, propia desde la misma app. Podemos usar la  importación especifica cuando traemos desde otras app


urlpatterns = [

    path('',views.tienda,name='Tienda'),

    path('categoria/<int:categoria_id>/', views.tienda, name='productos_por_categoria'),  # Vista filtrada por categoría
]



