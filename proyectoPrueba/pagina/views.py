from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index( request ):
	return HttpResponse("""
		<h1>Hola Tripulantes</h1>



		""")


def peliculas( request ):
	return HttpResponse("""
		<h1 style="text-aling: center">Peliculas<h1>


		""")
