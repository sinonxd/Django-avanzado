from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, ClaseViewSet,ClaseList, ClaseDetail, ReservaList, ReservaDetail

# Crear el router y registrar el ViewSet
router = DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clases', ClaseViewSet)  


# Incluir las rutas del router en las URLs de la aplicación
urlpatterns = [
    path('api/', include(router.urls)),  

    # Endpoints para Clase
    path('clases/', ClaseList.as_view(), name='clase-list'),
    path('clases/<int:pk>/', ClaseDetail.as_view(), name='clase-detail'),

    # Endpoints para Reserva
    path('reservas/', ReservaList.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
]
