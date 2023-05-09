from django.shortcuts import render

# Create your views Lectores here.
def listar_lectores(request):
    contexto = {
        "lectores": [
            {"nombre": "Cata" , "apellido": "Berton"} ,
            {"nombre": "Flo" , "apellido": "Berton"} ,
            {"nombre": "Mahia" , "apellido": "Berton"}, 
        ]
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
        "escritores": [
            {"nombre": "Emanuel" , "apellido": "Dautel"} ,
            {"nombre": "Flo" , "apellido": "Dotta"} ,
            {"nombre": "carlos" , "apellido": "perez"}, 
        ]
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
        "articulos": [
            {"nombre": "Nombre 1" , "categoria": "recetas"} ,
            {"nombre": "Nombre 2" , "categoria": "libros"} ,
            {"nombre": "Nombre 3" , "categoria": "deporte"} ,
        ]
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/lista_articulos.html',
        context=contexto,
    )
    return http_response