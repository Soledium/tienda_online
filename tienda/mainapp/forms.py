from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nombre_cliente',
            'email',
            'telefono',
            'producto',
            'descripcion',
            'imagen_ref1',
            'imagen_ref2',
            'imagen_ref3',
            'fecha_necesita',
        ]
        widgets = {
            'fecha_necesita': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
