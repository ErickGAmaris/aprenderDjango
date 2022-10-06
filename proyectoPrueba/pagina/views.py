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
		contrasenia = request.POST['contrasenia']
		edad = request.POST['edad']
	except:
		return HttpResponse('Error')
	else:
		usuarios(nombre=nombre, edad=edad, contrasenia=contrasenia, dia_registro=timezone.now()).save()
		return HttpResponseRedirect( reverse( 'pagina:index' ) )

def vistaRegistroUsuario( request ):
	return render( request, 'pagina/registrarse.html')
