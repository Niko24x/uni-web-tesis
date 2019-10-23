from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin
from django.urls import path, include

from .views import home
from .views import listaAnimal, crearAnimal, actualizarAnimal
from .views import listaAvistamiento, crearAvistamiento, actualizarAvistamiento
from .views import listaGenero, crearGenero, actualizarGenero
from .views import listaEspecie, crearEspecie, actualizarEspecie
from .views import listaFinca, crearFinca, actualizarFinca
from .views import listaCamara, crearCamara, actualizarCamara
from .views import listaAvistamientom, crearAvistamientom, actualizarAvistamientom
                    
app_name = 'core'
urlpatterns = [
 	#Avistamiento
   path('avistamiento/', login_required(listaAvistamiento.as_view()), name='listaAvistamiento'),
   path('avistamiento/crear/', login_required(crearAvistamiento.as_view()), name='crearAvistamiento'),
   path('avistamiento/<pk>/act/', login_required(actualizarAvistamiento.as_view()), name='actualizarAvistamiento'),

   #Nit
   path('animal/', login_required(listaAnimal.as_view()), name='listaAnimal'),
   path('animal/crear', login_required(crearAnimal.as_view()), name='crearAnimal'),
   path('animal/<pk>/act/', login_required(actualizarAnimal.as_view()), name='actualizarAnimal'),   

   #Genero
   path('genero/', login_required(listaGenero.as_view()), name='listaGenero'),
   path('genero/crear', login_required(crearGenero.as_view()), name='crearGenero'),
   path('genero/<pk>/act/', login_required(actualizarGenero.as_view()), name='actualizarGenero'),   

   #Especie
   path('especie/', login_required(listaEspecie.as_view()), name='listaEspecie'),
   path('especie/crear', login_required(crearEspecie.as_view()), name='crearEspecie'),
   path('especie/<pk>/act/', login_required(actualizarEspecie.as_view()), name='actualizarEspecie'),   

   #Finca
   path('finca/', login_required(listaFinca.as_view()), name='listaFinca'),
   path('finca/crear', login_required(crearFinca.as_view()), name='crearFinca'),
   path('finca/<pk>/act/', login_required(actualizarFinca.as_view()), name='actualizarFinca'),   

   #Camara
   path('camara/', login_required(listaCamara.as_view()), name='listaCamara'),
   path('camara/crear', login_required(crearCamara.as_view()), name='crearCamara'),
   path('camara/<pk>/act/', login_required(actualizarCamara.as_view()), name='actualizarCamara'),   

   #AvistamientoM
   path('avistamientom/', login_required(listaAvistamientom.as_view()), name='listaAvistamientoM'),
   path('avistamientom/crear', login_required(crearAvistamientom.as_view()), name='crearAvistamientoM'),
   path('avistamientom/<pk>/act/', login_required(actualizarAvistamientom.as_view()), name='actualizarAvistamientoM'),   
]
