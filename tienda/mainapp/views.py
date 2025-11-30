from django.shortcuts import render
from .models import Producto
# Create your views here.

def home(request):
    return render(request, 'home.html')

def tazones(request):
    return render(request, 'categorias.html')

def poleras(request):
    return render(request, 'categorias.html')

def polerones(request):
    return render(request, 'categorias.html')

def zapatillas(request):
    return render(request, 'categorias.html')