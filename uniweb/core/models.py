from django.db import models
from django.urls import reverse

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_animal = models.CharField('Nombre Animal', help_text='*', max_length = 64, blank=False)
    nombre_latin = models.CharField('Nombre Latin', max_length = 64, null=True, blank=True)
    descripcion = models.CharField('Descripcion', max_length = 64, null=True, blank=True)
    region = models.CharField('Region', help_text='*', max_length = 64, blank=False)
    alimentacion = models.CharField('Alimentacion', max_length = 64, null=True, blank=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animal'

    def __str__(self):
        #return self.id
        return str('%s - %s')%(self.nombre_animal, self.nombre_latin)

    def get_absolute_url(self):
        return reverse("core:home")     
    
########################################################################

#Tablas Hijas

class Avistamiento(models.Model):
    id = models.AutoField(primary_key=True)
    #direccionPersona = models.CharField('Direccion', help_text='*', max_length=100, blank=False)
    cantidad = models.CharField('Cantidad',max_length=128)
    fecha_avistamiento = models.DateField('Fecha de avistamiento')
    comentario = models.CharField('Comentario', max_length=100, help_text='*', blank=False)
    animal_fk = models.ForeignKey(Animal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animal"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("core:home")

#Cambios finales

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField('Nombre Genero', max_length = 64, null=True, blank=True)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.nombre_genero

    def get_absolute_url(self):
        return reverse("core:listaGenero")

class Especie(models.Model):
    id = models.AutoField(primary_key=True)
    genero_fk = models.ForeignKey(Genero, on_delete=models.CASCADE)
    nombre_especie = models.CharField('Nombre Especie', max_length = 64, null=True, blank=True)
    clase = models.CharField(max_length = 64, null=True, blank=True)#form
    dieta = models.CharField(max_length = 64, null=True, blank=True)#form

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"

    def __str__(self):
        return self.nombre_especie

    def get_absolute_url(self):
        return reverse("core:listaEspecie")

class Finca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_finca = models.CharField('Nombre Finca', max_length = 64, null=True, blank=True)

    class Meta:
        verbose_name = "Finca"
        verbose_name_plural = "Fincas"

    def __str__(self):
        return self.nombre_finca

    def get_absolute_url(self):
        return reverse("core:listaFinca")

class Camara(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_camara = models.CharField('Nombre Camara', max_length = 64, null=True, blank=True)
    ubicacion_latitud = models.CharField('Ubicacion Latitud', max_length = 64, null=True, blank=True)
    ubicacion_longitud = models.CharField('Ubicacion Longitud', max_length = 64, null=True, blank=True)
    finca_fk = models.ForeignKey(Finca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Camara"
        verbose_name_plural = "Camaras"

    def __str__(self):
        return self.nombre_camara

    def get_absolute_url(self):
        return reverse("core:listaCamara")

class Avistamientom(models.Model):
    id = models.AutoField(primary_key=True)
    finca_fk = models.ForeignKey(Finca, on_delete=models.CASCADE)
    camara_fk = models.ForeignKey(Camara, on_delete=models.CASCADE)
    especie_fk = models.ForeignKey(Especie, on_delete=models.CASCADE)
    no_de_individuos = models.IntegerField('Numero de Individuos',null=True, blank=True)
    temperatura = models.IntegerField('Temperatura',null=True, blank=True)
    fecha_avistamiento = models.DateField('Fecha de avistamiento')
    hora_avistamientos = models.TimeField('Hora de avistamientos')
    fase_lunar = models.CharField('Fase Lunar', max_length = 64, null=True, blank=True)#form
    memoria = models.CharField('Memoria', max_length = 64, null=True, blank=True)
    video = models.CharField('Video', max_length = 64, null=True, blank=True)

    class Meta:
        verbose_name = "Avistamiento"
        verbose_name_plural = "Avistamientos"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:listaAvistamientoM")
