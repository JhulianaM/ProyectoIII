from tabnanny import verbose
from django.db import models

# Create your models here.
class Paciente(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    modalidad = models.CharField(max_length=100, verbose_name='Modalidad')
    fecha = models.DateTimeField()
    study = models.CharField(max_length=200, verbose_name='Study')
    series = models.CharField(max_length=200, verbose_name='Series')
    soap = models.CharField(max_length=200, verbose_name='Soap')
    
    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Modalidad: " + self.modalidad
        return fila
   # def delete(self, using=None, keep_parents=False):
    #    self.imagen.storage.delete(self.imagen.name)
     #   super().delete()