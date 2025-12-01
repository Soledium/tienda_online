from django.contrib import admin
from .models import Producto, Categoria, Insumo, Pedido
from django.utils.html import format_html

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'producto', 'fecha_pedido', 'estado', 'token')
    list_filter = ('fecha_pedido', 'estado')
    search_fields = ('nombre_cliente', 'email',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'vista_imagen',)
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)

    def vista_imagen(self, obj):
        if obj.imagen:
            return format_html ('<img src="{}" width="100" height="100" />', obj.imagen.url)
        return "Sin imagen de referencia"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion',)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad')
    search_fields = ('nombre',) 

