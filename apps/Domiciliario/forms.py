from django import forms
from apps.Domiciliario.models import Domiciliario

class DomiciliarioForm(forms.ModelForm):
    class Meta:
        model = Domiciliario
        fields = [
            'ID_Domiciliario',
            'Nombre',
            'Apellido',
            'Placa_Vehiculo'
        ]

        widgets = {
            'ID_Domiciliario':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Apellido':forms.TextInput(attrs={'class':'form-control'}),
            'Placa_Vehiculo':forms.TextInput(attrs={'class':'form-control'}),
        }