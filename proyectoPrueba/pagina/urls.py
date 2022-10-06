from django.urls import path
from . import views

app_name="pagina"
urlpatterns = [
	#localhost:8000/pagina
	path("", views.index, name="index"),
	#localhost:8000/pagina/peliculas
	path("todosLosUsuarios", views.todosLosUsuarios, name="todosLosUsuarios"),
	path("registrarse", views.vistaRegistroUsuario, name="registrarse"),
	path('registrarUsuario', views.registrarUsuario, name="registrarUsuario")
]