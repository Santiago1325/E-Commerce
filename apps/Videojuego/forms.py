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
            'ID_Admin',
            'ID_Clasificacion_de_edad',
            'ID_Desarrollador',
            'ID_Franquicia',
            'ID_Plataforma',
        ]

        widgets = {
            'Codigo': forms.TextInput(attrs={'class':'form-control'}),
            'Multijugador':forms.TextInput(attrs={'class':'form-control'}),
            'Costo':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'ID_Admin': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Clasificacion_de_edad': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Desarrollador': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Franquicia': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Plataforma': forms.TextInput(attrs={'class':'form-control'}),
        }