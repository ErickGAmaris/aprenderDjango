from django.contrib import admin
from pagina.models import Usuario, Tarea
# Register your models here.

admin.site.register([Usuario, Tarea])