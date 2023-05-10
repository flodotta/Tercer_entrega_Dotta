from django.db import models

# Create your models here.
# Creo 4 clases: Lector, Escritor, Articulo

#creo la clase lector
class Lector(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True)

#le agrego el método mágico str para visualizarlo bien en el panel admin
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

#Creo la clase Escritor    
class Escritor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)    

    class Meta: 
        verbose_name_plural = "Escritores"

 #le agrego el método mágico str para visualizarlo bien en el panel admin
    def __str__(self):
        return f"{self.apellido} / {self.nombre} / {self.fecha_nacimiento}"

#Creo la clase articulo
class Articulo(models.Model):
    nombre = models.CharField(max_length=256)
    codigo = models.CharField(max_length=20)
    categoria = models.CharField(max_length=256)
    fecha_publicacion = models.DateField(null=True)
  
  #le agrego el método mágico str para visualizarlo bien en el panel admin
    def __str__(self):
        return f"{self.nombre}, {self.categoria}, {self.fecha_publicacion}"
