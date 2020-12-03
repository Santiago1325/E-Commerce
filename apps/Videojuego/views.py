from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from apps.Videojuego.models import Videojuego
from apps.Videojuego.forms import VideojuegoForm
# Create your views here.

def consultarJuegos(request):
    videojuegos = Videojuego.objects.all()
    contexto = {'videojuegos':videojuegos}
    return render(request, 'consulta/consultar_vj.html', contexto)


def editarJuego(request,id_j):
    videojuego = Videojuego.objects.get(Codigo=id_j)
    contexto = {'videojuegos':videojuego}
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
        return consultarJuegos(request)
    else:
        form = VideojuegoForm(instance=videojuego)
        return render(request, 'edicion/editarJuego.html',{'form':form})

def crearJuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        form.save()
    else:
        form = VideojuegoForm()
    return render(request, 'registro/crearJuego.html', {'form':form})

def eliminarJuego(request, id_j):
    videojuego = Videojuego.objects.get(Codigo=id_j)
    if request.method == 'POST':
        videojuego.delete()
        return consultarJuegos(request)
    else:
        return render(request, 'edicion/eliminarJuego.html',{'videojuego':videojuego})