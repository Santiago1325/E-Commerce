from django import forms
from apps.Videojuego.models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = [
            'Codigo',
            'Multijugador',
            'Costo',
            'Nombre',
        ]
        fields = {
            'Codigo':'Codigo',
            'Multijugador':'Multijugador',
            'Costo':'Costo',
            'Nombre':'Nombre',
        }
        widgets = {
            'Codigo': forms.TextInput(attrs={'class':'form-control'}),
            'Multijugador':forms.TextInput(attrs={'class':'form-control'}),
            'Costo':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
        }