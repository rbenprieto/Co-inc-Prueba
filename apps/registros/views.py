from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


def home(request):
    usuariosregistrados = UsuariosInscritos.objects.all()
    return render(request, 'registros.html', {"registros": usuariosregistrados})


def registrarse(request):
    nombre = request.POST['txtNombre']
    email = request.POST['emlEmail']
    ciudad = request.POST['txtCiudad']

    registro = UsuariosInscritos.objects.create(nombre=nombre, email=email, ciudad=ciudad)
    return redirect('/formulario/')

def editar(request, id):
    registros = UsuariosInscritos.objects.get(id=id)
    return render(request, 'editarRegistros.html', {"registros": registros})

def cambiarRegistro(request):
    nombre = request.POST['txtNombre']
    email = request.POST['emlEmail']
    ciudad = request.POST['txtCiudad']

    registros = UsuariosInscritos.objects.get(id=id)
    registros.nombre = nombre
    registros.email = email
    registros.ciudad = ciudad
    return redirect('/formulario/')


def eliminarRegistro(request, id):
    registros = UsuariosInscritos.objects.get(id=id)
    registros.delete()

    return redirect('/formulario/')
