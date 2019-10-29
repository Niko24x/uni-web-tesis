from django.shortcuts import render
from itertools import chain
from core.models import Avistamientom, Camara, Finca, Camara, Avistamientom

def default_map(request):
    listaAvistamiento = Avistamientom.objects.all()
    cantFincas = Finca.objects.count()
    cantCamaras = Camara.objects.count()
    cantAvistamiento = Avistamientom.objects.count()
    return render(request, 'base/maps/default.html', { 
            'consulta': listaAvistamiento, 'firstValue': listaAvistamiento[0],  'cantFincas': cantFincas,
            'cantCamaras': cantCamaras, 'cantAvistamiento': cantAvistamiento
        })