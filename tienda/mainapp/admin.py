from django.contrib import admin
from .models import Producto, Categoria, Insumo

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'proveedor')
    search_fields = ('nombre', 'proveedor') 
