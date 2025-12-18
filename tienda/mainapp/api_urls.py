from django.urls import path, include
from mainapp import api_views
from rest_framework.routers import DefaultRouter
from .api_views import InsumoViewSet


router = DefaultRouter()
router.register('insumos', InsumoViewSet, basename = 'insumo')


urlpatterns = [
    
    path('', include(router.urls)),
    path("pedidos/", api_views.PedidoList.as_view()),
    path("pedidos/<int:pk>/", api_views.PedidoDetail.as_view()),
    path("pedidos/filtrar/", api_views.pedidos_filtrar, name="api_pedidos_filtrar"),
    ]
    



