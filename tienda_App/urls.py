from django.urls import path
from tienda_App import views

urlpatterns = [
    path('',views.tienda,name='Tienda'),

    # path('categoria/<int:categoria_id>/', views.blog, name='posts_por_categoria'),  # Vista filtrada por categoría
]



