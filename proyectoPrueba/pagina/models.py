from django.db import models

# Create your models here.


#Relacion 1 a muchos

class Usuario( models.Model ):
	nombre = models.CharField( max_length = 50 )
	contrasenia = models.CharField( max_length = 15 )
	dia_registro = models.DateTimeField("Dia registro")

	def __str__(self):
		return self.nombre


class Tarea( models.Model ):
	usuario = models.ForeignKey( Usuario, on_delete=models.CASCADE )
	nombreTarea = models.CharField( max_length = 60)
	estado = models.BooleanField( default = False )
	inicio = models.DateTimeField('Dia de inicio')
	finalizar = models.DateTimeField('Plazo maximo')

	def __str__(self):
		return self.nombreTarea