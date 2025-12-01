from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404
from .forms import PedidoForm
from .models import Pedido

def home(request):
    categorias = [
        {
            'nombre': 'Polerones',
            'url_name': 'polerones',
            'imagen': 'categorias/polerones/poleron1.jpeg',
        },
        {
            'nombre': 'Poleras',
            'url_name': 'poleras',
            'imagen': 'categorias/poleras/polera1.jpeg',
        },
        {
            'nombre': 'Zapatillas',
            'url_name': 'zapatillas',
            'imagen': 'categorias/zapatillas/zapatilla1.jpeg',
        },
        {
            'nombre': 'Tazones',
            'url_name': 'tazones',
            'imagen': 'categorias/tazones/tazon1.jpg',
        },
    ]

    data = {
        'categorias': categorias,
    }
    return render(request, 'home.html', data)


def tazones(request):
    data = {
        'categoria': 'TAZONES',
        'productos': [
            {'nombre': 'Tazon 1', 'precio': 10.99, 'imagen': 'categorias/tazones/tazon1.jpg'},
            {'nombre': 'Tazon 2', 'precio': 12.99, 'imagen': 'categorias/tazones/tazon2.jpeg'},
            {'nombre': 'Tazon 3', 'precio': 9.99, 'imagen': 'categorias/tazones/tazon3.jpeg'},
            {'nombre': 'Tazon 4', 'precio': 11.99, 'imagen': 'categorias/tazones/tazon4.jpeg'},
            {'nombre': 'Tazon 5', 'precio': 14.99, 'imagen': 'categorias/tazones/tazon5.jpeg'},
            {'nombre': 'Tazon 6', 'precio': 8.99, 'imagen': 'categorias/tazones/tazon6.jpeg'},
            {'nombre': 'Tazon 7', 'precio': 11.99, 'imagen': 'categorias/tazones/tazon7.jpeg'},
            {'nombre': 'Tazon 8', 'precio': 14.99, 'imagen': 'categorias/tazones/tazon8.jpeg'},
            {'nombre': 'Tazon 9', 'precio': 8.99, 'imagen': 'categorias/tazones/tazon9.jpeg'},
        ]
    }
    return render(request, 'categoria.html', data)


def poleras(request):
    data = {
        'categoria': 'POLERAS',
        'productos': [
            {'nombre': 'Polera 1', 'precio': 10.99, 'imagen': 'categorias/poleras/polera1.jpeg'},
            {'nombre': 'Polera 2', 'precio': 12.99, 'imagen': 'categorias/poleras/polera2.jpeg'},
            {'nombre': 'Polera 3', 'precio': 9.99, 'imagen': 'categorias/poleras/polera3.jpeg'},
            {'nombre': 'Polera 4', 'precio': 11.99, 'imagen': 'categorias/poleras/polera4.jpeg'},
            {'nombre': 'Polera 5', 'precio': 14.99, 'imagen': 'categorias/poleras/polera5.jpeg'},
            {'nombre': 'Polera 6', 'precio': 8.99, 'imagen': 'categorias/poleras/polera6.jpeg'},
            {'nombre': 'Polera 7', 'precio': 9.99, 'imagen': 'categorias/poleras/polera7.jpeg'},
            {'nombre': 'Polera 8', 'precio': 11.99, 'imagen': 'categorias/poleras/polera8.jpeg'},
            {'nombre': 'Polera 9', 'precio': 14.99, 'imagen': 'categorias/poleras/polera9.jpeg'},
        ]
    }
    return render(request, 'categoria.html', data)


def polerones(request):
    data = {
        'categoria': 'POLERONES',
        'productos': [
            {'nombre': 'Polerón 1', 'precio': 10.99, 'imagen': 'categorias/polerones/poleron1.jpeg'},
            {'nombre': 'Polerón 2', 'precio': 12.99, 'imagen': 'categorias/polerones/poleron2.jpeg'},
            {'nombre': 'Polerón 3', 'precio': 9.99, 'imagen': 'categorias/polerones/poleron3.jpeg'},
            {'nombre': 'Polerón 4', 'precio': 11.99, 'imagen': 'categorias/polerones/poleron4.jpeg'},
            {'nombre': 'Polerón 5', 'precio': 14.99, 'imagen': 'categorias/polerones/poleron5.jpeg'},
            {'nombre': 'Polerón 6', 'precio': 8.99, 'imagen': 'categorias/polerones/poleron6.jpeg'},
            {'nombre': 'Polerón 7', 'precio': 9.99, 'imagen': 'categorias/polerones/poleron7.jpeg'},
            {'nombre': 'Polerón 8', 'precio': 11.99, 'imagen': 'categorias/polerones/poleron8.jpeg'},
            {'nombre': 'Polerón 9', 'precio': 14.99, 'imagen': 'categorias/polerones/poleron9.jpeg'},
        ]
    }
    return render(request, 'categoria.html', data)


def zapatillas(request):
    data = {
        'categoria': 'ZAPATILLAS',
        'productos': [
            {'nombre': 'Zapatilla 1', 'precio': 10.99, 'imagen': 'categorias/zapatillas/zapatilla1.jpeg'},
            {'nombre': 'Zapatilla 2', 'precio': 12.99, 'imagen': 'categorias/zapatillas/zapatilla2.jpeg'},
            {'nombre': 'Zapatilla 3', 'precio': 9.99, 'imagen': 'categorias/zapatillas/zapatilla3.jpeg'},
            {'nombre': 'Zapatilla 4', 'precio': 11.99, 'imagen': 'categorias/zapatillas/zapatilla4.jpeg'},
            {'nombre': 'Zapatilla 5', 'precio': 14.99, 'imagen': 'categorias/zapatillas/zapatilla5.jpeg'},
            {'nombre': 'Zapatilla 6', 'precio': 8.99, 'imagen': 'categorias/zapatillas/zapatilla6.jpeg'},
            {'nombre': 'Zapatilla 7', 'precio': 9.99, 'imagen': 'categorias/zapatillas/zapatilla7.jpeg'},
            {'nombre': 'Zapatilla 8', 'precio': 11.99, 'imagen': 'categorias/zapatillas/zapatilla8.jpeg'},
            {'nombre': 'Zapatilla 9', 'precio': 14.99, 'imagen': 'categorias/zapatillas/zapatilla9.jpeg'},
        ]
    }
    return render(request, 'categoria.html', data)


def pedidos(request):
    lista = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'pedidos.html', {'pedidos': lista})


def solicitar(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)

            pedido.estado = 'Solicitado'
            pedido.estado_pago = 'Pendiente'

            pedido.save()

            url_seguimiento = request.build_absolute_uri(
                reverse('seguimiento') + f'?token={pedido.token}'
            )

            context = {
                'pedido': pedido,
                'url_seguimiento': url_seguimiento,
            }
            return render(request, 'confirmacion.html', context)
    else:
        form = PedidoForm()

    return render(request, 'solicitud.html', {'form': form})


def seguimiento(request):
    pedido = None
    token_str = None

    if request.method == 'POST':
        token_str = request.POST.get('token')
    else:
        token_str = request.GET.get('token')

    if token_str:
        try:
            pedido = Pedido.objects.get(token=token_str)
        except Pedido.DoesNotExist:
            pedido = None

    context = {'pedido': pedido}
    if token_str and not pedido:
        context['mensaje'] = 'No se encontró ningún pedido con ese código.'

    return render(request, 'seguimiento.html', context)
