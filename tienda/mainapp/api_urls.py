from django.urls import path
from . import api_views

urlpatterns = [
    path("insumos/", api_views.insumo_list_create, name="api_insumo_list_create"),
    path("insumos/<int:pk>/", api_views.insumo_detail, name="api_insumo_detail"),

    path("pedidos/", api_views.pedido_create, name="api_pedido_create"),
    path("pedidos/<int:pk>/", api_views.pedido_update, name="api_pedido_update"),

    path("pedidos/filtrar/", api_views.pedidos_filtrar, name="api_pedidos_filtrar"),
]

