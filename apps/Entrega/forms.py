from django import forms
from apps.Entrega.models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = [
            'ID_Entrega',
            'Fecha',
            'ID_Direccion',
            'ID_Domiciliario'
        ]

        widgets = {
           'ID_Entrega':forms.TextInput(),
            'Fecha':forms.TextInput(),
            'ID_Direccion':forms.TextInput(),
            'ID_Domiciliario':forms.TextInput(),
        }
