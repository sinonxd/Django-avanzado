# pylint: disable=E1101
from rest_framework import viewsets
from rest_framework import generics
from .models import Clase, Reserva
from .serializers import ClaseSerializer, ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):  # Permite CRUD completo
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

# Vistas para el modelo Clase
class ClaseList(generics.ListCreateAPIView):  # GET (listar) y POST (crear)
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class ClaseDetail(generics.RetrieveUpdateDestroyAPIView):  # GET, PUT, PATCH, DELETE
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

# Vistas para el modelo Reserva
class ReservaList(generics.ListCreateAPIView):  # GET (listar) y POST (crear)
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):  # GET, PUT, PATCH, DELETE
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer