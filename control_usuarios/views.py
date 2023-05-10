from django.shortcuts import render, redirect
from django.urls import reverse

from control_usuarios.forms import LectorFormulario
from control_usuarios.models import Lector, Escritor, Articulo


# Create your views Lectores here.
def listar_lectores(request):
    contexto = {
        "lectores": Lector.objects.all()
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_lectores.html',
        context=contexto,
    )
    return http_response

# Create your views Escritores here.
def listar_escritores(request):
    contexto = {
        "escritores": Escritor.objects.all()
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_escritores.html',
        context=contexto,
    )
    return http_response

# Create your views Articulos here.
def listar_articulos(request):
    contexto = {
        "articulos": Articulo.objects.all()
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_articulos.html',
        context=contexto,
    )

    
    return http_response

# Creao la view del formulario django

def crear_lector(request):
    if request.method == "POST":
        formulario = LectorFormulario(request.POST)

        if formulario.is_valid():
           data=formulario.cleaned_data
           nombre=data["nombre"]
           apellido=data["apellido"]
           email=data["email"]
           fecha_nacimiento=data["fecha_nacimiento"]
           lector = Lector(nombre=nombre, apellido=apellido, email=email,fecha_nacimiento=fecha_nacimiento)
           lector.save()
           url_exitosa=reverse('listar_lectores')
           return redirect(url_exitosa)
    else:  # GET
        formulario = LectorFormulario()
    http_response = render(
        request=request,
        template_name='control_usuarios/formulario_lector.html',
        context={'formulario': formulario}
    )
    return http_response
