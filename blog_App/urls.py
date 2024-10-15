from django.urls import path
from blog_App import views

urlpatterns = [
    
    path('',views.blog,name='Blog'),
    path('categoria/<int:categoria_id>/', views.blog, name='posts_por_categoria'),  # Vista filtrada por categoría
    
]