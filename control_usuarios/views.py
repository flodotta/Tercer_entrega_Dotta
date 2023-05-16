from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from control_usuarios.forms import LectorFormulario, EscritorFormulario, ArticuloFormulario
from control_usuarios.models import Lector, Escritor, Articulo

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
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

@login_required
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

@login_required
def eliminar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       articulo.delete()
       url_exitosa = reverse('listar_articulos')
       return redirect(url_exitosa)
   
 #Defino una vista para actualizar(update) Articulos 

@login_required
def editar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       formulario = ArticuloFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           
           articulo.nombre = data['nombre']
           articulo.codigo = data['codigo']
           articulo.categoria = data['categoria']
           articulo.fecha_publicacion=data['fecha_publicacion']
           
           articulo.save()
           
           url_exitosa = reverse('listar_articulos')
           return redirect(url_exitosa)
       
   else:  # GET
       inicial = {
           'nombre': articulo.nombre,
           'codigo': articulo.codigo,
           'categoria': articulo.categoria,
           'fecha_publicacion': articulo.fecha_publicacion,
       }
       formulario = ArticuloFormulario(initial=inicial)
   return render(
       request=request,
       template_name='control_usuarios/formulario_articulo.html',
       context={'formulario': formulario},
   )

  
#vistas basadas en clases

#Vistas de Lectores
class LectorListView(ListView):
    model = Lector
    template_name = 'control_usuarios/lista_lectores.html' #mismo que le pasaba al render

#Crear un Lector

class LectorCreateView(LoginRequiredMixin, CreateView):
    model = Lector
    fields = ( 'nombre','apellido', 'email')
    success_url = reverse_lazy('lista_lectores') #mismo que usaba en url exitosa pero con reverse_lazy

class LectorDetailView(DetailView):
    model = Lector
    succes_url= reverse_lazy('lista_lectores') 

class LectorUpdateView(LoginRequiredMixin,UpdateView):
    model = Lector
    fields = ('apellido', 'nombre', 'email')
    success_url = reverse_lazy('lista_lectores')

class LectorDeleteView(LoginRequiredMixin, DeleteView):
    model = Lector
    success_url = reverse_lazy('lista_lectores')   

