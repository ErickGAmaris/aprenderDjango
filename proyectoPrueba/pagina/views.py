from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from django.utils import timezone
from django.urls import reverse

def index( request ):
	usuarios = Usuario.objects.all()
	return render( request, 'pagina/index.html')

def todosLosUsuarios( request ):
	usuarios = Usuario.objects.all()

	return render( request, 'pagina/todosLosUsuarios.html',{
			'usuarios': usuarios
		})

def registrarUsuario( request ):
	try:
		nombre = request.POST['nombre']
		contrasenia = request.POST['contrasenia']
		edad = request.POST['edad']
	except:
		return HttpResponse('Error')
	else:
		usuario = Usuario(nombre=nombre, edad=edad, contrasenia=contrasenia, dia_registro=timezone.now())
		usuario.save()
		_id = usuario.id
		return HttpResponseRedirect( reverse( 'pagina:login', args=( _id, ) ) )

def vistaRegistroUsuario( request ):
	return render( request, 'pagina/registrarse.html')

def login( request, usuario_id ):
	usuario = get_object_or_404( Usuario, pk=usuario_id)
	return render( request, 'pagina/login.html',{
		'usuario': usuario
		})

