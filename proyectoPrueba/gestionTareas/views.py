from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pagina.models import Usuario, Tarea
from django.utils import timezone
# Create your views here.


def gestionTareas( request, usuario_id ):
	usuario = Usuario.objects.get( pk=usuario_id)

	if request.method == 'POST' and request.POST['nuevaTarea'] != '':


		nuevaTarea = request.POST['nuevaTarea']
		usuario.tarea_set.create(
				nombreTarea=nuevaTarea,
				inicio = timezone.now(),
				finalizar = timezone.now(),
			)

	return render( request, 'gestionTareas/index.html', {
				'usuario': usuario
			})

