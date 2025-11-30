from django.shortcuts import render
from .models import Producto
# Create your views here.

def home(request):
    categorias = [
        {
            'nombre': 'TAZONES',
            'url_name': 'tazones',
            'imagen': 'carrusel/tazon.webp',
        },
        {
            'nombre': 'POLERAS',
            'url_name': 'poleras',
            'imagen': 'carrusel/polera.jpg',
        },
        {
            'nombre': 'POLERONES',
            'url_name': 'polerones',
            'imagen': 'carrusel/poleron.jpg',
        },
        {
            'nombre': 'ZAPATILLAS',
            'url_name': 'zapatillas',
            'imagen': 'carrusel/zapatillas.webp',
        },
    ]
    data = {
        'categorias': categorias,
    }
    return render(request, 'home.html', data)


def tazones(request):
    data = {
        'categoria' : 'TAZONES',
        'productos' : [
                    {'nombre': 'Tazon 1', 'precio': 10.99, 'imagen':'categorias/tazones/tazon1.jpg'},
                    {'nombre': 'Tazon 2', 'precio': 12.99, 'imagen':'categorias/tazones/tazon2.jpeg'},
                    {'nombre': 'Tazon 3', 'precio': 9.99, 'imagen':'categorias/tazones/tazon3.jpeg'},
                    {'nombre': 'Tazon 4', 'precio': 11.99, 'imagen':'categorias/tazones/tazon4.jpeg'},
                    {'nombre': 'Tazon 5', 'precio': 14.99, 'imagen':'categorias/tazones/tazon5.jpeg'},
                    {'nombre': 'Tazon 6', 'precio': 8.99, 'imagen':'categorias/tazones/tazon6.jpeg'},
                    {'nombre': 'Tazon 7', 'precio': 11.99, 'imagen':'categorias/tazones/tazon7.jpeg'},
                    {'nombre': 'Tazon 8', 'precio': 14.99, 'imagen':'categorias/tazones/tazon8.jpeg'},
                    {'nombre': 'Tazon 9', 'precio': 8.99, 'imagen':'categorias/tazones/tazon9.jpeg'},
                    ]
    }
    return render(request, 'categoria.html', data)

def poleras(request):
    data = {
        'categoria' : 'POLERAS',
        'productos' : [
                    {'nombre': 'Polera 1', 'precio': 10.99},
                    {'nombre': 'Polera 2', 'precio': 12.99},
                    {'nombre': 'Polera 3', 'precio': 9.99},
                    {'nombre': 'Polera 4', 'precio': 11.99},
                    {'nombre': 'Polera 5', 'precio': 14.99},
                    {'nombre': 'Polera 6', 'precio': 8.99},
                    {'nombre': 'Polera 3', 'precio': 9.99},
                    {'nombre': 'Polera 4', 'precio': 11.99},
                    {'nombre': 'Polera 5', 'precio': 14.99},
                    ]
    }
    return render(request, 'categoria.html', data)

def polerones(request):
    data = {
        'categoria' : 'POLERONES',
        'productos' : [
                    {'nombre': 'Polerón 1', 'precio': 10.99},
                    {'nombre': 'Polerón 2', 'precio': 12.99},
                    {'nombre': 'Polerón 3', 'precio': 9.99},
                    {'nombre': 'Polerón 4', 'precio': 11.99},
                    {'nombre': 'Polerón 5', 'precio': 14.99},
                    {'nombre': 'Polerón 6', 'precio': 8.99},
                    ]
    }
    return render(request, 'categoria.html', data)

def zapatillas(request):
    data = {
        'categoria' : 'ZAPATILLAS',
        'productos' : [
                    {'nombre': 'Zapatilla 1', 'precio': 10.99},
                    {'nombre': 'Zapatilla 2', 'precio': 12.99},
                    {'nombre': 'Zapatilla 3', 'precio': 9.99},
                    {'nombre': 'Zapatilla 4', 'precio': 11.99},
                    {'nombre': 'Zapatilla 5', 'precio': 14.99},
                    {'nombre': 'Zapatilla 6', 'precio': 8.99},
                    ]
    }
    return render(request, 'categoria.html', data)