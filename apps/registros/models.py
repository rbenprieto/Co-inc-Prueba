from django.db import models


class UsuariosInscritos(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre completo')
    email = models.EmailField(verbose_name='Email')
    ciudad = models.CharField(max_length=255, verbose_name='Ciudad')
    fecha_inscripcion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Usuario Inscrito'
        verbose_name_plural = 'Usuarios Inscritos'
        ordering = ['id',]
