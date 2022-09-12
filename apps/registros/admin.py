from django.contrib import admin
from .models import *

@admin.register(UsuariosInscritos)
class UsuariosInscritosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'fecha_inscripcion',)

# Register your models here.
