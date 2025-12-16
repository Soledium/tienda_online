from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date
from .models import Insumo, Pedido
from .serializers import InsumoSerializer, PedidoSerializer

#1
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def insumo_list_create(request):
    if request.method == "GET":
        insumos = Insumo.objects.all().order_by('id')
        serializer = InsumoSerializer(insumos, many = True)
        return Response(serializer.data)
    
    serializer = InsumoSerializer(data = request.data)
    if serializer.is_valid():
        return Response(serializer.data, status =status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def insumo_detail(request, pk):
    try:
        insumo = Insumo.objects.get(pk=pk)
    except Insumo.DoesNotExist:
        return Response({"detail": "Insumo no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(InsumoSerializer(insumo).data)

    if request.method in ["PUT", "PATCH"]:
        partial = (request.method == "PATCH")
        serializer = InsumoSerializer(insumo, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    insumo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




#2
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def pedido_create(request):
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def pedido_update(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return Response({"detail": "Pedido no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    partial = (request.method == "PATCH")
    serializer = PedidoSerializer(pedido, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#3
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def pedidos_filtrar(request):
    qs = Pedido.objects.all().order_by("-fecha_pedido")

    desde = request.GET.get("desde")
    hasta = request.GET.get("hasta")
    estados = request.GET.getlist("estado")
    max_results = request.GET.get("max")

    if desde:
        d = parse_date(desde)
        if not d:
            return Response({"error": "Formato 'desde' inválido. Usa YYYY-MM-DD."}, status=400)
        qs = qs.filter(fecha_pedido__date__gte=d)

    if hasta:
        h = parse_date(hasta)
        if not h:
            return Response({"error": "Formato 'hasta' inválido. Usa YYYY-MM-DD."}, status=400)
        qs = qs.filter(fecha_pedido__date__lte=h)

    if estados:
        qs = qs.filter(estado__in=estados)

    if max_results:
        try:
            qs = qs[: int(max_results)]
        except ValueError:
            return Response({"error": "max debe ser un número"}, status=400)
    else:
        qs = qs[:20]

    return Response(PedidoSerializer(qs, many=True).data)
