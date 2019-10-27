from django.shortcuts import render
from itertools import chain
from core.models import Avistamientom, Camara

def default_map(request):
    listaAvistamiento = Avistamientom.objects.all()
    return render(request, 'base/maps/default.html', { 'consulta': listaAvistamiento, 'firstValue': listaAvistamiento[0] })