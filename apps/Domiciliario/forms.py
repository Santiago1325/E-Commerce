from django import forms
from apps.Domiciliario.models import Domiciliario

class DomiciliarioForm(forms.ModelForm):
    class Meta:
        model = Domiciliario
        fields = [
            'ID_Domiciliario',
            'Nombre',
            'Apellido',
        ]
        fields = {
            'ID_Domiciliario':'ID_Domiciliario',
            'Nombre':'Nombre',
            'Apellido':'Apellido',
        }
        widgets = {
            'ID_Domiciliario':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Apellido':forms.TextInput(attrs={'class':'form-control'}),
        }