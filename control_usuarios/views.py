from django.shortcuts import render, redirect
from django.urls import reverse

from control_usuarios.forms import LectorFormulario, EscritorFormulario, ArticuloFormulario
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

# Crea la view del formulario django para crear lector

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

# Crea la view del formulario django para crear escritor

def crear_escritor(request):
    if request.method == "POST":
        formulario = EscritorFormulario(request.POST)

        if formulario.is_valid():
           data=formulario.cleaned_data
           nombre=data["nombre"]
           apellido=data["apellido"]
           email=data["email"]
           telefono =data["telefono"]
           dni =data["dni"]     
           fecha_nacimiento=data["fecha_nacimiento"]
           escritor = Escritor(nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni, fecha_nacimiento=fecha_nacimiento)
           escritor.save()
           url_exitosa=reverse('listar_escritores')
           return redirect(url_exitosa)
    else:  # GET
        formulario = EscritorFormulario()
    http_response = render(
        request=request,
        template_name='control_usuarios/formulario_escritor.html',
        context={'formulario': formulario}
    )
    return http_response


# Crea la view del formulario django para crear Articulo

def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
           data=formulario.cleaned_data
           nombre=data["nombre"]
           codigo=data["codigo"]
           categoria=data["categoria"]  
           fecha_publicacion=data["fecha_publicacion"]
           articulo = Articulo(nombre=nombre, codigo=codigo, categoria=categoria, fecha_publicacion=fecha_publicacion)
           articulo.save()
           url_exitosa=reverse('listar_articulos')
           return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario()
    http_response = render(
        request=request,
        template_name='control_usuarios/formulario_articulo.html',
        context={'formulario': formulario}
    )
    return http_response

#DEfino una vista para buscar Escritores 

def buscar_escritor(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       escritor = Escritor.objects.filter(apellido__icontains=busqueda)
       contexto = {
           "escritores": escritor,
       }
       http_response = render(
           request=request,
           template_name='control_usuarios/lista_escritores.html',
           context=contexto,
       )
       return http_response
   

#Defino una vista para eliminar Articulos
def eliminar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       articulo.delete()
       url_exitosa = reverse('listar_articulos')
       return redirect(url_exitosa)
