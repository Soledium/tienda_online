from django.db import models
import uuid

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class EstadoPedido(models.Model):
    SOLICITADO = 'Solicitado', 'SOLICITADO' #pedido creado
    EN_PROCESO = 'En Proceso', 'EN PROCESO'
    APROBADO = 'Aprobado', 'APROBADO'
    REALIZADO = 'Realizado', 'REALIZADO' #terminado para entrega
    ENTREGADO = 'Entregado', 'ENTREGADO'
    FINALIZADO = 'Finalizado', 'FINALIZADO' #entregado y aceptado
    CANCELADO = 'Cancelado', 'CANCELADO'  

class EstadoPago(models.Model):
    PENDIENTE = 'Pendiente', 'PENDIENTE'
    PARCIAL = 'Parcial', 'PARCIAL'
    PAGADO = 'Pagado', 'PAGADO'


class Pedido(models.Model):
    token = models.UUIDField(default = uuid.uuid4, editable=False, unique=True, verbose_name= "Link de seguimiento")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estado = models.CharField(max_length = 50)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.cantidad} x {self.producto.nombre} el {self.fecha_pedido}"


class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Plataforma del pedido")

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    talla = models.CharField(max_length=10, null=True, blank=True)
    cantidad = models.IntegerField()
    proveedor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre