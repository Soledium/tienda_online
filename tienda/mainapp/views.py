from django.shortcuts import render
from .models import Producto
# Create your views here.

def productos(request):
    lista_productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': lista_productos})