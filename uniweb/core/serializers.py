from .models import Camara
from .models import Avistamientom
from rest_framework import serializers


class CamaraSerializer(serializers.HyperlinkedModelSerializer):
    finca_fk = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Camara
        fields = ['id', 'nombre_camara', 'ubicacion_latitud', 'ubicacion_longitud', 'finca_fk']


class AvistamientoMSerializer(serializers.HyperlinkedModelSerializer):
    finca_fk = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    camara_fk = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    especie_fk = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Avistamientom
        #fields = ['id', 'camara_fk', 'no_de_individuos', 'temperatura', 'fecha_avistamiento', 'hora_avistamientos', 'fase_lunar', 'memoria', 'video']
        fields = ['id', 'finca_fk', 'camara_fk', 'especie_fk', 'no_de_individuos', 'temperatura', 'fecha_avistamiento', 'hora_avistamientos', 'fase_lunar', 'memoria', 'video']