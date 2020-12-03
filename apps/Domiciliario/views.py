from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from apps.Domiciliario.models import Domiciliario
from apps.Domiciliario.forms import DomiciliarioForm
from django.shortcuts import render

def consultarDomiciliario(request):
    domiciliarios = Domiciliario.objects.all()
    contexto = {'domiciliarios':domiciliarios}
    return render(request, 'consulta/consultar_dom.html', contexto)

def crearDomiciliario(request):
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST)
        form.save()
    else:
        form = DomiciliarioForm()
    return render(request, 'registro/crearDomiciliario.html', {'form':form})

def editarDom(request,id_dom):
    domiciliario = Domiciliario.objects.get(ID_Domiciliario=id_dom)
    contexto = {'domiciliario':domiciliario}
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST, instance=domiciliario)
        if form.is_valid():
            form.save()
        return consultarDomiciliario(request)
    else:
        form = DomiciliarioForm(instance=domiciliario)
        return render(request, 'edicion/editarDom.html',{'form':form})




def eliminarDom(request, id_dom):
    domiciliario = Domiciliario.objects.get(ID_Domiciliario=id_dom)
    if request.method == 'POST':
        domiciliario.delete()
        return consultarDomiciliario(request)
    else:
        return render(request, 'edicion/eliminarDom.html',{'domiciliario':domiciliario})

