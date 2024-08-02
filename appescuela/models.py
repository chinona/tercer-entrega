from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre= models.CharField(max_length= 30) #charfield genera un string, siempre se debe poner un maximo de longitud dentro
    comision= models.IntegerField(null=True) #integerfield pide un numero entero, esto que pedimos en el "models.---" es el tipo de dato que guardamo en la base de datos

class Estudiante(models.Model):
    nombre= models.CharField(max_length= 30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length= 30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Entregable(models.Model):
    nombre=models.CharField(max_length= 30)
    fecha_de_entrega= models.DateField()
    entregado= models.BooleanField()