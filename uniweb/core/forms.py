from django import forms

from .models import Animal
from .models import Avistamiento
from .models import Genero
from .models import Especie
from .models import Finca
from .models import Camara
from .models import Avistamientom

class animalForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = (
			'nombre_animal',
			'nombre_latin',
			'descripcion',
			'region',
			'alimentacion')

class avistamientoForm(forms.ModelForm):
	class Meta:
		model = Avistamiento
		fields = (
			'cantidad',
			'fecha_avistamiento',
			'comentario',
			'animal_fk')

class generoForm(forms.ModelForm):
	class Meta:
		model = Genero
		fields = '__all__'

class especieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = '__all__'

class fincaForm(forms.ModelForm):
	class Meta:
		model = Finca
		fields = '__all__'

class camaraForm(forms.ModelForm):
	class Meta:
		model = Camara
		fields = '__all__'

class avistamientomForm(forms.ModelForm):
	class Meta:
		model = Avistamientom
		fields = '__all__'