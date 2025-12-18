from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, generics
from django.utils.dateparse import parse_date
from .models import Insumo, Pedido
from .serializers import InsumoSerializer, PedidoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#1
class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by('id')
    serializer_class = InsumoSerializer
    permission_classes = [IsAuthenticated]



#2
@method_decorator(csrf_exempt, name = "dispatch")
class PedidoList(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer 
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
@method_decorator(csrf_exempt, name = "dispatch")
class PedidoDetail(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        return self.update(request , *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request , *args, **kwargs)



#3
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def pedidos_filtrar(request):
    solicitud = Pedido.objects.all().order_by("-fecha_pedido")

    desde = request.GET.get("desde")
    hasta = request.GET.get("hasta")
    estados = request.GET.getlist("estado")
    max_results = request.GET.get("max")

    if desde:
        des = parse_date(desde)
        if not des:
            return Response({"error": "Formato 'desde' inválido. Usa YYYY-MM-DD."}, status=400)
        solicitud = solicitud.filter(fecha_pedido__date__gte=des)

    if hasta:
        has = parse_date(hasta)
        if not has:
            return Response({"error": "Formato 'hasta' inválido. Usa YYYY-MM-DD."}, status=400)
        solicitud = solicitud.filter(fecha_pedido__date__lte=has)

    if estados:
        solicitud = solicitud.filter(estado__in=estados)

    if max_results:
        try:
            solicitud = solicitud[: int(max_results)]
        except ValueError:
            return Response({"error": "max debe ser un número"}, status=400)
    else:
        solicitud = solicitud[:20]

    return Response(PedidoSerializer(solicitud, many=True).data)


