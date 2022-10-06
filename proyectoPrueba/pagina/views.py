from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import usuarios
from django.utils import timezone
from django.urls import reverse

def index( request ):
	_usuarios = usuarios.objects.all()

	return render( request, 'pagina/index.html')

def todosLosUsuarios( request ):
	_usuarios = usuarios.objects.all()

	return render( request, 'pagina/todosLosUsuarios.html',{
			'usuarios': _usuarios
		})

def registrarUsuario( request ):

	try:

		nombre = request.POST['nombre']
		contrasenia = request.POST['nombre']
		edad = request.POST['nombre']
		dia_registro = timezone.now()
	except:
		return HttpResponse("Error")
	else:
		nuevoUsuario = usuarios( 
			nombre=nombre, 
			edad=edad,
			dia_registro=dia_registro,
			contrasenia=contrasenia)
		nuevoUsuario.save()
		return 	HttpResponseRedirect( reverse( "pagina:index" ) )	


def vistaRegistroUsuario( request ):
	return render( request, 'pagina/registrarse.html')
