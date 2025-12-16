from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Insumo
from .serializers import InsumoSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by('id')
    serializer_class = InsumoSerializer
    permission_classes = [IsAuthenticated]
    