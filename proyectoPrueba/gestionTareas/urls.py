from django.urls import path
from . import views

app_name="gestionTareas"
urlpatterns = [
	path("<int:usuario_id>", views.gestionTareas, name="gestionTareas"),

	
]