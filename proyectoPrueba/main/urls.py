from django.urls import path
from . import views

app_name="pagina"
urlpatterns = [
	#localhost:8000/pagina
	path("", views.home, name="home"),
]