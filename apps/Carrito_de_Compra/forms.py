from django import forms
from apps.Carrito_de_Compra.models import Carrito_de_Compra
from apps.Cliente.models import Cliente
from apps.Domiciliario.models import Domiciliario

class CompraForm(forms.ModelForm):
    class Meta:
        model = Carrito_de_Compra
        fields = [
            'ID_Carrito',
            'ID_Domiciliario',
            'Identificacion_Cliente',
        ]

        widgets = {
            'ID_Carrito': forms.TextInput(),
            'ID_Domiciliario':forms.TextInput(),
            'Identificacion_Cliente': forms.TextInput(),
        }
