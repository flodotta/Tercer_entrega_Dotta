from django.shortcuts import render

#from control_usuarios.forms import CursoFormulario
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