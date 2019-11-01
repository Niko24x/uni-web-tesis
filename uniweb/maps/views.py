from django.shortcuts import render
from itertools import chain
from core.models import Avistamientom, Camara, Finca, Camara, Avistamientom

def default_map(request):

    class itemCamara(object):
        def __init__(self, ids, nombre_camara, ubicacion_latitud, ubicacion_longitud, listadoAvistamientos=0):
            self.id = ids
            self.nombre_camara = nombre_camara
            self.ubicacion_latitud = ubicacion_latitud
            self.ubicacion_longitud  = ubicacion_longitud
            self.listadoAvistamientos = listadoAvistamientos

    listaAvistamiento = Avistamientom.objects.all()

    cantFincas = Finca.objects.count()
    cantCamaras = Camara.objects.count()
    cantAvistamiento = Avistamientom.objects.count()

    listaCamaras = Camara.objects.all()
    listaItemCamara = []
    for cam in listaCamaras:
        avistamientoResult = Avistamientom.objects.filter(camara_fk=cam.id)
        listaItemCamara.append(itemCamara(cam.id, cam.nombre_camara, cam.ubicacion_latitud, cam.ubicacion_longitud, avistamientoResult))

    for cami in listaItemCamara:
        print(cami.id)
        print(cami.nombre_camara)
        print(cami.listadoAvistamientos)
        print("----------------------")

    return render(request, 'base/maps/defaultclick.html', { 
            'consulta': listaAvistamiento, 'firstValue': listaItemCamara[0],  'cantFincas': cantFincas,
            'cantCamaras': cantCamaras, 'cantAvistamiento': cantAvistamiento, 'listaItemCamara': listaItemCamara
        })