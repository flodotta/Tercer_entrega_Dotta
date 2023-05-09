from django.db import models

# Create your models here.
# Creo 4 clases: Lector, Escritor, Articulo

 #   def __str__(self):
  #      return f"{self.apellido}, {self.nombre}"
class Lector(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    comision = models.IntegerField()  # Equivalent de int

class Escritor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)    

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

  #  def __str__(self):
   #     return f"{self.nombre}, {self.apellido}"
    
class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

   # def __str__(self):
    #    return f"{self.nombre} | {self.comision}"
