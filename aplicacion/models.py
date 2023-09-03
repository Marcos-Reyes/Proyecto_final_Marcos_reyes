from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    numero=models.IntegerField()
    stock=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"


class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=50)  
    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.email}"  

class   Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    class Meta:
        verbose_name= "Proveedor"
        verbose_name_plural= "Proveedores"
        ordering=['-nombre']

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"