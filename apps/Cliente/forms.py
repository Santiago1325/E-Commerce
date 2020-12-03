from django import forms
from apps.Cliente.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'Identificacion',
            'Nombre',
            'Apellido',
            'Correo',
            'Contraseña',
        ]
        fields = {
            'Identificacion': 'Identificacion',
            'Nombre': 'Nombre',
            'Apellido': 'Apellido',
            'Correo':'Correo',
            'Contraseña': 'Contraseña',
        }
        widgets = {
            'Identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Apellido': forms.TextInput(attrs={'class':'form-control'}),
            'Correo': forms.TextInput(attrs={'class':'form-control'}),
            'Contraseña': forms.TextInput(attrs={'class':'form-control'}),
        }