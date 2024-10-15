from django.shortcuts import render, get_object_or_404
from blog_App.models import Post, Categoria

# Create your views here.

def blog(request, categoria_id=None):
    categorias=Categoria.objects.all()

    if categoria_id:
        categoria=get_object_or_404(Categoria,id=categoria_id)
        post=Post.objects.filter(categoria=categoria)
    else:
        post=Post.objects.all()
    return render(request,'blog/blog.html',{'categoria':categoria if categoria_id else None,'post':post, 'categorias':categorias})
