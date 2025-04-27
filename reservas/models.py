from django.contrib.auth.models import User, Group
from django.db import models

# Extensión del usuario para asignarle un grupo
class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  

    def __str__(self) -> str:
        return self.user.username # pylint: disable=no-member

# Modelo para las clases del gimnasio
class Clase(models.Model):
    id = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cupo_maximo = models.IntegerField()
    fecha_hora = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.nombre)

# Modelo para las reservas de clases
class Reserva(models.Model):
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    clase = models.ForeignKey("Clase", on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.usuario.username} - {self.clase.nombre}" # pylint: disable=no-member
