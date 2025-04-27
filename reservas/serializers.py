from rest_framework import serializers
from .models import Clase, Reserva  

class ClaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) 
    class Meta:
        model = Clase
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'  
