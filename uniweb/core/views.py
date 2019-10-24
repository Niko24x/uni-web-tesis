from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Animal
from .forms import animalForm
from .models import Avistamiento
from .forms import avistamientoForm
from .models import Genero
from .forms import generoForm
from .models import Especie
from .forms import especieForm
from .models import Finca
from .forms import fincaForm
from .models import Camara
from .forms import camaraForm
from .models import Avistamientom
from .forms import avistamientomForm

from django.views.generic import (ListView,
    CreateView, 
	UpdateView, 
	DeleteView)

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

### Inicia Animal ###

class listaAnimal(ListView):
    model = Animal
    template_name = 'base/animal/listaAnimal.html'
    context_object_name = 'Animal' 

class crearAnimal(CreateView):
    model = Animal
    form_class = animalForm
    template_name = 'base/animal/formAnimal.html'
    success_url = reverse_lazy('core:listaAnimal')
    
class actualizarAnimal(UpdateView):
    model = Animal
    form_class = animalForm
    template_name = 'base/animal/formAnimal.html'
    success_url = reverse_lazy('core:listaAnimal')

class eliminarAnimal(DeleteView):
    model = Animal
    form_class = animalForm

### Termina Animal ###

### Inicia Avistamiento

class listaAvistamiento(ListView):
    model = Avistamiento
    template_name = 'base/avistamiento/listaAvistamiento.html'
    context_object_name = 'Avistamientos'

class crearAvistamiento(CreateView):
    model = Avistamiento
    form_class = avistamientoForm
    template_name = 'base/avistamiento/formAvistamiento.html'
    success_url = reverse_lazy('core:listaAvistamiento')
    
class actualizarAvistamiento(UpdateView):
    model = Avistamiento
    form_class = avistamientoForm
    template_name = 'base/avistamiento/formAvistamiento.html'
    success_url = reverse_lazy('core:listaAvistamiento')
    
### Termina Avistamiento

### Inicia Genero

class listaGenero(ListView):
    model = Genero
    template_name = 'base/genero/listaGenero.html'
    context_object_name = 'Generos'

class crearGenero(CreateView):
    model = Genero
    form_class = generoForm
    template_name = 'base/genero/formGenero.html'
    success_url = reverse_lazy('core:listaGenero')
    
class actualizarGenero(UpdateView):
    model = Genero
    form_class = generoForm
    template_name = 'base/genero/formGenero.html'
    success_url = reverse_lazy('core:listaGenero')
    
### Termina Genero

### Inicia Especie

class listaEspecie(ListView):
    model = Especie
    template_name = 'base/especie/listaEspecie.html'
    context_object_name = 'Especies'

class crearEspecie(CreateView):
    model = Especie
    form_class = especieForm
    template_name = 'base/especie/formEspecie.html'
    success_url = reverse_lazy('core:listaEspecie')
    
class actualizarEspecie(UpdateView):
    model = Especie
    form_class = especieForm
    template_name = 'base/especie/formEspecie.html'
    success_url = reverse_lazy('core:listaEspecie')
    
### Termina Especie

### Inicia Finca

class listaFinca(ListView):
    model = Finca
    template_name = 'base/finca/listaFinca.html'
    context_object_name = 'Avistamientos'

class crearFinca(CreateView):
    model = Finca
    form_class = fincaForm
    template_name = 'base/finca/formFinca.html'
    success_url = reverse_lazy('core:listaFinca')
    
class actualizarFinca(UpdateView):
    model = Finca
    form_class = fincaForm
    template_name = 'base/finca/formFinca.html'
    success_url = reverse_lazy('core:listaFinca')
    
### Termina Finca

### Inicia Camara

class listaCamara(ListView):
    model = Camara
    template_name = 'base/Camara/listaCamara.html'
    context_object_name = 'Avistamientos'

class crearCamara(CreateView):
    model = Camara
    form_class = camaraForm 
    template_name = 'base/Camara/formCamara.html'
    success_url = reverse_lazy('core:listaCamara')
    
class actualizarCamara(UpdateView):
    model = Camara
    form_class = camaraForm
    template_name = 'base/Camara/formCamara.html'
    success_url = reverse_lazy('core:listaCamara')
    
### Termina Camara

### Inicia Avistamientom

class listaAvistamientom(ListView):
    model = Avistamientom
    template_name = 'base/avistamientom/listaAvistamientom.html'
    context_object_name = 'Avistamientos'

class crearAvistamientom(CreateView):
    model = Avistamientom
    form_class = avistamientomForm
    template_name = 'base/avistamientom/formAvistamientom.html'
    success_url = reverse_lazy('core:listaAvistamientoM')
    
class actualizarAvistamientom(UpdateView):
    model = Avistamientom
    form_class = avistamientomForm
    template_name = 'base/avistamientom/formAvistamientom.html'
    success_url = reverse_lazy('core:listaAvistamientoM')
    
### Termina Avistamientom