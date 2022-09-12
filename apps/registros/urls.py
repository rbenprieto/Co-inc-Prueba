from django.urls import path
from apps.registros.views import *
app_name = 'registros'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='inicio'),
    path('formulario/', home, name='formulario'),
    path('registrarse/', registrarse, name='registrarse'),
    path('formulario/editar/<int:id>', editar, name='editar'),
    # Acá está el error, no doy todavía con como debe ir la url pero debe ser algo tonto, pido disculpas
    path('editar/cambiarRegistro/', cambiarRegistro, name='cambiar-registros'),
    path('formulario/eliminarRegistro/<int:id>', eliminarRegistro, name='eliminar-registro'),

]