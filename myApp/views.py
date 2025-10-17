from django.shortcuts import render
from .models import Categoria, Producto

def principal(request):
    productos = Producto.objects.all()
    return render(request, "main.html", {"productos": productos})

def categorias(request):
    context = {}
    categorias = Categoria.objects.all()
    context['categorias'] = categorias
    return render(request, 'categorias.html', context)

def producto_detalle(request,id):
    context = {}
    producto = Producto.objects.get(id=id)
    context['producto'] = producto
    return render(request, 'producto_detalle.html', context)

def categoria_detalle(request, id):
    categoria = Categoria.objects.get(id=id)
    productos = Producto.objects.filter(categoria=categoria)
    context = {'categoria': categoria,'productos': productos}
    return render(request, 'categoria_detalle.html', context)
