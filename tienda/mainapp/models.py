from django.db import models
import uuid
from django.utils import timezone

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
    SOLICITADO = 'Solicitado', 'SOLICITADO'  # pedido creado
    EN_PROCESO = 'En Proceso', 'EN PROCESO'
    APROBADO = 'Aprobado', 'APROBADO'
    REALIZADO = 'Realizado', 'REALIZADO'  # terminado para entrega
    ENTREGADO = 'Entregado', 'ENTREGADO'
    FINALIZADO = 'Finalizado', 'FINALIZADO'  # entregado y aceptado
    CANCELADO = 'Cancelado', 'CANCELADO'


class Pedido(models.Model):
    ESTADOS_PAGO = [
        ('Pendiente', 'PENDIENTE'),
        ('Completado', 'COMPLETADO'),    
        ('Parcial', 'PARCIAL'),
    ]

    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Link de seguimiento")

    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,null=True,blank=True
    )

    estado = models.CharField(max_length=50)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    nombre_cliente = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripción de lo solicitado")

    imagen_ref1 = models.ImageField(upload_to='pedidos/', null=True, blank=True)
    imagen_ref2 = models.ImageField(upload_to='pedidos/', null=True, blank=True)
    imagen_ref3 = models.ImageField(upload_to='pedidos/', null=True, blank=True)

    fecha_necesita = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha en que necesita el producto"
    )
    plataforma = models.ForeignKey(
        'Plataforma',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    estado_pago = models.CharField(
        max_length=20,
        choices=ESTADOS_PAGO,
        default='Pendiente'
    )

    def __str__(self):
        return f"Pedido de {self.producto or 'sin producto'} el {self.fecha_pedido.strftime('%Y-%m-%d')}"


class Plataforma(models.Model):
    PLATAFORMAS = [
        ('Instagram', 'INSTAGRAM'), 
        ('Facebook', 'FACEBOOK'), 
        ('TikTok', 'TIKTOK'), 
        ('WhatsApp', 'WHATSAPP'),]

    nombre = models.CharField(max_length=50,unique=True, choices=PLATAFORMAS, verbose_name="Plataforma de origen del pedido")

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    proveedor = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    

class Seguimiento(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def ha_expirado(self):
        expiration_time = self.fecha_creacion + timezone.timedelta(hours=48)
        return timezone.now() > expiration_time

    def __str__(self):
        return f"Seguimiento para {self.pedido} - Token: {self.token}"
