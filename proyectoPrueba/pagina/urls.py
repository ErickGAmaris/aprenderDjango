from django.urls import path
from . import views


urlpatterns = [
	#localhost:8000/pagina
	path("", views.index, name="index"),
	#localhost:8000/pagina/peliculas
	path("peliculas/", views.peliculas, name="peliculas")
]