"""
URL configuration for proyecto_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from control_usuarios.views import listar_escritores , listar_articulos,\
    crear_escritor, crear_articulo, buscar_escritor, eliminar_articulo, editar_articulo,\
    LectorListView, LectorCreateView, LectorDetailView, LectorUpdateView , LectorDeleteView 

urlpatterns = [
    #URL de Escritores:
    path('escritores/', listar_escritores, name= "listar_escritores"),
    path('crear-escritor/', crear_escritor, name= "crear_escritor"),
    path('buscar-escritor/', buscar_escritor, name= "buscar_escritor"),
    
    #URL de Articulos
    path('articulos/', listar_articulos, name= "listar_articulos"),
    path('crear-articulo/', crear_articulo, name= "crear_articulo"),
    path('eliminar-articulo/<int:id>/', eliminar_articulo, name= "eliminar_articulo"),
    path('editar-articulo/<int:id>/', editar_articulo, name= "editar_articulo"),
    
    #URL de Lectores
    #path('lectores/', listar_lectores, name= "listar_lectores"),
    #path('crear-lector/', crear_lector, name= "crear_lector"),
    path("lectores/",LectorListView.as_view(),name="lista_lectores"),
    path("crear-lector/",LectorCreateView.as_view(),name="crear_lector"),
    path("lectores/<int:pk>/",LectorDetailView.as_view(),name="ver_lector"),
    path("editar-lector/<int:pk>/",LectorUpdateView.as_view(),name="editar_lector"),
    path("eliminar-lector/<int:pk>/",LectorDeleteView.as_view(),name="eliminar_lector")
]
