from django.contrib import admin
from .models import Producto, Categoria, Insumo, Pedido

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'fecha_pedido', 'estado')
    list_filter = ('fecha_pedido', 'estado')
    search_fields = ('cliente__nombre', 'cliente__email')


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'proveedor')
    prepopulated_fields = {'slug': ['nombre']}
    search_fields = ('producto_nombre', 'token') 