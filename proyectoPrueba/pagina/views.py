from django.shortcuts import render
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
		dia_registro = timezone.now()
	except:
		return HttpResponse("Error")
	else:
		Usuario( nombre=nombre, contrasenia=contrasenia, dia_registro=dia_registro  ).save()
		return 	HttpResponseRedirect( reverse( "pagina:resultadoRegistro" ) )

def vistaRegistroUsuario( request ):
	return render( request, 'pagina/registrarse.html')

def resultadoRegistro( request ):
	return render( request, 'pagina/resultadoDelRegistro.html')

def validacionExistenteUsuario( request ):
	try:
		nombre = request.POST['nombreUsuario']
		contrasenia = request.POST['contraseniaUsuario']
		usuarioValidar = Usuario.objects.get(nombre=nombre)

	except :
		return render( request, 'pagina/index.html', {
			'error': 'Usuario no encontrado'
			})
	else:
		if( contrasenia == usuarioValidar.contrasenia ):
			return HttpResponseRedirect( reverse( 'gestionTareas:gestionTareas',
										  args=(usuarioValidar.id,)  ) )
		else:
			return render( request, 'pagina/index.html', {
					'error': 'Usuario o contrasenia no coincidentes'
				})

			# return HttpResponseRedirect( reverse( 'pagina:gestionTareas', args=(usuarioValidar.id) ) ) 





