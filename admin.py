from django.contrib import admin
from .models import UserProfile, Clase, Reserva

admin.site.register(UserProfile)
admin.site.register(Clase)
admin.site.register(Reserva)