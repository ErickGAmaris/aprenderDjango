from django.db import models

# Create your models here.


#Relacion 1 a muchos

class usuarios( models.Model ):
	#id primary key

	#nombre varchar
	nombre = models.CharField( max_length = 50 )
	#contrasenia varchar
	contrasenia = models.CharField( max_length = 15 )
	#dia_registro datetime
	dia_registro = models.DateTimeField("Dia registro")
	#edad
	edad = models.IntegerField()

	#metodo constructor
	# def __init__(self):
	# 	pass

	def __str__(self):
		return "Usuario: " + self.nombre


class peliculas( models.Model ):
	user = models.ForeignKey( usuarios, on_delete=models.CASCADE )
	nombre = models.CharField( max_length = 60)
	anios = models.DateTimeField("Anio de lanzamiento")